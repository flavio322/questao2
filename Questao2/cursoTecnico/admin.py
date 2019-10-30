from datetime import *
from django.contrib import admin
from  .models import  *
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display =("nome","carga_horaria","ementa","valor")

class TurmaInline(admin.TabularInline):
    #list_display =("data_inicio","data_termino","hora_inicio","hora_termino")
    model = Turma

class ProfessorAdmin(admin.ModelAdmin):
    list_display =("nome","telefone","valor_hora_aula")
    inlines = [
        TurmaInline
    ]

admin.site.register(Curso,CursoAdmin)
admin.site.register(Professor,ProfessorAdmin)
#admin.site.register(Turma)

