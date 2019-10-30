# Generated by Django 2.1.5 on 2019-10-22 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=15)),
                ('carga_horaria', models.IntegerField(verbose_name='carga horaria')),
                ('ementa', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('telefone', models.CharField(max_length=13)),
                ('valor_hora_aula', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='valor da hora aula')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(verbose_name='data de inicio')),
                ('data_termino', models.DateField(verbose_name='data de termino')),
                ('hora_inicio', models.TimeField(verbose_name='hora de inicio')),
                ('hora_termino', models.TimeField(verbose_name='hora de termino')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursoTecnico.Curso')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursoTecnico.Professor')),
            ],
        ),
    ]