# Generated by Django 4.2 on 2023-04-29 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admision', '0002_alter_postulante_tipo_documento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=6)),
            ],
        ),
    ]