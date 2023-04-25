from rest_framework import routers
from .api import EstudianteViewSet

route = routers.DefaultRouter()

route.register('api/estudiante', EstudianteViewSet, 'academico')
urlpatterns = route.urls