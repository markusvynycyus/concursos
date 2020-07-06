from django.db import models

# Create your models here.

class AreaFormacao(models.Model):

    nome_area = models.CharField("Area de Formação",max_length=50)
