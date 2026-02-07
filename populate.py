import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Loginform.settings')
import django
django.setup()
from random import randint
from faker import Faker
from Testapp.models import StudentInfo
fake=Faker()
def Age():
    num=randint(20,100)
    return int(num)
def Papu(n):
    for i in range(n):
        fname=fake.name()
        fage=Age()
        faddress=fake.address()
        fmail=fake.email()
        stero=StudentInfo.objects.get_or_create(name=fname,age=fage,address=faddress,email=fmail)
Papu(25)
