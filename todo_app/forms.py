from django import forms
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class todoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description','completed']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title f1',}),
            'description': forms.Textarea(attrs={'class': 'form-title',}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class signupForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'class': 'form-input',
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'class': 'form-input',
            'autocomplete': 'off',
        })
        self.fields["password1"].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'class': 'form-input',
        })
        self.fields["password2"].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'class': 'form-input',
        })

class loginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'class': 'form-input',
        })
        self.fields["password"].widget.attrs.update({
            'required': '',
            'name': 'password',
            'id': 'password',
            'class': 'form-input',
        })