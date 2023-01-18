from dataclasses import field, fields
import email
from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question1','question2','question3','question4']
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating',]
class JobForm(forms.ModelForm):
    class Meta:
        model = JobInfo
        fields = '__all__'
class ContactForm(forms.ModelForm):
    class Meta:
        model = Concerns
        fields = '__all__'
class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['employed','workPlace','yearsEmployment','yearGraduated','salaryRange',]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['linkedIn', 'gitHub', 'facebook','twitter']
class UserEditViewForm(UserChangeForm):
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-contro'}))
    last_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-contro'}))
    email =  forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = None
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
class IDApplicationForm(forms.ModelForm):
    class Meta:
        model = IDApplication
        fields = 'idNumber',
class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = '__all__'
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name']
