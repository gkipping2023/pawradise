from django.contrib import admin
from .models import User,Dogs,Reserves_Daily, Reserves_Hotel

# Register your models here.
admin.site.register(User)
admin.site.register(Dogs)
admin.site.register(Reserves_Daily)
admin.site.register(Reserves_Hotel)