from rest_framework.viewsets import ModelViewSet

from avaliacoes.models import Avaliacao

from .serializers import AvaliacoeSerializer


class AvaliacaoViewset(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoeSerializer
