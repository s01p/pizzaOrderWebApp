from django.conf import settings
from django.db import models
from django.utils import timezone


class RegularPizza(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small = models.FloatField()
    large = models.FloatField()
    price_small = models.FloatField()
    price_large = models.FloatField()
    topping = models.ManyToManyField('Toppings')


class SicilianPizza(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small = models.FloatField()
    large = models.FloatField()
    price_small = models.FloatField()
    price_large = models.FloatField()


class Subs(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small = models.FloatField()
    large = models.FloatField()
    price_small = models.FloatField()
    price_large = models.FloatField()   


class DinnerPlatters(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small = models.FloatField()
    large = models.FloatField()
    price_small = models.FloatField()
    price_large = models.FloatField()  


class Pasta(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small = models.FloatField()
    large = models.FloatField()
    price_small = models.FloatField()
    price_large = models.FloatField() 


class Salads(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small = models.FloatField()
    large = models.FloatField()
    price_small = models.FloatField()
    price_large = models.FloatField()       


class Toppings(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    small = models.FloatField()
    large = models.FloatField()
    price_small = models.FloatField()
    price_large = models.FloatField()  

    
class ShoppingCart(models.Model):
          
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default = False)
    date_of_checked_out = models.DateTimeField(blank=True, null=True)

class Item(models.Model):
    shoppingCart = models.ForeignKey('pizza.ShoppingCart',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    
class Record(models.Model):
    shoppingCart = models.ForeignKey('pizza.ShoppingCart',on_delete=models.CASCADE)
    order_confirm = models.BooleanField(default = False)
    date_of_confirm = models.DateTimeField(blank=True, null=True)






