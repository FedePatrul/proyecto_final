# Generated by Django 5.0.6 on 2024-05-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fedrigoni', '0002_alter_pdf_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pdf',
            old_name='title',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='file',
        ),
        migrations.AddField(
            model_name='pdf',
            name='archivo',
            field=models.FileField(default=5, upload_to='pdfs/'),
            preserve_default=False,
        ),
    ]
