# Generated by Django 5.0.6 on 2024-06-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(default=45),
            preserve_default=False,
        ),
    ]
