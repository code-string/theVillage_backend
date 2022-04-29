from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your name',
        'rows':'4'
    }))
    phone = forms.RegexField(regex=r'^[0]\d{10}$', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your Phone number',
        'rows':'4'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':'your email here',
        'rows':'4'
    }))
    comment = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'your comment here',
        'rows': '4'
    }))


    class Meta:
        model=ContactUs
        fields=('fullname', 'phone', 'email', 'comment')