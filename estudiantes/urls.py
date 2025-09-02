from django.urls import path
from . import views

app_name = "estudiantes"

urlpatterns = [
    path("", views.home, name="home"),

    # Programas
    path("programas/", views.lista_programas, name="lista_programas"),
    path("programas/<int:pk>/", views.detalle_programa, name="detalle_programa"),

    # Cursos
    path("cursos/", views.lista_cursos, name="lista_cursos"),
    path("cursos/<int:pk>/", views.detalle_curso, name="detalle_curso"),

    # Estudiantes
    path("estudiantes/", views.lista_estudiantes, name="lista_estudiantes"),
    path("estudiantes/<int:pk>/", views.detalle_estudiante, name="detalle_estudiante"),

    # Inscripciones
    path("inscripciones/", views.lista_inscripciones, name="lista_inscripciones"),
    path("inscripciones/<int:pk>/", views.detalle_inscripcion, name="detalle_inscripcion"),
]
