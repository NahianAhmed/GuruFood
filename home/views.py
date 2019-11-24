from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import BusLocation
from .models import FoodCatagory
from .models import FoodItem,FoodOrder
from .models import Offers,SocialAccount,UserQuery
import json
from django.core import serializers
from django.contrib import messages
from django.db.models import Sum

# Create your views here.

def home(request):
    location = BusLocation.objects.all()
    FoodCatagorys = FoodCatagory.objects.filter(publish=1)
    Offer = Offers.objects.filter(publish=1)
    account = SocialAccount.objects.all().first()
    context={
        'location': location,
        'FoodCatagory':FoodCatagorys,
        'offer': Offer,
        'account':account
    }
    return render(request,'home/index.html',context)
def about(request):
    return render(request,'home/about.html')

def FilterFood(request,id):
    data = FoodItem.objects.filter(catagory_id=id)

    html =""

    for item in data:
        tag='<div class="col-md-6 col-6 single-product-area"> <div class="row single-product"> <div class="col-md-3">'
        image = '<img src="'+ item.image.url +' " alt="" width="100%">'
        title = '</div><div class="col-md-9 "><div class="sc_blogger_item_header entry-header"><h6 class="header">'+ item.title +'</h6>'
        price = '<h6 class="header"> '+ item.price +' tk </h6> </div> </div> </div> </div>'
        html+=tag+image+title+price

    return HttpResponse(html)

def Query(request):
    data = UserQuery()
    data.name=request.POST['name']
    data.email=request.POST['email']
    data.query=request.POST['query']
    data.save()
    messages.success(request,"Thanks for your Query")
    return HttpResponseRedirect('/contact-with-us')

def makelunch(request):
    data = FoodItem.objects.all()
    return render(request,'home/lunchmenu.html',{'food':data})


def foodorder(request):
    #food array 
    food = request.POST['food']
    foodList = food.split(',')
    #print(food)
    foodItemName=[]
    tottalPrice = FoodItem.objects.filter(id__in=foodList).aggregate(Sum('price'))
    foodName=list(FoodItem.objects.filter(id__in=foodList).values('title'))
    for foods in foodName:
        #print(foods['title'])
        foodItemName.append(foods['title'])

    print(foodItemName) 
    data = FoodOrder()
    data.username=request.session['username']
    data.useremail=request.session['useremail']
    data.address=request.POST['address']
    data.deliveryDate=request.POST['date']
    data.foodItemName =",".join(foodItemName) 
    data.quantity= request.POST['quantity']
    data.bill= tottalPrice['price__sum']
    data.Payablebill= int(tottalPrice['price__sum'])*int(request.POST['quantity'])
    data.save()
    #print(tottalPrice['price__sum'])

    return HttpResponse(foodItemName)