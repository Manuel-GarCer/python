# Generated by Django 4.2 on 2023-04-29 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0004_matricula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='postCHOISE_INGRESOulante',
            new_name='postulante',
        ),
    ]
