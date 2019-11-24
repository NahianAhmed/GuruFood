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

class Offers(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    publish = models.BooleanField()
    image = models.ImageField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class SocialAccount(models.Model):

    facebook = models.TextField()
    instagram = models.TextField()
    tweeter = models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Facebook,Instragram,Tweeter"
    
class UserQuery(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    query = models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class FoodOrder(models.Model):

    username = models.CharField(max_length=255)
    useremail = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    orderDate = models.DateTimeField(auto_now_add=True)
    deliveryDate = models.CharField(max_length=255)
    foodItemName = models.TextField()
    quantity =  models.CharField(max_length=255)
    bill = models.CharField(max_length=255)
    Payablebill = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.username


