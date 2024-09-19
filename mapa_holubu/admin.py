from django.contrib import admin
from .models import Holubi, ImgHolubu

class ImgHolubuInline(admin.TabularInline):  # Nebo admin.StackedInline
    model = ImgHolubu
    extra = 1
    fields = ('image', 'description')

@admin.register(Holubi)
class HolubiAdmin(admin.ModelAdmin):
    list_display = ('id', 'jmeno', 'datum', 'latitude', 'longitude', 'adresa', 'popis')
    search_fields = ('id', 'jmeno', 'adresa', 'popis')
    list_filter = ('datum',)
    inlines = [ImgHolubuInline]

@admin.register(ImgHolubu)
class ImgHolubuAdmin(admin.ModelAdmin):
    list_display = ('id', 'holub', 'image', 'description')
    search_fields = ('description',)
    list_filter = ('holub',)
