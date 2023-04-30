# Generated by Django 4.2 on 2023-04-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('tipo_documento', models.CharField(max_length=1)),
                ('documento', models.CharField(max_length=12)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
            ],
        ),
    ]
