# Generated by Django 2.0.1 on 2018-12-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0020_merge_20181202_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planmedidas',
            name='plan_principal',
        ),
        migrations.RemoveField(
            model_name='planobjetivos',
            name='plan_principal',
        ),
        migrations.AddField(
            model_name='plan',
            name='medidas',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='plan',
            name='objetivo_especifico',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.DeleteModel(
            name='PlanMedidas',
        ),
        migrations.DeleteModel(
            name='PlanObjetivos',
        ),
    ]
