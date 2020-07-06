from django.db import models

# Create your models here.
class Instituicao (models.Model):
    nome_instituicao = models.CharField("nome_instituiçao",max_length=50)

    def __str__(self):
        return self.nome_instituicao