# Generated by Django 4.2.7 on 2024-02-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covenbiins', '0011_inmuebles_area_inmuebles_banos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmuebles',
            name='imagen',
            field=models.ImageField(blank=True, default='fotos_inmuebles/default.png', null=True, upload_to='fotos_inmuebles'),
        ),
    ]