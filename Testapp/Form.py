from django import forms
from Testapp.models import StudentInfo
class StudentForm(forms.ModelForm):
    RePassword=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'* * * * *','id':'repsd'}))
    value=forms.CharField(max_length=68,required=False,widget=forms.HiddenInput)
    class Meta:
       model=StudentInfo
       widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name','id':'name'}),
                  'age':forms.TextInput(attrs={'placeholder': 'Age', 'id':'age'}),
                  'address':forms.TextInput(attrs={'placeholder': 'Address','id':'adrs'}),
                  'email':forms.TextInput(attrs={'placeholder': 'email','id':''}),
                  'password':forms.PasswordInput(attrs={'placeholder': '* * * * *','id':'psd'}),
                  }
       fields='__all__' 
    def clean(self):
        data=super().clean()
        pas=data['password']
        repas=data['RePassword']
        val=data['value']
        if pas!=repas:
            raise forms.ValidationError('Both password should be same ')
        if len(val)>0:
            raise forms.ValidationError('thanks bot for comeing')