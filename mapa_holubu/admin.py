from django.contrib import admin
from mapa_holubu import models

from django.contrib import admin
from .models import Holubi

@admin.register(Holubi)
class HolubiAdmin(admin.ModelAdmin):
    list_display = ('id', 'jmeno', 'datum', 'latitude', 'longitude', 'adresa', 'popis')
    search_fields = ('id', 'jmeno', 'adresa', 'popis')
    list_filter = ('datum',)

