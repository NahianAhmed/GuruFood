from django.urls import path
from .import views

urlpatterns=[

 path('',views.login),
 path('sign-up',views.signup),
 path('signup-post',views.signup_post,name="signup"),
 path('login-post',views.login_post,name="login"),
 path('forget-password',views.forgetpassword,name="forget"),
 path('forget-mail',views.forgetmail,name="forgetmail"),
 path('link-verification/<str:email>/<int:token>/',views.LinkVerification,name="verify"),
 path('update-password/',views.ResetPassword),
 path('updateingpassword/',views.UpdatePassword ,name="updatepass"),




]