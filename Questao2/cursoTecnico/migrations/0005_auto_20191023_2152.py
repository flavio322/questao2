# Generated by Django 2.1.5 on 2019-10-24 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursoTecnico', '0004_delete_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursoTecnico.Professor'),
        ),
    ]
