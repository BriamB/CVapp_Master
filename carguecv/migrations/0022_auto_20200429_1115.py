# Generated by Django 3.0.4 on 2020-04-29 16:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carguecv', '0021_auto_20200429_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga_cv',
            name='Periodo_fin',
            field=models.DateField(default=datetime.datetime(2020, 4, 29, 11, 15, 51, 928831)),
        ),
        migrations.AlterField(
            model_name='carga_cv',
            name='Periodo_inicio',
            field=models.DateField(default=datetime.datetime(2020, 4, 29, 11, 15, 51, 928831)),
        ),
        migrations.AlterField(
            model_name='carga_cv',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carguecv.Cargo'),
        ),
        migrations.AlterField(
            model_name='carga_cv',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
