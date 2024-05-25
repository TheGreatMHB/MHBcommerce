from django import forms


class ContactForm (forms.Form):
    fullname = forms.CharField()
    email = forms.CharField()
    content = forms.Textarea()
