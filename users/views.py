from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.


def login(request):
     if request.method == 'POST':
          Username = request.POST['email']
          Password = request.POST['password']

          User = authenticate(username = Username, password=Password)
          if User is not None:
               auth.login(request,User)
               messages.success(request, 'Login Successfully.')
               return redirect ('/')
          else:
               messages.error(request, 'Invalid username or password.')
               return redirect ('/auth/login')
     return render(request, 'login.html')

def register(request):

     if request.method == 'POST':
          Username = request.POST['email']
          First_name = request.POST['firstname']
          Last_name = request.POST['lastname']
          Email = request.POST['email']
          Password = request.POST['pass']
          Confirm_Password = request.POST['pass2']

          if Password != Confirm_Password:
               messages.error(request, 'Password did not match')
               return redirect ('/auth/register')
          user = User.objects.create_user(username=Username, first_name=First_name, last_name =Last_name,email=Email,password=Password)
          user.save()
          messages.success(request, 'User Create Successfully.')
          return redirect ('/auth/login')

     return render(request, 'register.html')

def syslogout(request):
     logout(request)
     messages.success(request, 'User Logout Successfully.')
     return redirect ('/')
     return HttpResponse ("Response Redirect")

def profile(request):
     return render(request, 'profile.html')