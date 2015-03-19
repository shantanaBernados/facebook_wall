from django import forms


class PostForm(forms.Form):
    your_name = forms.CharField(
        label='Status',
        max_length=100,
        widget=forms.Textarea(
            attrs={'placeholder': 'What\'s on your mind?'}
        )
    )
