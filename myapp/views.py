from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import FoodForm
from .models import Food, Order
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .middleware import auth, guest

# Create your views here.
@auth
def index(request):
    if request.method=='GET':
        foods = Food.objects.all()
        return render(request, "index.html", {'foods':foods})
    
@auth
def add_item(request):
    initData = {'name': '', 'type': 'unknown', 'price': 0.00}
    foodForm = FoodForm(initial=initData)
   
    if request.method=='POST':
        foodData = request.POST
        foodForm = FoodForm(foodData)
        if foodForm.is_valid():
            foodForm.save()
            messages.success(request, 'Item added succesfully.')
            return redirect('index')
        else:
            messages.error(request, 'Could not add the Item.')
    return render(request, "addItem.html", {'foodForm': foodForm})

@auth 
def add_item_cart(request):
    if request.method=='POST':
        
        food_id = request.POST.get('food_id')
        food = Food.objects.get(id=food_id)
        # order = Order() 
        order = Order.objects.filter(user=request.user, is_placed=False).first()
        if order:
            order.items.add(food)
        else:
            order, created = Order.objects.create(user=request.user)
            order.items.add(food)
        order.user = request.user
        order.save()
    return redirect('index')

# View Function to Login 
@guest
def user_login(request):
    initialVal = {'username': '', 'password': ''}
    loginForm = AuthenticationForm(initial=initialVal)
    if request.method=='POST':
        loginForm = AuthenticationForm(request, data=request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect('index')

    return render(request, 'login.html', {'loginForm': loginForm})

# View Function to Login 
@guest
def user_regiter(request):
    initialVal = {'username': '', 'password1':'', 'password2': ''}
    regForm = UserCreationForm(initial=initialVal)
    if request.method=='POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            user = regForm.save()
            request.session['username'] = user.username
            return redirect('login')

    return render(request, 'register.html', {'regForm': regForm})


# View Function to Logout
def user_logout(request):
    logout(request)
    return redirect('login')
        
    