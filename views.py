from django.shortcuts import render,redirect, get_object_or_404
from .models import RegularPizza,SicilianPizza,Subs,DinnerPlatters,Pasta,Salads,Toppings,ShoppingCart,Item,Record
from django.utils import timezone
#from tablib import Dataset
from django.contrib.auth.decorators import login_required
#from .resourse import BookResource
from django.http import HttpResponse
from django.db.models import Q
from django.http import Http404
#import requests
import json
from .forms import SignUpForm
from django.contrib.auth import login, authenticate,logout
#from .forms import SignUpForm
from django.core.exceptions import PermissionDenied
from django.db.models import F
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'pizza/signup.html', {'form': form})   

def index(request):
    regularpizza = RegularPizza.objects.all()
    
    for t in regularpizza:
        print(t.id)
    
    sicilianpizza = SicilianPizza.objects.all()
    subs = Subs.objects.all()
    dinnerPlatters = DinnerPlatters.objects.all()
    pasta = Pasta.objects.all()
    salads = Salads.objects.all()
    toppings = Toppings.objects.all()
    return render(request,'pizza/index.html',{'regularpizza' : regularpizza, 'sicilianpizza' : sicilianpizza,'subs' : subs,'dinnerplatters' : dinnerPlatters,'pasta' : pasta,'salads' : salads,'toppings' : toppings})


def add_to_cart(request,pk,label):
   
   obj, created = ShoppingCart.objects.get_or_create(customer = request.user,checked_out=False)
   if label == 1:
    product = RegularPizza.objects.get(pk=pk)

   elif label == 2:
    product = SicilianPizza.objects.get(pk=pk) 

   else:
    product = Salads.objects.get(pk=pk) 
   flag = 0 
   try:
         item= Item.objects.get( Q(shoppingCart = obj) & Q(product_name = product.name) & Q(product_price = product.price_small))
         print(item)
   except Item.DoesNotExist:
         flag  = 1
         item = Item.objects.create(shoppingCart = obj,product_name =product.name,product_price=product.price_small,product_quantity=1)
         item.save()

   if flag == 0:
         item.product_quantity = F('product_quantity') + 1
         item.save() 

   cart_item = Item.objects.filter(shoppingCart = obj)
   
   sum =0
   count = 0
   for i in cart_item:
        sum = sum + i.product_price * i.product_quantity
        count = count + 1 
   return render(request,'pizza/demo.html',{'item1':cart_item,'sum':sum,'count':count,'flag':0})

def shopcart(request):
    flag = 0
    try:
         obj= ShoppingCart.objects.get(customer =request.user,checked_out=False)
     
    except ShoppingCart.DoesNotExist:
         flag = 1
    if flag == 0:
        cart_item = Item.objects.filter(shoppingCart = obj)
        sum =0
        count = 0
        for i in cart_item:
             sum = sum + i.product_price * i.product_quantity
             count = count + 1 
        return render(request,'pizza/demo.html',{'item1':cart_item,'sum':sum,'count':count,'flag':0 })
    else:
        return render(request,'pizza/demo.html',{'item1':"Cart Empty",'flag':1})
def customise(request,pk,label):
    toppings = Toppings.objects.all()
    regularpizza = RegularPizza.objects.get(pk =pk)
    return render(request,'pizza/customise.html',{'toppings':toppings,'regularpizza':regularpizza})

def add_to_cart_customised_pizza(request,pk,label,price,name):
    obj, created = ShoppingCart.objects.get_or_create(customer =request.user,checked_out=False)
    if label == 1:
         product = RegularPizza.objects.get(pk=pk)
    #else:
         #product = SicilianPizza.objects.get(pk=pk) 

    flag = 0     
    try:
         item= Item.objects.get( Q(shoppingCart = obj) & Q(product_name = name) & Q(product_price = float(price)))
    except Item.DoesNotExist:
         flag  = 1
         item = Item.objects.create(shoppingCart = obj,product_name=name,product_price=price,product_quantity=1)
         item.save()
    if flag == 0:
         item.product_quantity = F('product_quantity') + 1
         item.save() 

    cart_item = Item.objects.filter(shoppingCart = obj)
    sum =0
    count = 0
    for i in cart_item:    
        sum = sum + i.product_price * i.product_quantity
        count = count + 1 
    return render(request,'pizza/demo.html',{'item1':cart_item,'sum':sum,'count':count,'flag':0})

