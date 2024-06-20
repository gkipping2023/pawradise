from django.forms import ModelForm, ModelChoiceField
from .models import User, Reserves_Daily,Dogs
from django.contrib.auth.forms import UserCreationForm
from django import forms
from datetime import date

class NewUserForm(UserCreationForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['email','nombre','apellido','telefono']

class Daily_ReserveForm(ModelForm):
    dog = ModelChoiceField(widget=forms.Select(attrs={'class':'form-select'}),queryset=None)
    paquete = forms.Select(attrs={'class':'form-select'})
    fecha_in = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))

    class Meta:
        model = Reserves_Daily
        fields = '__all__'
        exclude = ['propietario']

    def __init__(self, user, *args, **kwargs):
        super(Daily_ReserveForm, self).__init__(*args, **kwargs)
        self.fields['dog'].queryset = Dogs.objects.filter(propietario=user)