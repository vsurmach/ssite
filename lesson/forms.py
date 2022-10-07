from django import forms
from .models import HomeWork, MyUser


class PersonForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=50)


class PrForm(forms.Form):
    name = forms.CharField()
    tel = forms.CharField()


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = '__all__'


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'
