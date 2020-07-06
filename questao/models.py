from django.db import models


from banca.models import Banca
from disciplina.models import Disciplina
from instituicao.models import Instituicao
from cargo.models import Cargo
from assunto.models import Assunto

from django.utils import timezone




# Create your models here.
class Questao (models.Model):
    banca = models.ForeignKey(Banca,on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao,on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE)
    assunto = models.ForeignKey(Assunto,on_delete=models.CASCADE)


    pergunta_questao =models.TextField()

    letra_a = models.TextField()
    letra_b = models.TextField()
    letra_c = models.TextField()
    letra_d = models.TextField()
    letra_e = models.TextField()



class Comentario (models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    questao = models.ForeignKey('Questao', related_name='comentarios', on_delete=models.CASCADE)
    data_comentario = models.DateTimeField(default=timezone.now)
    comentario= models.TextField()


    def __str__(self):
        return self.comentario


    #def __str__(self):
    #    return self.user.username



