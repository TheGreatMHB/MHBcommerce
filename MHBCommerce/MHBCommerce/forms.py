from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User


class ContactForm (forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Full Name"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Message"
            }
        )
    )

    def email_validation(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be Gmail")
        return email


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=200, min_length=4, required=True, label='FirstName',
        widget=forms.TextInput(
            attrs={'id': 'first_name',
                   'class': 'form-control',
                   'placeholder': 'Paul'}
        )
    )
    last_name = forms.CharField(
        max_length=200, min_length=4, required=True, label='Last Name',
        widget=forms.TextInput(
            attrs={'id': 'last_name',
                   'class': 'form-control',
                   'placeholder': 'Anderson'}
        )
    )
    username = forms.CharField(
        max_length=200, min_length=4, required=True, label='Username',
        widget=forms.TextInput(
            attrs={'id': 'username',
                   'class': 'form-control',
                   'placeholder': 'Paul_A0691'}
        )
    )
    email = forms.CharField(
        max_length=200, min_length=4, required=True, label='Email',
        widget=forms.TextInput(
            attrs={'id': 'email',
                   'type': 'email',
                   'class': 'form-control',
                   'placeholder': 'Paul.Anderson@gmail.com'}
        )
    )
    password = forms.CharField(
        max_length=200, min_length=4, required=True, label='Password',
        widget=forms.TextInput(
            attrs={'id': 'password',
                   'class': 'form-control',
                   'type': 'password',
                   'placeholder': '*123QWE@ewq*'}
        )
    )
    password2 = forms.CharField(
        max_length=200, min_length=4, required=True, label='Password Confirm',
        widget=forms.TextInput(
            attrs={'id': 'password',
                   'class': 'form-control',
                   'type': 'password',
                   'placeholder': '*123QWE@ewq*'}
        )
    )

    def duplicate_username_validation(self):
        username = self.cleaned_data.get('username')
        this_user = User.objects.filter(username=username)
        if this_user.exists():
            raise forms.ValidationError("Username is taken !!")
        return username

    def duplicate_email_validation(self):
        email = self.cleaned_data.get('email')
        this_user = User.objects.filter(email=email)
        if this_user.exists():
            raise forms.ValidationError("Email is taken !!")
        return email

    def password_match_validation(self):
        data = self.cleaned_data
        password = data.get("password")
        password2 = data.get("password2")

        if password != password2:
            raise forms.ValidationError("Password is not match !")

    # def user_duplicate_validation(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')
    #     all_users = User.objects.all()
    #     for user in all_users:
    #         if user.username == str(username):
    #             self.errors[""] = self.error_class(
    #                 ["User already exist"])
    #         elif user.email == email:
    #             self.errors[""] = self.error_class(["E-mail already in use"])
    #         else:
    #             pass

        # super(RegisterForm, self).clean()
        # if password != password2:
        #     self.errors[""] = self.error_class(
        #         ["The two password fields must match"])

        # for instance in User.objects.all():
        #     if instance.username == str(username):
        #         self.errors[""] = self.error_class(["User already exist"])
        #     elif instance.email == email:
        #         self.errors[""] = self.error_class(["E-mail already in use"])
        #     else:
        #         pass

        return data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200, min_length=4, required=True, label='Username',
        widget=forms.TextInput(
            attrs={'id': 'username',
                   'class': 'form-control',
                   'placeholder': 'Paul_Anderson'}
        )
    )
    password = forms.CharField(
        max_length=200, min_length=4, required=True, label='Password',
        widget=forms.TextInput(
            attrs={'id': 'password',
                   'class': 'form-control',
                   'type': 'password',
                   'placeholder': '*123QWE@ewq*'}
        )
    )
