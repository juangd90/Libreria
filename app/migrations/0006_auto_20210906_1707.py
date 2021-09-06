# Generated by Django 3.2.5 on 2021-09-06 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210906_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventaproducto',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ventaproducto',
            name='fecha_venta',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
