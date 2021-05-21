from django.contrib import admin
from funworks.mensalidade.models import Mensalidade
from funworks.mensalidade.list_filter.mesfilter import MesFilter
from funworks.mensalidade.actions.pagarmensalidade import pagar_mensalidades
# Register your models here.
class MensalidadeAdmin(admin.ModelAdmin):
    list_filter = ['associado', 'pago', 'mandato',MesFilter]
    list_display = ['associado', 'vencimento', 'mensalidade', 'pago']
    actions = [pagar_mensalidades]
    ordering=['vencimento']

    def mensalidade(self, obj):
        return 'R$ {},00'.format(obj.valor)

    def get_queryset(self, request): 
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(MensalidadeAdmin, self).get_queryset(request) 
        if not request.user.is_superuser:
            qs = qs.filter(associado=request.user.associado)
        return qs 

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'pagar_mensalidades' in actions:
                del actions['pagar_mensalidades']
        return actions

    def get_list_filter(self, request):
        actions = super().get_list_filter(request)
        print(actions)
        if not request.user.is_superuser:
            if 'associado' in actions:
                actions.remove('associado')
        return actions

admin.site.register(Mensalidade, MensalidadeAdmin)