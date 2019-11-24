from django.urls import path
from .import views

urlpatterns=[
 path('',views.index),
 path('order-list',views.OrderList),
 path('edit-order/<int:id>',views.editOrder),
 path('delete-order/<int:id>',views.deleteOrder),
 path('update-order/',views.UpdateOrder,name="updateorder"),
 path('logout',views.logoutUser,name='logout'),

]