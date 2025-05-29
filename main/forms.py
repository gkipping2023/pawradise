from django.forms import ModelForm, ModelChoiceField
from .models import User, Reserves_Daily,Dogs, Reserves_Hotel
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from datetime import date
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class NewUserForm(UserCreationForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-primary border-primary'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-primary border-primary'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control text-primary border-primary','type':'tel', 'pattern':'[0-9]{4}-[0-9]{4}','placeholder':'Ej: 1234-5678'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control text-primary border-primary','type':'email'}))

    class Meta:
        model = User
        fields = ['email','nombre','apellido','telefono']

class NewDogForm(ModelForm):
    class Meta:
        model = Dogs
        fields = '__all__'
        exclude = ['is_special','propietario']
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            # Open the uploaded image
            img = Image.open(photo)
            # Convert to RGB if necessary
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            # Save to BytesIO with reduced quality
            output = BytesIO()
            img.save(output, format='JPEG', quality=70, optimize=True)
            output.seek(0)
            # Replace the uploaded file with the compressed one
            photo = InMemoryUploadedFile(
                output, 'ImageField', photo.name, 'image/jpeg',
                output.getbuffer().nbytes, None
            )
            # Check size after compression
            if photo.size > 5 * 1024 * 1024:
                raise forms.ValidationError("La foto no puede ser mayor a 5Mb.")
        return photo

class Daily_ReserveForm_admin(ModelForm):
    dog = ModelChoiceField(widget=forms.Select(attrs={'class':'form-select'}),queryset=Dogs.objects.all())
    paquete = forms.Select(attrs={'class':'form-select','name':'paquete'})
    fecha_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))

    class Meta:
        model = Reserves_Daily
        fields = '__all__'
        exclude = ['is_checked_in','check_in','check_out']

class Daily_ReserveForm_Hotel_admin(ModelForm):
    dog = ModelChoiceField(widget=forms.Select(attrs={'class':'form-select'}),queryset=Dogs.objects.all())
    fecha_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))
    fecha_out = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))

    class Meta:
        model = Reserves_Hotel
        fields = '__all__'

#RESERVE FORM DIARIO label='Selecciona tu Perro',
class Daily_ReserveForm(ModelForm):
    dog = ModelChoiceField(label='Selecciona tu Perro',widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    paquete = forms.Select(attrs={'class':'form-select','name':'paquete'})
    fecha_in = forms.DateField(label='Fecha de Ingreso',widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))

    class Meta:
        model = Reserves_Daily
        fields = '__all__'
        exclude = ['propietario','is_checked_in','check_in','check_out']
        widgets = {
            'dog': forms.Select(attrs={'class':'form-select'}),
            'fecha_in': forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}),
            'paquete': forms.Select(attrs={'class':'form-select'}),
        }   
        
    #Para que solo salgan los perros del usuario actual
    def __init__(self, user, *args, **kwargs):
        super(Daily_ReserveForm, self).__init__(*args, **kwargs)
        self.fields['dog'].queryset = Dogs.objects.filter(propietario=user)

class Daily_ReserveForm2(ModelForm):
    dog = ModelChoiceField(label='Selecciona tu Perro',widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    fecha_in = forms.DateField(label='Fecha de Ingreso',widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))

    class Meta:
        model = Reserves_Daily
        fields = '__all__'
        exclude = ['propietario','is_checked_in','paquete','check_in','check_out']
        widgets = {
            'dog': forms.Select(attrs={'class':'form-select'}),
            'fecha_in': forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'})
        }
        
    #Para que solo salgan los perros del usuario actual
    def __init__(self, user, *args, **kwargs):
        super(Daily_ReserveForm2, self).__init__(*args, **kwargs)
        self.fields['dog'].queryset = Dogs.objects.filter(propietario=user)

#RESERVE FORM HOTEL
class Hotel_ReserveForm(ModelForm):
    dog = ModelChoiceField(label='Selecciona tu Perro',widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    fecha_in = forms.DateField(label='Fecha de Ingreso',widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))
    fecha_out = forms.DateField(label='Fecha de Salida',widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkout'}))


    class Meta:
        model = Reserves_Hotel
        fields = '__all__'
        exclude = ['propietario','is_checked_in']

        
    #Para que solo salgan los perros del usuario actual
    def __init__(self, user, *args, **kwargs):
        super(Hotel_ReserveForm, self).__init__(*args, **kwargs)
        self.fields['dog'].queryset = Dogs.objects.filter(propietario=user)

class Daily_ReserveForm_Admin(ModelForm):
    dog = ModelChoiceField(widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    paquete = forms.Select(attrs={'class':'form-select','name':'pack'})
    fecha_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))

    class Meta:
        model = Reserves_Daily
        fields = '__all__'