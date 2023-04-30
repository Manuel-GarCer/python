from rest_framework import serializers
from .models import Postulante

class PostulanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulante
        fields = ['id', 'nombre', 'apellido', 'tipo_documento', 'documento', 'genero']