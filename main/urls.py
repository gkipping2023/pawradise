from django.urls import path
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.loginPage,name= 'login'),
    path('logout',views.logoutUser,name='logout'),
    path('register_user',views.registeruser,name='registeruser'),
    path('home',views.home,name='home'),
    path('hotel',views.booking_hotel,name='booking_hotel'),
    path('diario',views.booking_diario,name='booking_diario'),
    
]