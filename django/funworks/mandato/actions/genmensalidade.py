from django.contrib import admin
from django.contrib import messages
from funworks.associado.models import Associado
from funworks.mensalidade.models import Mensalidade
from datetime import datetime


@admin.action(description='Gerar Mensalidades')
def gerar_mensalidades(modeladmin, request, queryset):

    associados = Associado.objects.all()

    print(len(queryset))

    if len(queryset) > 1:
        messages.error(request, 'Não e possivel gerar mensalidades de multiplos anos!')
        return True
    mandato = queryset.first()
    if not mandato.mensalidades_geradas:
        for associado in associados:
            for i in range(12):
                vencimento = datetime(queryset.first().ano, i+1, queryset.first().vencimento)
                valor = queryset.first().valor_mensalidade
                mensalidade = Mensalidade(
                    mandato=mandato,
                    pago = False,
                    associado = associado,
                    vencimento = vencimento,
                    valor = valor
                )
                mensalidade.save()
        messages.success(request, 'Mensalidades geradas para {}'.format(mandato.ano))
        mandato.mensalidades_geradas = True
        mandato.save()
    else:
        messages.info(request, 'Mensalidades ja foram geradas para {}'.format(mandato.ano))

    return True