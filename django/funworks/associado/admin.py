from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from funworks.associado.models import Associado
from funworks.associado.list_filter.entradafilter import EntradaFilter
from funworks.associado.list_filter.nascimentofilter import NascimentoFilter


class AssociadoAdmin(admin.ModelAdmin): 
    search_fields = [
        'user__first_name',
        'user__last_name'
    ]
    list_display = [
        'nome', 'filhos', 'nascimento', 'entrada', 'saida'
    ]

    list_filter = ['filhos', NascimentoFilter, EntradaFilter]

    readonly_fields = ['user', 'entrada', 'nascimento', 'saida']

    def get_readonly_fields(self, request, obj=None):

        if request.user.is_superuser:
            return ['user', 'nome', 'filhos', 'nascimento', 'entrada', 'saida', 'endereco', 'orientacao_alimentar', 'alergias_intolerancia', 'obs_gerais', 'telefone', 'whatsapp']

        return self.readonly_fields

    def nome(self, obj):
        return str(obj)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request): 
        # For Django < 1.6, override queryset instead of get_queryset
        qs = super(AssociadoAdmin, self).get_queryset(request) 
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs 


class AssociadoInline(admin.StackedInline):
    model = Associado
    can_delete = False
    verbose_name_plural = 'Associados'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (AssociadoInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Associado, AssociadoAdmin)
