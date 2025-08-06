from django.contrib import admin
from .models import User,Dogs,Reserves_Daily, Reserves_Hotel

# Register your models here.

class DogsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'propietario', 'is_special')

class UserAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email','available_days')

class ReservesDailyAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'dog', 'paquete', 'fecha_in', 'check_in', 'check_out', 'is_checked_in')

admin.site.register(User,UserAdmin)
admin.site.register(Dogs,DogsAdmin)
admin.site.register(Reserves_Daily,ReservesDailyAdmin)
admin.site.register(Reserves_Hotel)