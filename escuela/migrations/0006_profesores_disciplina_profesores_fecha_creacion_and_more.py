# Generated by Django 4.0.3 on 2022-04-13 03:34

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0005_profesores_delete_nivel_inicial_delete_primaria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesores',
            name='disciplina',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profesores',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profesores',
            name='tarjeta_presentacion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
