from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Όνομα')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Μήνυμα')
