from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post']
        widgets = {
            'post': forms.Textarea(
                attrs={
                    'required': True, 
                    'placeholder': 'What\'s on your mind?',
                    'autofocus': True,
                    'cols': 55,
                    'rows': 5
                }
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    # first_name = forms.CharField(label="First name")
    # last_name = forms.CharField(label="Last name")

    class Meta:
        model = User
        # fields = ("first_name", "last_name", "email")
        fields = ("username", "email",)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # first_name, last_name = self.cleaned_data["fullname"].split()
        # user.first_name = first_name
        # user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
