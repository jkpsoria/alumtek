from audioop import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

def alumni_login(request):

    if request.method == "POST":
        username = request.POST['login-username']
        password = request.POST['login-password']
        user = authenticate(request, username = username, password = password)

        if username == 'admin' and password == 'buggoys123':
            login(request,user)
            return redirect('AlumTeknew:admin_dashboard')
        if user is not None and user.last_login is None:
            login(request, user)
            return redirect('change_password')
            
        elif user is not None and user.last_login is not None:
            login(request, user)
            return redirect('AlumTeknew:products1')
        else:
            messages.error(request, ("Login error!"))
            return render(request, 'authenticate/login.html', {})

    else:

        return render(request, 'authenticate/login.html', {})

def alumni_logout(request):
    logout(request)
    messages.success(request,("You were logout!"))
    return redirect('alumni_login')



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'authenticate/password_success.html', {})



########################## ADMIN #################################


def admin_login(request):

    if request.method == "POST":
        username = request.POST['admin-username']
        password = request.POST['admin-password']
        user = authenticate(request, username = username, password = password)


        if user is not None and user.is_superuser == 1:
            login(request, user)
            return redirect('AlumTeknew:admin_dashboard')
        else:
            messages.error(request, ("Login error!"))
            return render(request, 'authenticate/admin_login.html', {})

    else:

        return render(request, 'authenticate/admin_login.html', {})



def admin_logout(request):
    logout(request)
    messages.success(request,("You were logout!"))
    return redirect('admin_login')
