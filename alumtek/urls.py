from django.contrib import admin
from django.urls import path
from . import views
from .views import UserEditView
app_name = 'AlumTeknew'
urlpatterns = [
    path('index', views.MyIndexView.as_view(), name="my_index_view"),
    path('survey', views.MySurveyView.as_view(), name="my_survey_view"),
  #  path('subjects', views.RateSubjectView.as_view(), name="my_ratesubjects_view"),
  #delete subject 1819,223 
    path('subjects1617', views.SubjectsperCurriculum16.as_view(), name="my_subjectpercurriculum_view16"),
    path('jobboard',views.MyJobBoardView.as_view(), name="my_jobboard_view"),
    path('workdetails',views.MyWorkDetails.as_view(), name="my_work_details_view"),
    path('viewwork',views.MyViewWorkView.as_view(), name="my_view_work_view"),
    path('alumni_ID',views.MyAlumniIDView.as_view(), name="my_alumni_view"),
    path('profile', UserEditView.as_view(), name="my_profile_view"),
    #path('subjects',views.newDets, name="new_Dets"),
    path('addSocials', views.MySocialsView.as_view(), name="my_socials_view"),
    path('update_Socials', views.MyUpdateSocialView.as_view(), name ="my_update_socials_view"),
    path('add_Course', views.MyAddCourseView.as_view(), name ="my_add_course_view"),
    path('addCurriculum', views.MyAddCurriculumView.as_view(), name ="my_add_curriculum_view"),
    ########3
    path('subjects/', views.products1, name='products1'),
    path('course_details/<str:curriculum>', views.course_details, name='course_details'),
    
    path('rating_display/', views.curriculumList, name='curriculumList'),
    path('curriculum_rating/<str:curriculum>', views.curriculum_rating, name='curriculum_rating'),
    path('rating_list', views.RatingperCurriculum.as_view(), name="my_ratingpercurriculum_view"),
    #######3
    #admin
    path('admin_dashboard',views.AdminDashboard.as_view(), name="admin_dashboard"),
    path('admin_jobs',views.AdminJobs.as_view(), name="admin_jobs"),
    path('adminratingdashboard',views.AdminRatingDashboard.as_view(), name="admin_dashboard_view"),
    path('joblist',views.JobList.as_view(), name="admin_job_list_view"),
    path('addUser', views.AddUserView, name ="my_add_user_view"),

]
