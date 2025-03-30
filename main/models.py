from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

# Create your models here.
class User(AbstractUser):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250,default='None')
    telefono = models.CharField(blank=False,max_length=25,default='9999-9999')
    email = models.EmailField(unique=True,max_length=250)
    rewards = models.IntegerField(null=False,default=0)
    available_days = models.IntegerField(null=False,default=0)
    balance = models.DecimalField(null=True,max_digits=6,decimal_places=2)
    username = models.CharField(max_length=150,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nombre

Sexo_Choices = (
    ('macho','MACHO'),
    ('hembra','HEMBRA')
)

Paquetes = (
    ('1','Medio dia - $7.49'),
    ('1','Pase Diario - $12.84'),
    ('3','Pase 3 dias - $35.31'),
    ('6','Pase 6 dias - $64.20'),
    ('12','Pase 12 dias - $117.70'),
    ('24','Pase 24 dias - $214.00')
)

class Dogs(models.Model):
    nombre = models.CharField(max_length=250)
    raza = models.CharField(max_length=250)
    sexo = models.CharField(max_length=20,choices=Sexo_Choices,default='macho')
    propietario = models.ForeignKey(User,on_delete=models.CASCADE,max_length=250,null=False)
    is_special = models.BooleanField(default=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    vacunacion = models.ImageField(null=True, blank=True, upload_to='images/vacunacion',default=None)

    def __str__(self):
        return self.nombre

class Reserves_Daily(models.Model):
    propietario = models.ForeignKey(User,on_delete=models.CASCADE,max_length=250,null=False)
    dog = models.ForeignKey(Dogs,on_delete=models.CASCADE,max_length=250,null=False)
    paquete = models.CharField(max_length=250,choices=Paquetes,default='medio')
    fecha_in = models.DateField(default='1900-01-01')
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    is_checked_in = models.BooleanField(default=False) #By GPT
    #By GPT
    def get_duration(self):
        """Returns the time difference between check-in and check-out as a timedelta object."""
        if self.check_in and self.check_out:
            return self.check_out - self.check_in
        return None
    #By GPT
    def get_duration_formatted(self):
        """Formats the duration as hours and minutes."""
        duration = self.get_duration()
        if duration:
            hours, remainder = divmod(duration.total_seconds(), 3600)
            minutes, _ = divmod(remainder, 60)
            return f"{int(hours)}h {int(minutes)}m"
        return "Not checked out"

    def __str__(self):
        return str(self.propietario)
    
class Reserves_Hotel(models.Model):
    propietario = models.ForeignKey(User,on_delete=models.CASCADE,max_length=250,null=False)
    dog = models.ForeignKey(Dogs,on_delete=models.CASCADE,max_length=250,null=False)
    fecha_in = models.DateField(default='2024-01-01')
    fecha_out = models.DateField(default='2024-01-01')
    is_checked_in = models.BooleanField(default=False)

    def __str__(self):
        return str(self.propietario)