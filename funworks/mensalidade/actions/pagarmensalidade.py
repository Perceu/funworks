from django.contrib import admin
from django.contrib import messages

@admin.action(description='Pagar Mensalidades')
def pagar_mensalidades(modeladmin, request, queryset):

    for mensalidade in queryset:
        mensalidade.pago = True
        mensalidade.save()

    messages.success(request, 'Mensalidades selecionadas foram pagas')
    return True