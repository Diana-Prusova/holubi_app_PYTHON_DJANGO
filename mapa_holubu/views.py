from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django_filters.views import FilterView
from mapa_holubu import models
from .filters import HolubiFilter


# ==========================================================================
# INDEX 
# ==========================================================================
class HolubiAppIndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # data pro mapu
        holubi = models.Holubi.objects.all()
        data_pro_mapu = []
        for one in holubi:
            data_pro_mapu.append({
                'adresa': one.adresa,
                'latitude': float(one.latitude), 
                'longitude': float(one.longitude),
                'detail_url': one.get_absolute_url()
            })
        context['data'] = data_pro_mapu
        
        # Celkový počet záznamů v dtb
        total_count = models.Holubi.objects.count()
        context['holubi_count'] = total_count

        # Počet potvrzených střeleb
        potvrzene_streby_count = models.Holubi.objects.filter(potvrzena_streba=True).count()
        context['potvrzene_streby_count'] = potvrzene_streby_count
        context['potvrzene_streby_procenta'] = round((potvrzene_streby_count / total_count) * 100) if total_count > 0 else 0

        # Počet přeživších holoubků
        prezivsi_count = models.Holubi.objects.filter(prezil=True).count()
        context['prezivsi_count'] = prezivsi_count
        context['prezivsi_procenta'] = round((prezivsi_count / total_count) * 100) if total_count > 0 else 0

        return context


# ==========================================================================
# LIST 
# ==========================================================================
class HolubiListView(ListView):
    model = models.Holubi
    template_name = 'holubi_listing.html'
    

# ==========================================================================
# DETAIL 
# ==========================================================================
class HolubiDetailView(DetailView):
    model = models.Holubi
    template_name = 'holubi_detail.html'


# ==========================================================================
# FILTER 
# ==========================================================================
class HolubiFilteredListView(FilterView):
    model = models.Holubi
    template_name = 'holubi_filtered_list.html'
    context_object_name = 'holubi'
    filterset_class = HolubiFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Celkový počet záznamů v dtb
        total_count = models.Holubi.objects.count()
        context['holubi_count'] = total_count

        return context