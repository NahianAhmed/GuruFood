from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request,"login/login.html")
def signup(request):
    return render(request,"login/signup.html")

def signup_post(request):

    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password1=request.POST['password']
    password2=request.POST['re-password']

    email_val = User.objects.filter(username=email)
    if email_val:
        messages.success(request,"Email Already Taken")
        return HttpResponseRedirect('/account/sign-up')
    if not first_name or not last_name or not email:
        messages.success(request,"Please Fill up all fields")
        return HttpResponseRedirect('/account/sign-up')
    if password1!=password2:
        messages.success(request,"Password doesn't match")
        return HttpResponseRedirect('/account/sign-up')
    if len(password1)<8:
        messages.success(request,"Password Must be more then 7 character")
        return HttpResponseRedirect('/account/sign-up') 

    user=User.objects.create_user(username=email,password=password1,email=email,
    first_name=first_name,last_name=last_name,is_superuser=0,is_staff=0,is_active=1)
    user.save()
    messages.success(request,"Your Account Created")
    return HttpResponseRedirect('/account')

   
def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        if user.is_staff:
            return HttpResponseRedirect('/admin')
        else:
            return HttpResponseRedirect('/user') 
    else:
        messages.success(request,'Wrong Account Credentials')
        return HttpResponseRedirect('/account')
   


