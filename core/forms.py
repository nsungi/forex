
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (ImageUpload, TextUpload, Course, Technical,
                     Fundamental, Risk, Analysis, Trick, Pschology, Pair
                ) 


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        messages = {
            'username': {
                'required': 'Please enter your username.',
                'unique': 'This username is already taken. Please choose a different one.',
                'max_length': 'Username is too long.',
            },
            'email': {
                'required': 'Please enter your email address.',
                'unique': 'This email address is already registered. Please use a different one.',
                'invalid': 'Please enter a valid email address.',
                'max_length': 'Email address is too long.',
            },
            'password1': {
                'required': 'Please enter a password.',
                'min_length': 'Password must be at least 8 characters long.',
            },
            'password2': {
                'required': 'Please confirm your password.',
                'mismatch': 'Passwords do not match. Please enter the same password in both fields.',
            },
        }
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)



        

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['user', 'image' ,'description']

class TextUploadForm(forms.ModelForm):
    class Meta:
        model = TextUpload
        fields = ['user', 'text_content']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['user', 'title']

class TechnicalForm(forms.ModelForm):
    class Meta:
        model = Technical
        fields = ['user', 'title', 'image', 'texts']

#Fundamental form
class FundamentalForm(forms.ModelForm):
    class Meta:
        model = Fundamental
        fields = ['user', 'title','texts', 'image']

        
        
# Risk form        
class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['user', 'title','texts', 'image']

class AnalysisForm(forms.ModelForm):
    class Meta:
        model = Analysis
        fields = ['user', 'title','texts', 'image']

class TrickForm(forms.ModelForm):
    class Meta:
        model = Trick
        fields = ['user', 'title','texts', 'image']

class PschologyForm(forms.ModelForm):
    class Meta:
        model = Pschology
        fields = ['user', 'title','texts', 'image']

class PairForm(forms.ModelForm):
    class Meta:
        model = Pair
        fields = ['user', 'title','texts', 'image']

