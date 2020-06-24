from django.db import models

# Create your models here.
class Banca(models.Model):
    nome_banca = models.CharField("nome banca",max_length=100)
    sigla_banca = models.CharField("sigla banca",max_length=50)

    def __str__(self):
        return '%s - %s' %(self.sigla_banca,self.nome_banca)