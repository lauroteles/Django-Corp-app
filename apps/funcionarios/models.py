from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamentos



class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)


    def __str__(self):
        return f"{self.nome}"


