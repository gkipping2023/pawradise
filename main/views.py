import re
# from datetime import datetime
# import calendar
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User,Dogs
from .forms import NewUserForm
# from django.db.models import Sum,Count
# from django.core.mail import send_mail, EmailMultiAlternatives

# Create your views here.
@login_required(login_url='login')
def home(request):
    user = request.user
    rewards = user.rewards
    user_dogs = Dogs.objects.filter(propietario__exact=request.user)
    context = {
        'user_dogs':user_dogs,
    }
    return render(request,'main/home.html',context)

def booking_diario(request):
    context = {

    }
    return render(request,'main/booking_diario.html',context)
    
def booking_hotel(request):
    context = {
        
    }
    return render(request,'main/booking_hotel.html',context)    

def registeruser(request):
    new_user = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.nombre = user.nombre.capitalize()
            user.apellido = user.apellido.capitalize()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error ocurred during Registration. Try again or contact Administrator')
    context = {
        'new_user': new_user,
    }
    return render(request,'main/login.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username OR Password')

    context = {'page' : page}
    return render(request,'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')