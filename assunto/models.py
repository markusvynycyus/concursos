from django.db import models
from disciplina.models import Disciplina

# Create your models here.
class Assunto(models.Model):
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE)
    nome_assunto = models.CharField("nome assunto",max_length=100)

    def __str__(self):
        return '%s -- > %s' %(self.disciplina,self.nome_assunto)
