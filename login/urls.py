from django.urls import path
from .import views

urlpatterns=[
 path('',views.login),
 path('sign-up',views.signup),
 path('signup-post',views.signup_post,name="signup"),
 path('login-post',views.login_post,name="login"),

]