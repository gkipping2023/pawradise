import django_filters
from django.forms import DateInput
from django_filters import DateFilter
from .models import *

def get_dog_names():
    all_dogs = Dogs.objects.values_list('nombre','nombre').distinct()
    return list(all_dogs)

def get_dog_breed():
    all_breeds = Dogs.objects.values_list('raza','raza').distinct()
    return list(all_breeds)

class Reserves_DailyFilter(django_filters.FilterSet):
    Date_from = DateFilter(
        field_name='fecha_in',
        lookup_expr='gte',
        label='Desde',
        widget=DateInput(attrs={'type':'date'})
        )
    Date_to = DateFilter(
        field_name='fecha_in',
        lookup_expr='lte',
        label='Hasta',
        widget=DateInput(attrs={'type':'date'})
        )
    class Meta:
        model = Reserves_Daily
        fields = '__all__'
        exclude = ['is_checked_in','fecha_in','paquete','check_in','check_out']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs.update({
                'class': 'form-control text-center',
                'placeholder': self.filters[field].label
            })

    

class Reserves_HotelFilter(django_filters.FilterSet):
    Date_from = DateFilter(
        field_name='fecha_in',
        lookup_expr='gte',
        label='Desde',
        widget=DateInput(attrs={'type':'date'})
        )
    Date_to = DateFilter(
        field_name='fecha_in',
        lookup_expr='lte',
        label='Hasta',
        widget=DateInput(attrs={'type':'date'})
        )
    class Meta:
        model = Reserves_Hotel
        fields = '__all__'
        exclude = ['fecha_in','fecha_out','is_checked_in']

class DogsFilter(django_filters.FilterSet):
    nombre = django_filters.ChoiceFilter(
        choices = get_dog_names,
        label = 'Nombre',
        empty_label = 'Todos'
    )
    raza = django_filters.ChoiceFilter(
        choices = get_dog_breed,
        label = 'Raza',
        empty_label = 'Todas'
    )
    class Meta:
        model= Dogs
        fields = '__all__'
        exclude = ['photo','vacunacion','is_special']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.filters:
            self.filters[field].field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.filters[field].label
            })