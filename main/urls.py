from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.loginPage,name= 'login'),
    path('logout',views.logoutUser,name='logout'),
    path('register_user',views.registeruser,name='registeruser'),
    path('home',views.home,name='home'),
    path('hotel',views.booking_hotel,name='booking_hotel'),
    path('diario',views.booking_diario,name='booking_diario'),
    path('local_admin',views.local_admin,name='local_admin'),
    path('historial_admin_diario',views.historial_diario,name='historial_admin_diario'),
    path('historial_admin_hotel',views.historial_hotel,name='historial_admin_hotel'),
    path('check_in_out_daily/<int:dog_id>/', views.check_in_out_daily, name='check_in_out_daily'),
    path('check_in_out_hotel/<int:dog_id>/', views.check_in_out_hotel, name='check_in_out_hotel'),
    path('register_dog',views.new_dog,name='register_dog'),
    path('dogs_file',views.DogsFile,name='dogs_file'),
    path('admin_new_reserve',views.admin_new_dog,name='admin_new_reserve'),
    path('admin_new_reserve_hotel',views.admin_new_dog_hotel,name='admin_new_reserve_hotel'),
    path('update_dog_photo/<int:dog_id>/', views.update_dog_photo, name='update_dog_photo'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='main/password_reset_view.html'),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_confirm_view.html'),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'),name='password_reset_complete'),
]