"""
URL configuration for sistema_colegio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_colegio.views  import inicio, ruta_html, ruta_saludo, ruta_saludo2, ruta_html2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('ruta_html', ruta_html),
    path('saludo/<nombre>', ruta_saludo),
    path('saludo2/<nombre>/<int:edad>', ruta_saludo2),
    path('saludo2/<nombre>/<int:edad>', ruta_saludo2),
    path('ruta_html2/', ruta_html2),

]