def checkout(request,sum):
    delivery_charge = 20.0
    tax = 0.20*float(sum)
    total = float(sum) + delivery_charge + tax  
    return render(request,'pizza/place_order.html',{'delivery_charge':delivery_charge,'tax':tax,'sum':sum,'total':total})

def place_order(request):
    obj = ShoppingCart.objects.get(customer=request.user,checked_out=False)
    obj.date_of_checked_out = timezone.now()    
    obj.checked_out = True
    obj.save()
    record = Record.objects.create(shoppingCart=obj)
    record.save()
    return render(request,'pizza/thankyou.html',{'obj':obj})


@login_required    
def view_order(request):
      
         obj = ShoppingCart.objects.filter(checked_out=True)
         confirm_order = Record.objects.filter(order_confirm = False)
         list=[]
         for i in confirm_order:
            my_dict={}
            obj = ShoppingCart.objects.get(pk=i.shoppingCart.pk)
            print(obj)
            customer_info = User.objects.get(pk=obj.customer.pk)
            cart_item = Item.objects.filter(shoppingCart = obj)
            my_dict['customer_info'] = customer_info
            my_dict['shop_cart_info'] = obj
            my_dict['cart_item'] = cart_item
            list.append(my_dict)
            
         return render(request,'pizza/view_order.html',{'list':list}) 

def confirm_order(request,pk):
    if request.method == 'POST':
        obj = ShoppingCart.objects.get(pk=pk)
        customer_info = User.objects.get(pk=obj.customer.pk)
        
        record = Record.objects.get(shoppingCart=obj) 
        record.order_confirm = True
        record.date_of_confirm = timezone.now()
        record.save()
        
        return redirect('view_confirmed_order')  
    else:      
        return redirect('view_order')
        
def view_confirmed_order(request):

        confirm_order=Record.objects.filter(order_confirm=True)
        list=[]
        for i in confirm_order:
            my_dict={}
            obj = ShoppingCart.objects.get(pk=i.shoppingCart.pk)
            print(obj)
            customer_info = User.objects.get(pk=obj.customer.pk)
            cart_item = Item.objects.filter(shoppingCart = obj)
            my_dict['customer_info'] = customer_info
            my_dict['shop_cart_info'] = obj
            my_dict['cart_item'] = cart_item
            list.append(my_dict)
        return render(request,'pizza/confirm_order.html',{'list':list}) 
def track_order(request,pk):
        obj = ShoppingCart.objects.get(pk=pk)
        record = Record.objects.get(shoppingCart=obj)
        if record.order_confirm == True:
            flag=1
        else:
            flag=0
        return render(request,'pizza/track_order.html',{'flag':flag})    

def order_summary(request):
         confirm_order=Record.objects.filter(order_confirm=True)
         list=[]
         obj = ShoppingCart.objects.filter(customer=request.user,checked_out=True)
         for i in obj:
              my_dict={}
              confirm_order=Record.objects.get(shoppingCart=i.pk) 
              if confirm_order.order_confirm == True:
                  item = Item.objects.filter(shoppingCart=i.pk)
                  customer_info = User.objects.get(pk=i.customer.pk)
                  my_dict['customer_info']=customer_info
                  my_dict['shop_cart_info']=i
                  my_dict['cart_item']=item
                  list.append(my_dict)

          
         return render(request,'pizza/order_summary.html',{'list':list}) 
