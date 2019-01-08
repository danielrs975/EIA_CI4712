# Generated by Django 2.1.2 on 2018-11-26 01:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='IndicadorDeCumplimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Medida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomenclatura', models.CharField(max_length=10, unique=True, verbose_name='Nomenclatura')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('tipo', models.IntegerField(choices=[(0, 'Correctiva')], verbose_name='Tipo')),
                ('medio', models.IntegerField(choices=[(0, 'Físico'), (1, 'Biológico'), (2, 'Socio-Cultural')], verbose_name='Medio')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('marco_juridico', models.TextField(verbose_name='Marco Jurídico')),
                ('area', models.TextField(verbose_name='Área')),
                ('nombre_responsable', models.CharField(max_length=100, verbose_name='Nombre del Responsable')),
                ('apellido_responsable', models.CharField(max_length=100, verbose_name='Apellido del Responsable')),
                ('nivel_academico_responsable', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Nivel Académico del Responsable')),
                ('ci_responsable', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('/^[V|E|J|P][0-9]{5,9}$/', 'Cédula incorrecta', 'invalid')], verbose_name='Cédula del Responsable')),
            ],
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripción')),
                ('medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objetivos', to='medidas.Medida')),
            ],
        ),
        migrations.AddField(
            model_name='indicadordecumplimiento',
            name='medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicadoresdecumplimientos', to='medidas.Medida'),
        ),
        migrations.AddField(
            model_name='impacto',
            name='medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impactos', to='medidas.Medida'),
        ),
    ]
