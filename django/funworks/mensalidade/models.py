from funworks.associado.models import Associado
from django.db import models
from funworks.mandato.models import Mandato
from funworks.associado.models import Associado


# Create your models here.
class Mensalidade(models.Model):
    associado = models.ForeignKey(Associado, on_delete=models.RESTRICT)
    mandato = models.ForeignKey(Mandato, on_delete=models.RESTRICT)
    vencimento = models.DateField()
    pago = models.BooleanField()
    valor = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.vencimento)