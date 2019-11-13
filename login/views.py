from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    return render(request,"login/login.html")
def signup(request):
    return render(request,"login/signup.html")

def signup_post(request):
   
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    user=User.objects.create_user(username=email,password=password,email=email,
    first_name=first_name,last_name=last_name,is_superuser=1)
    user.save()
    return HttpResponse("ok")

def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/superuser')
    else:
        return HttpResponse("Password missmatch")
   


