from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required  
# def index(request):
#     if request.user.is_authenticated:
#         return render(request,'user/index.html')
#     else:
#         return HttpResponseRedirect('/account/')


@login_required
def index(request):
    return render(request,'user/index.html')
def logoutUser(request):
    logout(request)
    return HttpResponse("logout")

    