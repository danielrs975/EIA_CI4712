# Generated by Django 2.1.2 on 2018-12-04 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eia_app', '0004_auto_20181118_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecomendacionProyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendaciones', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eia_app.DatosProyecto')),
            ],
        ),
    ]
