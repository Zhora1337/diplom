from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        print(user)
        user.save()
        return user

class EditUserPhoto(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('photo',)