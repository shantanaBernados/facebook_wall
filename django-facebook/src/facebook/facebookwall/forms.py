from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.Form):
    post = forms.CharField(
        label='Status',
        max_length=100,
        widget=forms.Textarea(
            attrs={'placeholder': 'What\'s on your mind?'}
        )
    )


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
