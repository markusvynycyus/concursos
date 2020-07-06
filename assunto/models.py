from django.db import models

# Create your models here.

class Assunto (models.Model):

    nome_assunto = models.CharField("nome assunto", max_length=50)

    def __str__(self):
        return self.nome_assunto