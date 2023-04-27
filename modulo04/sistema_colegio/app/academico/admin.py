from django.contrib import admin
from .models import Estudiante, Curso, Nota

# Register your models here.


#admin.site.register(Estudiante)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'genero']
    # exclude = ["genero"]
    # ordering = ["id"]
    # search_fields = ['nombre', 'apellido']

@admin.register(Curso)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_estudiante', 'nombre_curso']

    def nombre_estudiante(self, obj):
        return obj.estudiante.nombre
    
    def nombre_curso(self, obj):
        return obj.curso.nombre
