from django.db import models
from django.contrib.auth.models import User

# 1. Tabela de Disciplinas
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

# 2. Tabela de Notas (Liga o Aluno à Disciplina)
class Nota(models.Model):
    estudante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    valor_nota = models.DecimalField(max_digits=4, decimal_places=2)
    data_lancamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudante.username} - {self.disciplina.nome}: {self.valor_nota}"

