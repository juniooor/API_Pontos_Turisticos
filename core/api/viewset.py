from rest_framework import viewsets
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewset(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer