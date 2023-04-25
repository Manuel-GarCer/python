from django.db import models

# Create your models here.
class Estudiante (models.Model):
    CHOISE_GENERO = (    # solo 2 opciones
        ('M', 'Masculino'),
        ('F', 'Femenino'), 

    )
    nombre  = models.CharField(max_length=50) 
    apellido  = models.CharField(max_length=50) 
    genero  = models.CharField(max_length=1, choices=CHOISE_GENERO) 