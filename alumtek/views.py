from distutils.fancy_getopt import fancy_getopt
from multiprocessing import context
import re
from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserEditViewForm, CreateUserForm
from django.db.models import Avg
from django.urls import reverse_lazy
from django.db.models import Count
from django.db import IntegrityError
#imports
from math import ceil
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import F
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class MyIndexView(View): 
	def get(self, request):
		return render(request,'index.html',{})
	def post(self, request):
		form = ContactForm(request.POST)		
		if form.is_valid():
			txtName = request.POST.get("txtName")
			txtEmail = request.POST.get("txtEmail")
			txtPhone = request.POST.get("txtPhone")
			txtMsg = request.POST.get("txtMsg")
			form = Concerns(txtName=txtName,txtEmail=txtEmail,txtPhone=txtPhone,txtMsg=txtMsg)
			form.save()	
			return redirect('/index')
		else:
			messages.error(request, 'Please fill all the field')
			return redirect('/index')
class MySurveyView(View): 
	def get(self, request):
		return render(request,'survey.html',{})
	def post(self, request):		
		form = QuestionForm(request.POST)		
		if form.is_valid():
			try:
				alumni = request.user.id
				question1 = request.POST.get("question1")
				question2 = request.POST.get("question2")
				question3 = request.POST.get("question3")
				question4 = request.POST.get("question4")
				survey = form.save(commit=False)
				survey.alumni = request.user.id
				survey.save()	
				return redirect('/survey')
			except IntegrityError:
				messages.info(request, 'Your already answered this survey.')
				return render(request, 'survey.html',{'form':form})
		else:
			messages.info(request, 'Please fill all the field')
			return redirect('/survey')
def products1(request):
	products = Curriculum.objects.all()
	context = {'products':products}
	return render(request, 'subjects.html', context)
	
def course_details(request, curriculum):
	product = Curriculum.objects.get(curriculum=curriculum)
	course = Course.objects.filter(curriculum_id = product, courseYear= 'First Year')
	course2 = Course.objects.filter(curriculum_id = product, courseYear='Second Year')
	course3 = Course.objects.filter(curriculum_id = product, courseYear='Third Year')
	course4 = Course.objects.filter(curriculum_id = product, courseYear='Fourth Year')
	form = RatingForm(request.POST)		
	if form.is_valid():
		csitcourse = request.POST.get("csitcourse")
		curriculum = request.POST.get("curriculum")
		rating = request.POST.get("rating")
		form = Rating(csitcourse_id = csitcourse,curriculum_id=curriculum,rating=rating)
		form.alumni = request.user.id
		if Rating.objects.filter(csitcourse_id=csitcourse, curriculum=curriculum, alumni=request.user.id).exists():
			messages.info(request, 'You already added rating for this course.')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			form.save()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	context = {
		'product': product,
		'course' : course,
		'course2' : course2,
		'course3': course3,
		'course4' : course4,
	}
	return render(request, 'subjects1617.html', context)
class SubjectsperCurriculum16(View): 
	def get(self, request):
		return render(request,'subjects1617.html',{})
def curriculumList(request):
	curriculums = Curriculum.objects.all()
	context = {'curriculums':curriculums}
	return render(request, 'rating_display.html', context)
def curriculum_rating(request, curriculum):
	curriculum = Curriculum.objects.get(curriculum=curriculum)
	average = Rating.objects.filter(curriculum_id=curriculum).values("csitcourse").annotate(avg_rating=Avg("rating"))
	context = {
		'average' : average,
	}
	return render(request, 'rating_list.html', context)
class RatingperCurriculum(View): 
	def get(self, request):
		return render(request,'rating_list.html',{})

def AddUserView(request):
		form = CreateUserForm(request.POST)		
		if form.is_valid():
			form.save()
			return redirect('/addUser')
		context = {
			'form': form,
		}
		return render(request,'addUser.html',context)
class MyJobBoardView(View): 
	def get(self, request):	
		if 'q' in request.GET:
			q = request.GET['q']
			jobdetails = JobInfo.objects.filter(jobtitle__icontains=q)
		else:
			jobdetails = JobInfo.objects.all()
		context = {
			'jobdetails' : jobdetails,
			}
		return render(request,'jobboard.html',context)

class UserEditView(generic.UpdateView):
		form_class = UserEditViewForm
		template_name = 'profile.html'
		success_url = reverse_lazy('AlumTeknew:my_profile_view')
		
		def get_object(self):
			return self.request.user			
class MyViewWorkView(View): 
	def get(self, request):
		viework = Work.objects.all()
		context = {
			'viework' : viework,
		}
		return render(request,'viewwork.html',context) 
	def post(self,request):
		if 'btnWorkDetails'in request.POST:
			alumni = request.user.id
			employed = request.POST.get("employed")
			workPlace = request.POST.get("workPlace")
			yearsEmployment = request.POST.get("yearsEmployment")
			yearGraduated = request.POST.get("yearGraduated")
			salaryRange = request.POST.get("salaryRange")
			update_work = Work.objects.filter(alumni = alumni).update(employed=employed,workPlace=workPlace,yearsEmployment=yearsEmployment,yearGraduated=yearGraduated,salaryRange=salaryRange)
			print(update_work)
			print('Work Updated')
			return redirect('/viewwork')
		elif 'btndeleteWorkDetails' in request.POST:
				alumni = request.user.id 
				alumni= Work.objects.filter(alumni = alumni).delete()
				print('deleted')
				return redirect('/index')		
