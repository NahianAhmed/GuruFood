from django.urls import path
from .import views

urlpatterns=[
 path('',views.home),
 path('',views.home,name='home'),
 path('contact-with-us',views.about,name='about'),
 path('food-item-by-id/<int:id>',views.FilterFood),


]