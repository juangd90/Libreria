# Generated by Django 3.2.5 on 2021-09-03 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_servicio_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='venta',
            name='ganancia',
            field=models.FloatField(default=0),
        ),
    ]