from django.contrib import admin
from .models import Pessoa, Diario
# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'foto')

@admin.register(Diario)
class DiarioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'create_at')
    list_filter = ('create_at',)