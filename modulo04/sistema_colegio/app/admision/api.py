from .models import Postulante
from rest_framework import viewsets, permissions
from .serializers import PostulanteSerializer

class PostulanteViewSet(viewsets.ModelViewSet):
    queryset = Postulante.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostulanteSerializer