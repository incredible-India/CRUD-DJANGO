from django import forms
from django.forms import widgets
from .models import student

class loginForm(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"
        labels = {'name' : "Name",'Usn': "Email","password":'Password'}
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control'}),
            'usn': forms.TextInput(attrs={'class' : 'form-control'})
            ,'password' : forms.PasswordInput(attrs={'class' : 'form-control'})

        }