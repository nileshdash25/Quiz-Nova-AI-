#from django.contrib import admin
#from Testapp.models import StudentInfo
# Register your models here.
#class StInfo(admin.ModelAdmin):
#    listInfo=['name','age','address']
#admin.site.register(StudentInfo,StInfo)
from django.contrib import admin
from Testapp.models import StudentInfo

# Register your models here.
class StInfo(admin.ModelAdmin):
    list_display = ['name', 'age', 'address','password'] # Change 'listInfo' to 'list_display'

admin.site.register(StudentInfo, StInfo)
