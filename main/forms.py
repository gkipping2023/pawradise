from django.forms import ModelForm, ModelChoiceField
from .models import User, Reserves_Daily,Dogs, Reserves_Hotel
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from datetime import date

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

#RESERVE FORM DIARIO
class Daily_ReserveForm(ModelForm):
    dog = ModelChoiceField(widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    paquete = forms.Select(attrs={'class':'form-select','name':'paquete'})
    fecha_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))

    class Meta:
        model = Reserves_Daily
        fields = '__all__'
        exclude = ['propietario','is_checked_in','check_in','check_out']
        
    #Para que solo salgan los perros del usuario actual
    def __init__(self, user, *args, **kwargs):
        super(Daily_ReserveForm, self).__init__(*args, **kwargs)
        self.fields['dog'].queryset = Dogs.objects.filter(propietario=user)

class Daily_ReserveForm2(ModelForm):
    dog = ModelChoiceField(widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    fecha_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))

    class Meta:
        model = Reserves_Daily
        fields = '__all__'
        exclude = ['propietario','is_checked_in','paquete','check_in','check_out']
        
    #Para que solo salgan los perros del usuario actual
    def __init__(self, user, *args, **kwargs):
        super(Daily_ReserveForm2, self).__init__(*args, **kwargs)
        self.fields['dog'].queryset = Dogs.objects.filter(propietario=user)

#RESERVE FORM HOTEL
class Hotel_ReserveForm(ModelForm):
    dog = ModelChoiceField(widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    fecha_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkin'}))
    fecha_out = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control','id':'checkout'}))


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