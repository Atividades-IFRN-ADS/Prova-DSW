from django.contrib import admin

from .models import Atleta, Equipe, Modalidade, Tecnico


class TecnicoInline(admin.StackedInline):
    model = Tecnico
    extra = 0
    max_num = 1
    can_delete = True


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "max_atletas")
    search_fields = ("nome",)
    ordering = ("nome",)


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ("nome", "curso", "quantidade_atletas")
    inlines = (TecnicoInline,)
    ordering = ("nome",)

    @admin.display(description="Quantidade de atletas")
    def quantidade_atletas(self, obj):
        return obj.atletas.count()


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ("nome", "matricula", "equipe")
    list_filter = ("equipe", "modalidades")
    search_fields = ("nome",)
    ordering = ("nome",)
