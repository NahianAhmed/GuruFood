from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from home.models import FoodOrder

# Create your views here.




def Myauth(request):
    if not request.session.has_key('useremail'):
        return HttpResponseRedirect('/')



def index(request):
    if not request.session.has_key('useremail'):
        return HttpResponseRedirect('/')
    data = FoodOrder.objects.filter(useremail=request.session['useremail']);

    #print(data)
    items=0
    payable=0
    for item in data:
        items=items+1
        payable = payable+int(item.Payablebill)

    context={
        'item':items,
        'payable':payable, 
    }

    return render(request,'user/index.html',context)
        
def logoutUser(request):
    request.session.flush()
    return HttpResponseRedirect('/')

def OrderList(request):
    if not request.session.has_key('useremail'):
        return HttpResponseRedirect('/')

    data = FoodOrder.objects.filter(useremail=request.session['useremail']);
    return render(request,'user/orderlist.html',{'data':data})

def editOrder(request,id):

    data = FoodOrder.objects.filter(id=id).get();
    return render(request,'user/editOrder.html',{'data':data})

def UpdateOrder(request):
    FoodOrder.objects.filter(id=request.POST['id']).update(address=request.POST['address'],
    deliveryDate=request.POST['deliveryDate'])

    return HttpResponseRedirect('/user/order-list')

def deleteOrder(request,id):
    #print(id)
    FoodOrder.objects.filter(id=id).delete()
    return HttpResponseRedirect('/user/order-list')