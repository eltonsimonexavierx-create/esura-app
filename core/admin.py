from django.contrib import admin
from .models import Disciplina, Nota

# Isto regista as tuas tabelas no painel oficial do Django
admin.site.register(Disciplina)
admin.site.register(Nota)