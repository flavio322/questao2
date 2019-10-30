from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=15)
    carga_horaria = models.IntegerField('carga horaria')
    ementa = models.TextField()
    valor = models.DecimalField( max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=25)
    telefone = models.CharField(max_length=13)
    valor_hora_aula = models.DecimalField('valor da hora aula', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    data_inicio = models.DateField('data de inicio')
    data_termino = models.DateField('data de termino')
    hora_inicio = models.TimeField('hora de inicio')
    hora_termino = models.TimeField('hora de termino')
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE
    )




