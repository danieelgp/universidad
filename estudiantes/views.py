from django.shortcuts import render, get_object_or_404
from .models import Programa, Curso, Estudiante, Inscripcion

def home(request):
    return render(request, "estudiantes/home.html", {})

# PROGRAMAS
def lista_programas(request):
    programas = Programa.objects.all().order_by("nombre")
    return render(request, "estudiantes/lista_programas.html", {"programas": programas})

def detalle_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    cursos = programa.cursos.all().order_by("nombre")  # related_name="cursos" en Curso
    return render(request, "estudiantes/detalle_programa.html", {"programa": programa, "cursos": cursos})

# CURSOS
def lista_cursos(request):
    cursos = Curso.objects.select_related("programa").order_by("nombre")
    return render(request, "estudiantes/lista_cursos.html", {"cursos": cursos})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso.objects.select_related("programa"), pk=pk)
    inscripciones = curso.inscripciones.select_related("estudiante").all()
    return render(request, "estudiantes/detalle_curso.html", {"curso": curso, "inscripciones": inscripciones})

# ESTUDIANTES
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.select_related("programa").order_by("nombre")
    return render(request, "estudiantes/lista_estudiantes.html", {"estudiantes": estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante.objects.select_related("programa"), pk=pk)
    inscripciones = estudiante.inscripciones.select_related("curso").all()
    return render(request, "estudiantes/detalle_estudiante.html", {"estudiante": estudiante, "inscripciones": inscripciones})

# INSCRIPCIONES
def lista_inscripciones(request):
    inscripciones = Inscripcion.objects.select_related("estudiante", "curso").order_by("-fecha")
    return render(request, "estudiantes/lista_inscripciones.html", {"inscripciones": inscripciones})

def detalle_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    return render(request, "estudiantes/detalle_inscripcion.html", {"inscripcion": inscripcion})
