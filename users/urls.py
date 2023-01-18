from django.contrib import admin
from django.urls import path
from . import views
from .views import PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('alumni_login',  views.alumni_login, name="alumni_login"),
    path('alumni_logout',  views.alumni_logout, name="alumni_logout"),
    # path('change_password/', auth_views.PasswordChangeView.as_view
    # (template_name='authenticate/change_password.html'),name='change-password'),

    path('change_password/', PasswordsChangeView.as_view(template_name='authenticate/change_password.html'),name='change_password'),
    path('password_success', views.password_success, name="password_success"),
    

    #paths for reset password.... class based views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='authenticate/password_reset.html'), name="password_reset"), #pass reset view

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='authenticate/reset_password_sent.html'), name="password_reset_done"), #render success message

    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authenticate/reset_password_confirm.html'), name = "password_reset_confirm"), #link that user will get to reset pass 

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authenticate/reset_password_complete.html'), name= "password_reset_complete"),  #lets the user know that password is changed


    #paths for admin
    path('admin_login',  views.admin_login, name="admin_login"),
    path('admin_logout',  views.admin_logout, name="admin_logout"),


    

]
