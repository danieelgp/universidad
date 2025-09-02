from django.contrib import admin
from .models import Programa, Curso, Estudiante, Inscripcion

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'duracion', 'descripcion')  
    search_fields = ('nombre', 'codigo')  

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'programa', 'creditos') 
    list_filter = ('programa',)
    search_fields = ('nombre',)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'programa')  
    list_filter = ('programa',)
    search_fields = ('nombre', 'apellido', 'email')


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha')  
    list_filter = ('curso', 'estudiante')
    search_fields = ('estudiante__nombre', 'estudiante__apellido', 'curso__nombre')
    autocomplete_fields = ('estudiante', 'curso')

