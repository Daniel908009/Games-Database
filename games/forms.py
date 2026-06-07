from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Review, UserProfile


User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Internal handle',
        widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Internal handle',
        max_length=150,
        help_text='This handle is used to log in and must be unique.'
    )

    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Internal handle', max_length=150)

    class Meta:
        model = UserProfile
        fields = ('display_name', 'bio', 'avatar')
        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = self.user.username
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['display_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your display name'})
        self.fields['bio'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'placeholder': 'Tell people about yourself'})
        self.fields['avatar'].widget.attrs.update({'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if User.objects.exclude(pk=self.user.pk).filter(username__iexact=username).exists():
            raise forms.ValidationError('That internal handle is already taken.')
        return username

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user.username = self.cleaned_data['username']
        if commit:
            profile.user.save()
            profile.save()
        return profile


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('value', 'note')
        widgets = {
            'value': forms.HiddenInput(),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your thoughts...'}),
        }


class SearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search games, studios, or handles'})
    )
