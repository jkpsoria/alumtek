from distutils.command.upload import upload
from email.policy import default
from operator import mod
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Questions(models.Model):
    alumni = models.IntegerField("Alumni",blank=False,default=1, unique= True)
    question1 = models.CharField(max_length=500,default =False, blank = False)
    question2 = models.CharField(max_length=500,default =False, blank = False)
    question3 = models.CharField(max_length=500,default =False, blank = False)
    question4 = models.CharField(max_length=500,default =False, blank = False)
class Curriculum(models.Model):
    curriculum = models.CharField(max_length=255,default =False, blank = False,unique=True)
class Course(models.Model):
    curriculum = models.ForeignKey(Curriculum,to_field='curriculum',related_name='curriculum+', on_delete=models.CASCADE)
    departmentCourse = models.CharField(max_length=50,default=False,blank=False)
    courseYear = models.CharField(max_length=500,default=False,blank=False)
    csitcourse = models.CharField(max_length=255,default=False,blank=False,unique=True)
    courseName = models.CharField(max_length=500,default=False,blank=False)
class Rating(models.Model):
    curriculum = models.ForeignKey(Curriculum,to_field='curriculum',related_name='curriculum+', on_delete=models.CASCADE,default=False)
    alumni = models.IntegerField("Alumni",blank=False,default=1)
    csitcourse=models.ForeignKey(Course,to_field='csitcourse',related_name='csitcourse+', on_delete=models.CASCADE,default=None)
    rating=models.CharField(max_length=70)
class JobInfo(models.Model):
    jobtitle = models.CharField(max_length=100,default =False, blank = False)
    position = models.CharField(max_length=100,blank = False)
    workDetails = models.CharField(max_length=1000,blank = False)
    companyName = models.CharField(max_length=50,blank = False)
    qualifications = models.CharField(max_length=1000,blank = False)
    jobtype = models.CharField(max_length=50, default = False,blank = False)
class Work(models.Model):
    alumni = models.IntegerField("Alumni",blank=False,default=1, unique= True)
    employed = models.CharField(max_length=100,default =False, blank = False)
    workPlace = models.CharField(max_length=100,blank = False)
    yearsEmployment = models.CharField(max_length=1000,blank = False)
    yearGraduated = models.CharField(max_length=100,default =False, blank = False)
    salaryRange = models.CharField(max_length=100,default =False, blank = False)
class Concerns(models.Model):
    txtName = models.CharField(max_length=500,default =False, blank = False)
    txtEmail = models.EmailField(max_length=500,default =False, blank = False)
    txtPhone = models.CharField(max_length=500,default =False, blank = False)
    txtMsg = models.CharField(max_length=500,default =False, blank = False)
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, unique=True, on_delete=models.CASCADE)
    linkedIn = models.CharField(max_length = 256, blank=True, null=True)
    gitHub = models.CharField(max_length = 256, blank=True, null=True)
    facebook = models.CharField(max_length = 256, blank=True, null=True)
    twitter = models.CharField(max_length = 256, blank=True, null=True)
class IDApplication(models.Model):
    idNumber = models.ForeignKey(User,to_field='username',related_name='username+', on_delete=models.CASCADE,default=False)
    approve = models.BooleanField(default=False)