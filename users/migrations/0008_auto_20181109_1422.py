# Generated by Django 2.1.2 on 2018-11-09 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20181109_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='doc_identidad',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[VEF]-\\d+$', 'Formato de documento de identidad inválido. Los números deben estar precedidos por V- o E-.')], verbose_name='Documento de Identidad'),
        ),
    ]
