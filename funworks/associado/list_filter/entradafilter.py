from django.contrib.admin import SimpleListFilter

class EntradaFilter(SimpleListFilter):
    title = 'Entrada' # or use _('country') for translated title
    parameter_name = 'mes_entrada'

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
            return queryset.filter(entrada__month = self.value())

        return queryset.filter()