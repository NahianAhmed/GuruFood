from django.db import models

# Create your models here.
class BusLocation(models.Model):
    title = models.CharField(max_length=255)
    location = models.TextField()
    time = models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FoodCatagory(models.Model):
    title = models.CharField(max_length=255)
    publish = models.BooleanField()
    image = models.ImageField(default='caffee.png')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class FoodItem(models.Model):
    title = models.CharField(max_length=255)
    publish = models.BooleanField()
    date=models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=6)
    image = models.ImageField()
    catagory = models.ForeignKey(FoodCatagory,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


