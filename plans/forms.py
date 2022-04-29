from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    def __init__(self, plan_title, plan_price, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['plan'].initial = plan_title
        self.fields['plan'].disabled = True
        self.fields['price'].initial = plan_price
        self.fields['price'].disabled = True
        
    firstname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your first name',
        'class':'form-control',
        'rows':'4'
    }))
    lastname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your last name',
        'class':'form-control',
        'rows':'4'
    }))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Enter your email',
        'class':'form-control',
        'rows':'4'
    }))
    phone = forms.RegexField(regex=r'^[0]\d{10}$', max_length=15, widget=forms.TextInput(attrs={'placeholder':'your phone number',
        'class':'form-control',
        'rows':'4'
    }))
    plan = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class':'form-control',
        'rows': '4',
        'readonly': 'readonly'
    }))
    price = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class':'form-control',
        'rows': '4',
        'readonly': 'readonly'
    }))
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'4'
    }))


    class Meta:
        model = Booking
        fields = ('firstname','lastname', 'email', 'phone', 'price', 'plan')

   