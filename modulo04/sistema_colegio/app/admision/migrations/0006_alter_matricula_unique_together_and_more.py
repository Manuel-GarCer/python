# Generated by Django 4.2 on 2023-04-29 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0005_rename_postchoise_ingresoulante_matricula_postulante'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matricula',
            unique_together={('postulante', 'periodo')},
        ),
        migrations.AlterUniqueTogether(
            name='postulante',
            unique_together={('tipo_documento', 'documento')},
        ),
    ]
