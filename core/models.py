from django.db import models
from django.contrib.auth.models import User

# 1. Tabela de Disciplinas
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")

    def __str__(self):
        return self.nome

# 2. Tabela de Turmas (Liga Disciplina ao Professor)
class Turma(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da Turma (Ex: Eng12)")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    docente = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Professor"}, verbose_name="Professor Responsável")
    ano_lectivo = models.IntegerField(default=2026)

    def __str__(self):
        return f"{self.nome} - {self.disciplina.nome}"

# 3. Tabela de Notas (Liga Aluno à Disciplina)
class Nota(models.Model):
    estudante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': False}, related_name="notas_aluno")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    valor_nota = models.DecimalField(max_digits=4, decimal_places=2)
    data_lancamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudante.username} - {self.disciplina.nome}: {self.valor_nota}"


