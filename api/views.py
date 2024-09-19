# api/views.py
from rest_framework import generics
from mapa_holubu.models import Holubi
from .serializers import HolubiSerializer

class HolubiListAPIView(generics.ListAPIView):
    queryset = Holubi.objects.all()
    serializer_class = HolubiSerializer

