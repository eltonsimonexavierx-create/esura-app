from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    docente = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})

    class Meta:
        verbose_name_plural = "Turmas"

    def __str__(self):
        return f"{self.nome} - {self.disciplina.nome}"

class Nota(models.Model):
    estudante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notas_aluno")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name_plural = "Notas"



