# Generated by Django 2.1.2 on 2018-11-18 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eia_app', '0003_auto_20181118_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcionproyecto',
            name='proyecto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto'),
        ),
    ]
