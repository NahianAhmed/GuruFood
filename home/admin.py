from django.contrib import admin
from .models import BusLocation
from .models import FoodCatagory
from .models import FoodItem
from .models import Offers

# Register your models here.

admin.site.register(BusLocation)
admin.site.register(FoodCatagory)
admin.site.register(FoodItem)
admin.site.register(Offers)
