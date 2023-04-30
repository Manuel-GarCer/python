from django.db import models

# Create your models here.
class Postulante(models.Model):
    CHOISE_GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    CHOISE_TIPO = (
        ('1', 'DNI'),
        ('2', 'otro'),
    )
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=1, choices=CHOISE_TIPO) 
    documento = models.CharField(max_length=12)
    genero = models.CharField(max_length=1, choices=CHOISE_GENERO)

    class Meta:
        unique_together = (('tipo_documento', 'documento'), )
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Periodo(models.Model):
    periodo = models.CharField(max_length=6)

    class Meta:
        unique_together = (('periodo'), )

    def __str__(self):
        return f"{self.periodo}"

class Matricula(models.Model):
    CHOISE_INGRESO = (
        ('1', 'Sí'), ('0', 'No'),
    )
    postulante = models.ForeignKey(Postulante, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    ingreso = models.CharField(max_length=1, choices=CHOISE_INGRESO)

    class Meta:
        unique_together = (('postulante', 'periodo'), )
    