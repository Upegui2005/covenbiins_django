# Generated by Django 4.2.6 on 2024-02-26 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covenbiins', '0016_lista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id_Informe', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreInforme', models.CharField(max_length=50)),
                ('inmueble', models.CharField(max_length=50)),
                ('fechaInforme', models.DateField()),
                ('descripcion', models.CharField(max_length=3500)),
                ('citas', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='covenbiins.citas')),
            ],
        ),
    ]