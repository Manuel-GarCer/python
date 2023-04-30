from rest_framework import routers
from .api import PostulanteViewSet

route = routers.DefaultRouter()

route.register('api/postulante', PostulanteViewSet, 'admision')
urlpatterns = route.urls