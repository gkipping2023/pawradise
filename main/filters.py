import django_filters
from django.forms import DateInput
from django_filters import DateFilter
from .models import *

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
        exclude = ['is_checked_in','fecha_in','paquete']