class MyWorkDetails(View): 
	def get(self, request):
		return render(request,'workdetails.html',{}) 
	def post(self, request):		
		form = WorkForm(request.POST)		
		if form.is_valid():
			try: 
				employed = request.POST.get("employed")
				workPlace = request.POST.get("workPlace")
				yearsEmployment = request.POST.get("yearsEmployment")
				yearGraduated = request.POST.get("yearGraduated")
				salaryRange = request.POST.get("salaryRange")
				work = form.save(commit=False)
				work.alumni = request.user.id
				work.save()	
				return redirect('/viewwork')
			except IntegrityError:
				print(form.errors)
				return render(request, 'workdetails.html',{'form':form})
		else:
			print(form.errors)
			return HttpResponse('not valid')
class MyAlumniIDView(View): 
	def get(self, request):
		return render(request,'alumni_ID.html',{})
	def post(self, request):		
		form = IDApplicationForm(request.POST)		
		if form.is_valid():
			idNumber = request.POST.get("idNumber")
			form = IDApplication(idNumber_id=idNumber)
			if IDApplication.objects.filter(idNumber_id=idNumber).exists():
				messages.info(request, 'Your Alumni ID Application is already being process.')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			else:
				form.save()
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			print(form.errors)
			return HttpResponse('not valid')
class MySocialsView(View):
	def get(self,request):
		return render(request, 'addSocials.html',{})
	def post(self,request):
		form = ProfileForm(request.POST)
		if form.is_valid():
			try:
				linkedIn = request.POST.get("linkedIn")
				gitHub = request.POST.get("gitHub")
				facebook = request.POST.get("facebook")
				twitter = request.POST.get("twitter")
				socials = form.save(commit=False)
				socials.user_id = request.user.id
				socials.save()
				return redirect('/profile')
			except IntegrityError:
				print(form.errors)
				return render(request, 'profile.html',{'form':form})
		else:
			print(form.errors)
			return HttpResponse('not valid')
class MyUpdateSocialView(View):
	def get(self,request):
		viewSocials = Profile.objects.all()
		context = {
			'viewSocials' : viewSocials,
		}		
		return render(request, 'update_Socials.html',context)
	def post(self,request):
		if 'btnUpdateSocials'in request.POST:
			user = request.user.id
			linkedIn = request.POST.get("linkedIn")
			gitHub = request.POST.get("gitHub")
			facebook = request.POST.get("facebook")
			twitter = request.POST.get("twitter")
			update_work = Profile.objects.filter(user_id = user).update(linkedIn=linkedIn,gitHub=gitHub,facebook=facebook,twitter=twitter)
			print(update_work)
			return redirect('/profile')
		elif 'btnDeleteWorkDetails' in request.POST:
				user = request.user.id 
				delete_user = Profile.objects.filter(user_id = user).delete()
				print(delete_user)
				return redirect('/profile')		
class MyAddCourseView(View):
	def get(self,request):
		curriculums = Curriculum.objects.all()
		context ={
			'curriculums' : curriculums,
		}
		return render(request,'add_Course.html',context)
	def post(self, request):		
		form = CourseForm(request.POST)		
		if form.is_valid():
			curriculum = request.POST.get("curriculum")
			departmentCourse = request.POST.get("departmentCourse")
			courseYear = request.POST.get("courseYear")
			csitcourse = request.POST.get("csitcourse")
			courseName = request.POST.get("courseName")
			form = Course(curriculum_id=curriculum,departmentCourse=departmentCourse,courseYear=courseYear,csitcourse=csitcourse,courseName=courseName)
			form.save()	
			return redirect('/add_Course')
		else:
			print(form.errors)
			return HttpResponse('not valid')
class MyAddCurriculumView(View):
	def get(self,request):
		return render(request,'add_Curriculum.html',{})
	def post(self, request):		
		form = CurriculumForm(request.POST)		
		if form.is_valid():
			curriculum = request.POST.get("curriculum")
			form = Curriculum(curriculum=curriculum)
			form.save()	
			return redirect('/addCurriculum')
		else:
			print(form.errors)
			return HttpResponse('not valid')





############### ADMIN #######################

