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

    def __str__(self):
        return f"{self.nombre} {self.apellido}" # __unicode__ on Python 2


class Curso (models.Model):
    nombre  = models.CharField(max_length=50)
    descripcion  = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.nombre}" 


class Nota (models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota01 = models.DecimalField(max_digits=5, decimal_places=2)
    nota02 = models.DecimalField(max_digits=5, decimal_places=2)
    nota03 = models.DecimalField(max_digits=5, decimal_places=2)
    nota04 = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = (('estudiante', 'curso'), )