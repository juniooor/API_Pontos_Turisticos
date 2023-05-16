from rest_framework.viewsets import ModelViewSet
from .serializers import AvaliacoeSerializer
from avaliacoes.models import Avaliacao


class AvaliacoesViewset(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacoeSerializer
