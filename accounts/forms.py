from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from . models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'max_length':60, 
        'help_text':'Required. Add a valid email address'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'max_length':120, 
        'help_text':'Please provide your first name name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'max_length':123, 
        'help_text':'please provide your last name'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    phone_number = forms.RegexField(regex=r'^[0]\d{10}$', widget=forms.TextInput(attrs={
        'class':'form-control',
        'max_length':11, 
        'help_text':'Please provide your phone number'
    }))

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2", "first_name", "last_name", "phone_number")

    
    




class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'label':'Password',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'label':'Email'
    }))

    class Meta:
        model = Account
        fields = ("email", "password")

    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login Details")


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'phone_number', 'first_name', 'last_name', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account)
            
    
    def clean_username(self):
        if self.is_valid():
            email = self.cleaned_data['username']

            try:
                username = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % account.username)
