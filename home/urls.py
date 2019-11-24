from django.urls import path
from .import views

urlpatterns=[
 path('',views.home),
 path('',views.home,name='home'),
 path('contact-with-us',views.about,name='about'),
 path('query',views.Query,name='query'),
 path('food-item-by-id/<int:id>',views.FilterFood),
 path('custom-lunch-menu/',views.makelunch),
 path('food-order/',views.foodorder),


]