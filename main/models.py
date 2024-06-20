from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250,default='None')
    telefono = models.CharField(max_length=250)
    email = models.EmailField(unique=True,max_length=250)
    rewards = models.IntegerField(null=True)
    available_days = models.IntegerField(null=True)
    balance = models.DecimalField(max_digits=6,decimal_places=2)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

Sexo_Choices = (
    ('macho','MACHO'),
    ('hembra','HEMBRA')
)

Paquetes = (
    ('medio','Medio dia - $7.49'),
    ('1dia','Pase Diario - $12.84'),
    ('3dias','Pase 3 dias - $35.31'),
    ('6dias','Pase 6 dias - $64.20'),
    ('12dias','Pase 12 dias - $117.70'),
    ('24dias','Pase 24 dias - $214.00')
)

class Dogs(models.Model):
    nombre = models.CharField(max_length=250)
    raza = models.CharField(max_length=250)
    sexo = models.CharField(max_length=20,choices=Sexo_Choices,default='macho')
    propietario = models.ForeignKey(User,on_delete=models.CASCADE,max_length=250,null=False)
    is_special = models.BooleanField(default=False)
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    vacunacion = models.ImageField(null=True, blank=True, upload_to='images/vacunacion')

    def __str__(self):
        return self.nombre

class Reserves_Daily(models.Model):
    propietario = models.OneToOneField(User,on_delete=models.CASCADE,max_length=250,null=False)
    dog = models.ForeignKey(Dogs,on_delete=models.CASCADE,max_length=250,null=False)
    paquete = models.CharField(max_length=250,choices=Paquetes,default='medio')
    fecha_in = models.DateField(default='1900-01-01')

    def __str__(self):
        return str(self.propietario)