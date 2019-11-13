from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User,auth


# Create your views here.

if __name__ == "__main__":
    MiddleWare()
    

def MiddleWare(request):
    if user.is_authenticated:
        pass
    else:
        return HttpResponseRedirect('account/login')


def index(request):
    return render(request,'superuser/index.html')