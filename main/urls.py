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
    path('local_admin',views.local_admin,name='local_admin'),
    path('historial_admin',views.historial,name='historial_admin'),
    path('check_in_out_daily/<int:dog_id>/', views.check_in_out_daily, name='check_in_out_daily'),
    path('check_in_out_hotel/<int:dog_id>/', views.check_in_out_hotel, name='check_in_out_hotel'),
    path('register_dog',views.new_dog,name='register_dog'),
]