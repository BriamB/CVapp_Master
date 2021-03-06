# Generated by Django 3.0.4 on 2020-05-02 00:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carguecv', '0025_auto_20200501_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga_cv',
            name='Periodo_fin',
            field=models.DateField(default=datetime.datetime(2020, 5, 1, 19, 5, 0, 684540)),
        ),
        migrations.AlterField(
            model_name='carga_cv',
            name='Periodo_inicio',
            field=models.DateField(default=datetime.datetime(2020, 5, 1, 19, 5, 0, 684540)),
        ),
        migrations.AlterField(
            model_name='carga_cv',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carguecv.Cargo'),
        ),
    ]
