from django.db import models
from atracoes.models import Atracao

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    Atracao = models.ManyToManyField(Atracao)
    
    def __str__(self):
        return self.nome    
