from django.conf import settings
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .models import Token,UserModel
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
import random

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

    email_val = UserModel.objects.filter(email=email)
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

    user = UserModel()
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    user.password=make_password(password1)
    user.active = 1
    user.token = 0
    user.save()
    
    messages.success(request,"Your Account Created")
    return HttpResponseRedirect('/account')

   
def login_post(request):
    email=request.POST['username']
    password=request.POST['password']
    user = UserModel.objects.filter(email=email)
    
    if user:
        data = UserModel.objects.filter(email=email).get()
        if check_password(password,data.password):
            request.session['useremail']=email
            request.session['username']=data.first_name
            request.session['userid']=data.id
            return HttpResponseRedirect('/user')
        messages.success(request,'Wrong Account Credentials')
        return HttpResponseRedirect('/account')   
    else:
        messages.success(request,'Wrong Account Credentials')
        return HttpResponseRedirect('/account')
   
def forgetpassword(request):
    return render(request,'login/forget.html')

def forgetmail(request):
    username = request.POST['username']
    user = UserModel.objects.filter(email=username)
    if not user:
        messages.success(request,"Invalid Email Address")
        return HttpResponseRedirect('/account/forget-password')
    token = random.randrange(1000000000,9999999999,10)
    Token.objects.filter(email=username).delete()
    data = Token()
    data.email = username
    data.token = token
    data.save()
     
    # email
    sub = "Reset Password"
    mess = "please click on the link to reset account password http://nahianofficial.pythonanywhere.com/account/link-verification/"+username+"/"+str(token)+"/"
    server_email=settings.EMAIL_HOST_USER
    to = username
    send_mail(sub,mess,server_email, [to,])


    messages.success(request,"Email Reset link sent to your email")
    return HttpResponseRedirect('/account')

def LinkVerification(request,email,token):
    data = Token.objects.filter(token=token,email=email)
    
    if data:
        request.session['useremail']=email
        return HttpResponseRedirect("/account/update-password")
    else:
        return HttpResponseRedirect("/")

def ResetPassword(request):
    if request.session.has_key('useremail'):
        return render(request,'login/updatepassword.html')
    else:
        return HttpResponseRedirect("/")

def UpdatePassword(request):
    
    if request.POST['password']==request.POST['repassword']:
        if len(request.POST['password'])<8:
            messages.success(request,"Password Must be more then 7 character")
            return HttpResponseRedirect('/account/update-password')
        
        password=make_password(request.POST['repassword'])
        data = UserModel.objects.filter(email=request.session['useremail']).update(password=password)
        messages.success(request,'Password Changed')
        return HttpResponseRedirect('/account')
    else:
        messages.success(request,'Password Doesnot match')
        return HttpResponseRedirect('/account/update-password')


    




        

    

