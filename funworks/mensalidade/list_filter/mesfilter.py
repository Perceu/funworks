from django.contrib.admin import SimpleListFilter

class MesFilter(SimpleListFilter):
    title = 'Vencimento' # or use _('country') for translated title
    parameter_name = 'mes_vencimento'

    def lookups(self, request, model_admin):
        return [
            (1, 'Janeiro'),
            (2, 'Fevereiro'),
            (3, 'Março'),
            (4, 'Abril'),
            (5, 'Maio'),
            (6, 'Junho'),
            (7, 'Julho'),
            (8, 'Agosto'),
            (9, 'Setembro'),
            (10, 'Outubro'),
            (11, 'Novembro'),
            (12, 'Dezembro'),
        ]

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(vencimento__month = self.value())

        return queryset.filter()