from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import StudentInfo
from Testapp.Form import StudentForm
# New SDK Import
from google import genai
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql

# --- 1. CLIENT SETUP (FIXED VERSION) ---
# 'v1' hata kar 'v1beta' kiya kyunki Gemini 2.5/2.0 wahin available hain
client = genai.Client(
    api_key="AIzaSyCWP-RqeP8KGTH6LOV4sbSLmevrT1junQw",
    http_options={"api_version": "v1beta"} 
)

# --- 2. LOGIN & DATABASE (TERA PURANA LOGIC) ---
em = ''
pwd = ''

def Temp(req):
    s = StudentInfo.objects.all()
    return render(req, 'FetchDatabase.html', {'stu': s})

def LogiN(req):
    if req.method == 'POST':
        fm = StudentForm(req.POST)
        if fm.is_valid():
            email_input = fm.cleaned_data['email']
            if StudentInfo.objects.filter(email=email_input).exists():
                return render(req, 'error.html', {'msg': 'Email already registered!'})
            fm.save()
            return redirect('/Test/thankyou/')
    else:
        fm = StudentForm()
    return render(req, 'Register.html', {'form': fm})

def Register_User(req):
    return LogiN(req)

def loginaction(request):
    global em, pwd
    if request.method == "POST":
        # Tera MySQL Connection
        m = sql.connect(
            host="nileshdash24.mysql.pythonanywhere-services.com",
            user="nileshdash24",
            passwd="Nobita@2002",
            database="nileshdash24$database8"
        )
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email": em = value
            if key == "password": pwd = value

        c = "select * from Testapp_studentinfo where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())

        if t == ():
            return render(request, 'error.html')
        else:
            user_name = t[0][1]
            user_email = t[0][4]
            request.session['user_email'] = user_email
            request.session['user_name'] = user_name
            try:
                send_mail('Login Successful', f'Welcome {user_name}', settings.EMAIL_HOST_USER, [user_email], fail_silently=True)
            except: pass
            return render(request, "welcome.html")
    return render(request, 'login_page.html')

def send_score_email(request):
    if request.method == "POST":
        recipient = request.POST.get('user_email')
        score = request.POST.get('score')
        try:
            send_mail('Quiz Score', f'Score: {score}', settings.EMAIL_HOST_USER, [recipient], fail_silently=True)
            return render(request, 'welcome.html', {'msg': 'Sent!', 'score': score})
        except: return render(request, 'welcome.html', {'msg': 'Error', 'score': score})
    return redirect('/Test/home/')

def logout_action(request):
    user_email = request.session.get('user_email')
    if user_email:
        try: send_mail('Logout', 'Visit again!', settings.EMAIL_HOST_USER, [user_email], fail_silently=True)
        except: pass
    request.session.flush()
    return redirect('/Test/home/')

def Home(req): return render(req, 'Home.html')
def ThankYou_Page(req): return render(req, 'thankyou.html')

# --- 3. CHATBOT (MODEL ROTATOR + v1beta) ---
@csrf_exempt
def chatbot_response(request):
    user_msg = request.GET.get("msg") or request.POST.get("msg")
    if not user_msg: return JsonResponse({"reply": "Kuch toh pucho! 🌸"})

    # Tere account mein jo models available hain (list ke hisaab se)
    # 2.0-flash sabse stable hai, 2.5 naya hai.
    models_to_try = [
        "gemini-2.0-flash", 
        "gemini-2.5-flash",
        "gemini-flash-latest"
    ]

    last_error = ""

    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=user_msg
            )
            # Agar reply aaya toh yahi se bhej do
            return JsonResponse({"reply": response.text})
        except Exception as e:
            last_error = str(e)
            continue # Agla model try karo

    # Agar saare fail ho gaye
    print(f"Chatbot Failed: {last_error}")
    if "429" in last_error:
        return JsonResponse({"reply": "Quota Full (429). Kal aana! 🌸"})
    
    return JsonResponse({"reply": "Server Error. Try again later."})