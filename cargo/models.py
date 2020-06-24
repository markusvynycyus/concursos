from django.db import models

class Cargo(models.Model):
    nome_cargo = models.CharField("nome cargo",max_length=100)

    def __str__(self):
        return self.nome_cargo