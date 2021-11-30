from django.contrib import admin
from funworks.mandato.models import Mandato
from funworks.mandato.actions.genmensalidade import gerar_mensalidades

# Register your models here.
class MandatoAdmin(admin.ModelAdmin):
    list_display = ['ano', 'valor_mensalidade', 'vencimento', 'mensalidades_geradas']
    actions = [gerar_mensalidades]

admin.site.register(Mandato, MandatoAdmin)