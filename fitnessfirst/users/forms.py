from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import User



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid Email Address.')
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    

    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = User.objects.get(email = email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already exists.')

    

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    # Validate email and password in the clean method
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login!")