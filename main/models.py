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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

Sexo_Choices = (
    ('macho','MACHO'),
    ('hembra','HEMBRA')
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