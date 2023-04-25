from django.contrib import admin
from .models import Estudiante

# Register your models here.


#admin.site.register(Estudiante)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'genero']
    # exclude = ["genero"]
    # ordering = ["id"]
    # search_fields = ['nombre', 'apellido']