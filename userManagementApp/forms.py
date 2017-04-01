from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control input-lg','width': '450px','placeholder':'Имя пользователя'}))
    password1 = forms.CharField(label='Введите пароль',required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control input-lg','width': '450px','placeholder':'Пароль'}))
    password2 = forms.CharField(label='Повторите пароль',required=True,widget=forms.TextInput(attrs={'class': 'form-control input-lg','width': '450px','placeholder':'Повторите пароль'}))
    email = forms.EmailField(required=True, error_messages='', widget=forms.TextInput(attrs={'class': 'form-control input-lg','width': '450px','placeholder':'Ваш email'}))
    first_name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control input-lg','width': '450px','placeholder':'Ваше имя'}))
    #first_name = forms.BooleanField(disabled=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')
class UserChangeForm(forms.ModelForm):

    """
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']