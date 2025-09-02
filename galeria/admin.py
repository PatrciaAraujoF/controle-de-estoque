from django.contrib import admin
from .models import Peca, DetalhesPeca

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Exibir apenas o nome na lista

admin.site.register(DetalhesPeca)  # Registrar apenas uma vez
