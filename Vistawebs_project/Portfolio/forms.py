from django import forms 
from .models import Contact_message

class Contact_form(forms.ModelForm):
    name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={
        'class': 'input-field', 'placeholder':'Your name'
    }))
    phone_number = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={
        'class': 'input-field', 'placeholder':'Phone number'
    }))
    email = forms.CharField(max_length = 250, widget=forms.EmailInput(attrs={
        'class': 'input-field', 'placeholder':'Email'
    }))
    subject = forms.CharField(max_length = 250, widget=forms.TextInput(attrs={
        'class': 'input-field', 'placeholder':'Subject'
    }))
    message = forms.CharField(max_length = 250, widget=forms.Textarea(attrs={
        'class': 'input-field textarea-field', 'placeholder':'Your message', 'rows': 5
    }))
    class Meta:
        model = Contact_message
        fields = ['name','phone_number', 'email','subject','message']