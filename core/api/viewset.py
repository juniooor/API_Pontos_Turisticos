from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from core.models import PontoTuristico

from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewset(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = [TokenAuthentication]
    search_fields = ["aprovado"]

    def get_queryset(self):
        queryset = PontoTuristico.objects.all()
        if "aprovados" in self.request.query_params:
            queryset = queryset.filter(aprovado=True)
        return queryset

    def destroy(self, request, *args, **kwargs):
        pass
