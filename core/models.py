from django.db import models

from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao, related_name='pontos_turisticos')
    comentarios = models.ManyToManyField(Comentario, related_name='pontos_turisticos')
    avaliacao = models.ManyToManyField(Avaliacao)
    
    def __str__(self):
        return self.nome    
