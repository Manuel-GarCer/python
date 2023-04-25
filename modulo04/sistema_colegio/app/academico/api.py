from .models import Estudiante
from rest_framework import viewsets, permissions
from .serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EstudianteSerializer