# Generated by Django 5.0.6 on 2024-05-29 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fedrigoni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='file',
            field=models.FileField(upload_to='fedrigoni/pdfs/'),
        ),
    ]