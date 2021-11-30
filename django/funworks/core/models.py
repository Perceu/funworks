from django.db import models

# Create your models here.
class PagamentosFunworks(models.Model):

    idContaReceber = models.IntegerField(primary_key=True)
    emailCliente = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100)
    pagamentoConta = models.DateTimeField()
    vencimentoConta = models.DateTimeField()
    valorReceber = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'vw_PagamentosFunworks'
        managed = False