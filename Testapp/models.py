from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name=models.CharField(max_length=56)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=78)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name
