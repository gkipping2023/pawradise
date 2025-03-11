import re
from datetime import date,datetime
from django.utils.timezone import now
# import calendar
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User,Dogs, Reserves_Daily, Reserves_Hotel
from .forms import NewUserForm, Daily_ReserveForm,Hotel_ReserveForm, Daily_ReserveForm2,NewDogForm
from .filters import Reserves_DailyFilter, DogsFilter, Reserves_HotelFilter
# from django.db.models import Sum,Count
# from django.core.mail import send_mail, EmailMultiAlternatives

# Create your views here.

def local_admin(request):
    today = date.today()
    today_reserves = Reserves_Daily.objects.filter(fecha_in__exact=today).order_by('-is_checked_in')
    total_checked_in = today_reserves.filter(is_checked_in=True).count()
    hotel_reserves = Reserves_Hotel.objects.filter(fecha_in__lte=date.today()).filter(fecha_out__gte=date.today())#Lista de Reservas
    hotel_reserves_today = Reserves_Hotel.objects.filter(fecha_in__exact=date.today()).count()
    hotel_total_checked_in = hotel_reserves.filter(is_checked_in=True).count() #Total de Reservas H checked in
    expected_today = Reserves_Daily.objects.filter(fecha_in__exact=today).count() #Total de reservasD para hoy
    total_presentes = total_checked_in + hotel_total_checked_in
    try:
        porcentaje_diario = round(total_checked_in/expected_today*100,2)
        porcentaje_hotel = round(hotel_total_checked_in/hotel_reserves_today*100,2)
        capacidad_total = round(total_presentes/70*100,2)
        x = total_checked_in + hotel_total_checked_in
        y = expected_today + hotel_reserves_today
        porcentaje_total_de_conversion = round(x/y*100,2)
    except: #BORRAR
        porcentaje_diario = 0
        porcentaje_hotel = 0
        capacidad_total = 0
        x = total_checked_in + hotel_total_checked_in
        y = expected_today + hotel_reserves_today
        porcentaje_total_de_conversion = 0
        
    #print(total_checked_in/expected_today*100,'%')

    #available_days1 = User.objects.get(id=user.id)

    
    context = {
        'porcentaje_total_de_conversion':porcentaje_total_de_conversion,
        'capacidad_total':capacidad_total,
        'porcentaje_hotel':porcentaje_hotel,
        'porcentaje_diario':porcentaje_diario,
        'total_presentes':total_presentes,
        'hotel_reserves_today':hotel_reserves_today,
        'expected_today':expected_today,
        'today_reserves':today_reserves,
        'total_checked_in':total_checked_in,
        'hotel_reserves':hotel_reserves,
        'hotel_total_checked_in':hotel_total_checked_in,
    }
    return render(request,'main/local_admin.html',context)

def historial_diario(request):

    
    users = User.objects.all()
    dogs_input = Dogs.objects.all()

    historial_Diario = Reserves_Daily.objects.all().order_by('-fecha_in')
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
    return render(request,'main/historial_admin_diario.html',context)

def historial_hotel(request):

    
    users = User.objects.all()
    dogs_input = Dogs.objects.all()

    
    historial_Hotel = Reserves_Hotel.objects.all().order_by('-fecha_in')

    filter_hotel_reserves = Reserves_HotelFilter(request.GET, queryset=historial_Hotel)
    historial_Hotel = filter_hotel_reserves.qs
    

    context = {
        'filter_hotel_reserves':filter_hotel_reserves,
        'dogs_input': dogs_input,
        'user_input' : users,
        'historial_Hotel' : historial_Hotel,
    }
    return render(request,'main/historial_admin_hotel.html',context)

#by GPT
def check_in_out_daily(request,dog_id):
    dog = Reserves_Daily.objects.get(id=dog_id)
    dueno = dog.propietario
    if request.method == "POST":
        if dueno.available_days > 0 and dog.is_checked_in is not True:
            dueno.available_days -= 1
            dog.check_in = now()
            dueno.save()
            messages.success(request, str(dog.dog) + " Checked In!")
        else:
            dog.check_out = now()
            messages.error(request, str(dog.dog) + " Checked Out!")
        dog.is_checked_in = not dog.is_checked_in
        dog.save()
    return redirect('local_admin')

def DogsFile(request):
    dogs_filter1 = DogsFilter(request.GET, queryset=Dogs.objects.all())
    dogs_filter = dogs_filter1.qs
    context = {
        'dogs_filter1' : dogs_filter1,
        'dogs_filter' : dogs_filter,
    }
    return render(request,'main/Perros.html', context)

@login_required(login_url='login')
def home(request):
    user = request.user
    rewards = user.rewards
    user_dogs = Dogs.objects.filter(propietario__exact=request.user)
    context = {
        'user_dogs':user_dogs,
    }
    return render(request,'main/home.html',context)

@login_required(login_url='login')
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

@login_required(login_url='login')    
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
    if dog.is_checked_in is not True:
        dog.is_checked_in = not dog.is_checked_in
        dog.save()
        messages.success(request, str(dog.dog) + " Checked In!")
    else:
        dog.is_checked_in = not dog.is_checked_in
        dog.save()
        messages.error(request, str(dog.dog) + " Checked Out!")
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
    return render(request,'main/register_user.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff is 1:
                return redirect('home')
            else:
                return redirect('local_admin')
        else:
            messages.error(request, 'Invalid Username OR Password')

    context = {'page' : page}
    return render(request,'main/login.html', context)

@login_required(login_url='login')
def new_dog(request):
    newdog_form = NewDogForm()
    if request.method == 'POST':
        newdog_form = NewDogForm(request.POST, request.FILES)
        if newdog_form.is_valid():
            name = newdog_form.save(commit=False)
            name.propietario = request.user
            name.nombre = name.nombre.capitalize()
            name.save()
            return redirect('home')
        else:
            messages.error(request, 'Error ocurred during Registration. Try again or contact Administrator')
    context = {
        'newdog_form':newdog_form,
    }
    return render(request,'main/register_dog.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#Borrar
def test(request):
    return render(request,'main/test.html',{})