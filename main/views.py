import re
from datetime import date,datetime
# import calendar
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User,Dogs, Reserves_Daily, Reserves_Hotel
from .forms import NewUserForm, Daily_ReserveForm,Hotel_ReserveForm, Daily_ReserveForm2
from .filters import Reserves_DailyFilter
# from django.db.models import Sum,Count
# from django.core.mail import send_mail, EmailMultiAlternatives

# Create your views here.

def local_admin(request):
    today = date.today()
    today_reserves = Reserves_Daily.objects.all()#filter(fecha_in__gte=today)
    total_checked_in = today_reserves.filter(is_checked_in=True).count()
    hotel_reserves = Reserves_Hotel.objects.filter(fecha_in__lte=date.today()).filter(fecha_out__gte=date.today())
    hotel_total_checked_in = hotel_reserves.filter(is_checked_in=True).count()

    


    #available_days1 = User.objects.get(id=user.id)

    
    context = {
        'today_reserves':today_reserves,
        'total_checked_in':total_checked_in,
        'hotel_reserves':hotel_reserves,
        'hotel_total_checked_in':hotel_total_checked_in,
    }
    return render(request,'main/local_admin.html',context)

def historial(request):

    
    users = User.objects.all()
    dogs_input = Dogs.objects.all()

    historial_Diario = Reserves_Daily.objects.all()
    historial_Hotel = Reserves_Hotel.objects.all()

    filter_today_reserves = Reserves_DailyFilter(request.GET, queryset=historial_Diario)
    historial_Diario = filter_today_reserves.qs

    context = {
        'filter_today_reserves':filter_today_reserves,
        'dogs_input': dogs_input,
        'user_input' : users,
        'historial_Hotel' : historial_Hotel,
        'historial_Diario' : historial_Diario,
    }
    return render(request,'main/historial_admin.html',context)

#by GPT
def check_in_out_daily(request,dog_id):
    dog = Reserves_Daily.objects.get(id=dog_id)
    dueno = dog.propietario
    if dueno.available_days > 0 and dog.is_checked_in is not True:
        dueno.available_days -= 1
        dueno.save()
        messages.success(request, str(dog.dog) + " Checked In")
    else:
        messages.error(request, str(dog.dog) + " Checked Out")
    dog.is_checked_in = not dog.is_checked_in
    dog.save()
    return redirect('local_admin')

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
    paquete_input = request.POST.get('paquete')
    form2 = Daily_ReserveForm2(request.user)
    form = Daily_ReserveForm(request.user)
    user = request.user
    user_dogs = Dogs.objects.filter(propietario__exact=request.user)
    #available_days1 = User.objects.get(id=user.id)

    if request.method == 'POST' and request.user.available_days <= 0 :
        form = Daily_ReserveForm(request.user,request.POST)
        if form.is_valid():
            propietario = form.save(commit=False)
            propietario.propietario = request.user
            propietario.save()
            request.user.available_days = int(paquete_input)
            request.user.save()
            print(request.user.available_days)
            messages.success(request,'Entry recorded Successfully!')
            return redirect('home')
    elif request.method == 'POST' and request.user.available_days > 0:
        form2 = Daily_ReserveForm2(request.user,request.POST)
        if form2.is_valid():
            propietario = form2.save(commit=False)
            propietario.propietario = request.user
            propietario.save()
            request.user.available_days = request.user.available_days
            print(request.user.available_days)
            request.user.save()
            messages.success(request,'Entry recorded Successfully!')
            return redirect('home')
        # is valid cuando no tiene available days, pero aun no es valid para no avail days.
    context = {
        'form2':form2,
        'form': form,
        'user':user,
        'user_dogs':user_dogs,
    }
    return render(request,'main/booking_diario.html',context)
    
def booking_hotel(request):
    form_h = Hotel_ReserveForm(request.user)
    user = request.user
    user_dogs = Dogs.objects.filter(propietario__exact=request.user)

    if request.method == 'POST':
        form_h = Hotel_ReserveForm(request.user,request.POST)
        if form_h.is_valid():
            propietario = form_h.save(commit=False)
            propietario.propietario = request.user
            propietario.save()
            messages.success(request,'Entry recorded Successfully!')
            return redirect('home') 
    context = {
        'form_h': form_h,
        'user':user,
        'user_dogs':user_dogs,
    }
    return render(request,'main/booking_hotel.html',context)

def check_in_out_hotel(request,dog_id):
    dog = Reserves_Hotel.objects.get(id=dog_id)
    dog.is_checked_in = not dog.is_checked_in
    dog.save()
    return redirect('local_admin')    

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