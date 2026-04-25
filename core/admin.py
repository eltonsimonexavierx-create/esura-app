from django.contrib import admin
from .models import Disciplina, Turma, Nota

print("--- O FICHEIRO ADMIN FOI CARREGADO COM SUCESSO ---")

admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Nota)



