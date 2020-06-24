from django.db import models

# Create your models here.
class Disciplina(models.Model):
    nome_disciplina = models.CharField("nome disciplina",max_length=100)

    def __str__(self):
        return self.nome_disciplina