# Generated by Django 2.1.2 on 2018-12-29 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eia_app', '0011_auto_20181229_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosproyecto',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
