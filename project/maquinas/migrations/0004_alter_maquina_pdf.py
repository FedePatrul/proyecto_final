# Generated by Django 5.0.6 on 2024-05-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maquinas', '0003_maquina_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='pdf',
            field=models.CharField(max_length=300),
        ),
    ]
