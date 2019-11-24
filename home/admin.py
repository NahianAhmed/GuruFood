from django.contrib import admin
from .models import BusLocation
from .models import FoodCatagory,FoodItem,FoodOrder
from .models import Offers,SocialAccount,UserQuery

# Register your models here.


admin.site.register(BusLocation)
admin.site.register(FoodCatagory)
admin.site.register(FoodItem)
admin.site.register(Offers)
admin.site.register(SocialAccount)
admin.site.register(UserQuery)
admin.site.register(FoodOrder)
