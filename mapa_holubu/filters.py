import django_filters
from django import forms
from .models import Holubi

class HolubiFilter(django_filters.FilterSet):
    datum_od = django_filters.DateFilter(
        field_name='datum', 
        lookup_expr='gte', 
        label='ZÁZNAMY OD DATA:',
        widget=forms.DateInput(attrs={'class': 'form-control',
                                      'type': 'date'})
    )
    datum_do = django_filters.DateFilter(
        field_name='datum', 
        lookup_expr='lte', 
        label='ZÁZNAMY DO DATA:',
        widget=forms.DateInput(attrs={'class': 'form-control',
                                      'type': 'date'})
    )
    adresa = django_filters.CharFilter(
        lookup_expr='icontains',
        label='ADRESA OBSAHUJE:',
        widget=forms.TextInput(attrs={'class': 'form-control', 
                                      'placeholder': 'město/ulice'})
    )
    potvrzena_streba = django_filters.ChoiceFilter(
        label='POTVRZENA STŘEBA:',
        choices=[(True, 'Ano'), (False, 'Ne')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    prezil = django_filters.ChoiceFilter(
        label='PŘEŽIL:',
        choices=[(True, 'Ano'), (False, 'Ne')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Holubi
        fields = ['datum_od', 'datum_do', 'adresa', 'potvrzena_streba', 'prezil']
