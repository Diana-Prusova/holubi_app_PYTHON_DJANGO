from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from mapa_holubu import models

# ==========================================================================
# INDEX 
# ==========================================================================
class HolubiAppIndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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