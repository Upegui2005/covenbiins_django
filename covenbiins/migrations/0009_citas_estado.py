# Generated by Django 4.2.7 on 2024-02-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covenbiins', '0008_alter_inmuebles_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Asignada'), (2, 'Realizada'), (3, 'Cancelada')], default=1),
        ),
    ]