class AdminDashboard(View):
	def get(self, request):
		employed_count = Work.objects.filter(employed__startswith="Yes").annotate(num_employed=Count('employed'))
		unemployed_count = Work.objects.filter(employed__startswith="No").annotate(num_employed=Count('employed'))
		local_count = Work.objects.filter(workPlace__startswith="Local").annotate(num_workPlace=Count('workPlace'))
		international_count = Work.objects.filter(workPlace__startswith="International").annotate(num_workPlace=Count('workPlace'))
		none_count = Work.objects.filter(workPlace__startswith="None").annotate(num_workPlace=Count('workPlace'))
		countYear = Work.objects.all().values("yearGraduated").annotate(total=Count("yearGraduated")).order_by('-total')
		countSalary = Work.objects.all().values("salaryRange").annotate(total=Count("salaryRange")).order_by('-total')
		idApplicationList = IDApplication.objects.filter(approve = False)
		activeUser = User.objects.exclude(last_login__isnull=True).count()
		inActiveUser = User.objects.filter(last_login__isnull=True).count()
		totalUser = User.objects.all().count()
		q1 = Questions.objects.values()
		average = Rating.objects.values("csitcourse").annotate(avg_rating=Avg("rating"))
		context = {
			'employed_count' : employed_count,
			'unemployed_count' : unemployed_count,
			'local_count' : local_count,
			'international_count' : international_count,
			'none_count' : none_count,
			'countYear' : countYear,
			'countSalary' : countSalary,
			'idApplicationList' : idApplicationList,
			'activeUser' : activeUser,
			'totalUser' : totalUser,
			'inActiveUser' : inActiveUser,
			'q1' : q1,
			'average' : average,
		}
		return render(request,'admin_dashboard.html',context)
	def post(self,request):
		if(request.method) == 'POST':
			if 'btnApproveIDProcessing'in request.POST:
				iddn = request.POST.get("id")
				approve = True
				approve_id = IDApplication.objects.filter(id = iddn).update(approve=approve)
				print(approve_id)
				print('ID is being process')
				return redirect('/admin_dashboard')
class AdminJobs(View): 
	def get(self, request):
		return render(request,'admin_jobs.html',{})
	def post(self, request):
		form = JobForm(request.POST)		
		if form.is_valid():
			jobtitle = request.POST.get("jobtitle")
			position = request.POST.get("position")
			workDetails = request.POST.get("workDetails")
			companyName = request.POST.get("companyName")
			qualifications = request.POST.get("qualifications")
			jobtype = request.POST.get("jobtype")
			form = JobInfo(jobtitle=jobtitle,position=position,workDetails=workDetails,companyName=companyName,qualifications=qualifications,jobtype=jobtype)
			form.save()	
			return redirect('/admin_jobs')
		else:
			print(form.errors)
			return HttpResponse('not valid')
class JobList(View): 
	def get(self, request):
		jobboarddetails=JobInfo.objects.all()
		coursedetails=Course.objects.all()
		curriculumdetails = Curriculum.objects.all()
		processedID = IDApplication.objects.filter(approve='1')
		concerns = Concerns.objects.all()
		context = {
			'coursedetails' : coursedetails,
			'jobboarddetails' : jobboarddetails,
			'curriculumdetails' : curriculumdetails,
			'processedID' : processedID,
			'concerns' : concerns,
		}
		return render(request,'joblist.html',context)
	def post(self,request):
		if 'BtnUpdateJobBoard'in request.POST:
			id = request.POST.get("id")
			jobtitle = request.POST.get("jobtitle")
			position = request.POST.get("position")
			workDetails = request.POST.get("workDetails")
			companyName = request.POST.get("companyName")
			qualifications = request.POST.get("qualifications")
			jobtype = request.POST.get("jobtype")		
			update_job = JobInfo.objects.filter(id = id).update(jobtitle=jobtitle,position=position,workDetails=workDetails,companyName=companyName,qualifications=qualifications,jobtype=jobtype)
			print(update_job)
			print('Job Updated')
			return redirect('/joblist')
		elif 'BtnDeleteJobHiring' in request.POST:
			iddn = request.POST.get("id") 
			iddn= JobInfo.objects.filter(id = iddn).delete()
			print('deleted')
			return redirect('/joblist')	
		elif 'BtnUpdateCourse' in request.POST:
			id = request.POST.get("id")
			csitcourse = request.POST.get("csitcourse")
			curriculum_id = request.POST.get("curriculum")
			departmentCourse = request.POST.get("departmentCourse")
			courseName = request.POST.get("courseName")
			courseYear = request.POST.get("courseYear")
			update_course = Course.objects.filter(id = id).update(csitcourse=csitcourse,curriculum=curriculum_id,courseName=courseName,departmentCourse=departmentCourse,courseYear=courseYear)
			print(update_course)
			return redirect('/joblist')
		elif 'BtnDeleteCourse' in request.POST:
			iddn = request.POST.get("id") 
			iddn= Course.objects.filter(id = iddn).delete()
			return redirect('/joblist')	
		elif 'BtnUpdateCurriculum' in request.POST:
			id = request.POST.get("id")
			curriculum = request.POST.get("curriculum")
			update_curriculum = Curriculum.objects.filter(id = id).update(curriculum=curriculum)
			print(update_curriculum)
			return redirect('/joblist')
		elif 'BtnDeleteCurriculum' in request.POST:
			iddn = request.POST.get("id") 
			iddn= Curriculum.objects.filter(id = iddn).delete()
			return redirect('/joblist')	
class AdminRatingDashboard(View): 
	def get(self, request):
		average = Rating.objects.values("csitcourse").annotate(avg_rating=Avg("rating"))
		context={
			'average' : average,
		}
		return render(request,'adminratingdashboard.html',context)
