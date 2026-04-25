from django.contrib import admin
from .models import Disciplina, Turma, Nota
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Nota)

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
    search_fields = ('nome', 'codigo')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'docente', 'ano_lectivo')
    list_filter = ('disciplina', 'ano_lectivo')

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'disciplina', 'valor_nota', 'data_lancamento')
    search_fields = ('estudante__username', 'disciplina__nome')
