from django.urls import path
from Testapp import views
urlpatterns = [
    path('Database/',views.Temp),
    path('LoginForm/',views.LogiN),
    path('home/',views.loginaction),
    path('First/',views.Home),
    path('SendMail/', views.send_score_email, name='send_score_email'),
    path('logout/', views.logout_action, name='logout'),
    path('chat-api/', views.chatbot_response, name='chat_api'),
    path('LoginForm/', views.LogiN, name='login'),          # Login ke liye
    path('home/', views.Register_User, name='register'),
    path('thankyou/', views.ThankYou_Page, name='thank_you'),

]