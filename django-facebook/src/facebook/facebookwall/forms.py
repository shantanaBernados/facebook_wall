from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import Post, Like


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


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        def save(self, commit=True):
            user = super(RegisterForm, self).save(commit=False)
            # first_name, last_name = self.cleaned_data["fullname"].split()
            # user.first_name = first_name
            # user.last_name = last_name
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
