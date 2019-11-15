from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout

# Create your views here.


if __name__ == '__main__':
    Myauth()

def Myauth(request):
    if not request.session.has_key('useremail'):
        return HttpResponseRedirect('/')



def index(request):
    if not request.session.has_key('useremail'):
        return HttpResponseRedirect('/')
    return render(request,'user/index.html')
        
def logoutUser(request):
    request.session.flush()
    return HttpResponseRedirect('/')

    