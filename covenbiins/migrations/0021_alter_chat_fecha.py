# Generated by Django 4.2.6 on 2024-03-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covenbiins', '0020_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]