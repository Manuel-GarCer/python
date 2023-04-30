from django.contrib import admin
from .models import Postulante, Periodo, Matricula
# Register your models here.
#admin.site.register(Postulante)

@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'tipo_documento', 'documento', 'genero']
    # search_fields = ['nombre', 'apellido', ]

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'periodo']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_postulante', 'nombre_periodo', 'ingreso', ]

    def nombre_postulante(self, obj):
        return obj.postulante.nombre
    
    def nombre_periodo(self, obj):
        return obj.periodo.periodo