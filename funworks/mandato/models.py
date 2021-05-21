from django.db import models
from funworks.associado.models import Associado


# Create your models here.
class Mandato(models.Model):
    presidente = models.ForeignKey(Associado, on_delete=models.DO_NOTHING, related_name='presidente', null=True, blank=True, default=True)
    vice = models.ForeignKey(Associado, on_delete=models.DO_NOTHING, related_name='vice', null=True, blank=True, default=True)
    secretario = models.ForeignKey(Associado, on_delete=models.DO_NOTHING, related_name='secretario', null=True, blank=True, default=True)
    tesoureiro = models.ForeignKey(Associado, on_delete=models.DO_NOTHING, related_name='tesoureiro', null=True, blank=True, default=True)
    ano = models.IntegerField()
    valor_mensalidade = models.IntegerField(default=15, blank=True)
    vencimento = models.IntegerField(default=5, blank=True)
    acessores = models.ManyToManyField(Associado, related_name='acessores')
    mensalidades_geradas = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.ano)