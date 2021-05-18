from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Associado(models.Model):
    PAI = 'P'
    MAE = 'M'
    SEM_FILHOS = 'SF'
    FILHOS = [
        (SEM_FILHOS, 'Sem Filhos'),
        (PAI, 'Pai'),
        (MAE, 'Mãe')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nascimento = models.DateField()
    entrada = models.DateField()
    saida = models.DateField(blank=True, default=None, null=True)
    endereco = models.TextField(blank=True, default=None)
    orientacao_alimentar = models.CharField(
        max_length=100,
        blank=True, default=None
    )
    telefone = models.CharField(
        max_length=20,
        blank=True, default=None, null=True
    )
    whatsapp = models.CharField(
        max_length=20,
        blank=True, default=None, null=True
    )
    alergias_intolerancia = models.TextField(blank=True, default=None)
    obs_gerais = models.TextField(blank=True, default=None)
    filhos = models.CharField(
        max_length=2,
        choices=FILHOS,
        default=SEM_FILHOS,
    )

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)