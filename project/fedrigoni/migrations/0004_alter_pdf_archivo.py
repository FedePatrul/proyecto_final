# Generated by Django 5.0.6 on 2024-05-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fedrigoni', '0003_rename_title_pdf_nombre_remove_pdf_file_pdf_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='archivo',
            field=models.FileField(upload_to='fedrigoni/pdfs/'),
        ),
    ]
