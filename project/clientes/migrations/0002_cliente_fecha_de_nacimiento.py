# Generated by Django 5.0.6 on 2024-06-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
    ]
