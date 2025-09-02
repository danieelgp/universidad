from django.core.exceptions import ValidationError
from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.CharField(max_length=50, blank=True, null=True)  # Ej: "5 semestres"
    codigo = models.CharField(max_length=20, blank=True, null=True)    # Ej: "ING-SIS"

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    creditos = models.PositiveIntegerField(blank=True, null=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, null=True)  # nuevo campo
    email = models.EmailField(unique=True)
    programa = models.ForeignKey(Programa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido or ''}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='inscripciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='inscripciones')
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')  # evita duplicados

    def clean(self):
        """
        Validación: el curso debe pertenecer al mismo programa que el estudiante.
        Si el estudiante no tiene programa asignado, se permite la inscripción.
        """
        if self.estudiante.programa and self.curso.programa != self.estudiante.programa:
            raise ValidationError(
                f"El curso '{self.curso}' no pertenece al programa de {self.estudiante}."
            )

    def __str__(self):
        return f"{self.estudiante} → {self.curso}"

    @property
    def fecha_inscripcion(self):
        """Alias para usar en la plantilla detalle_inscripcion.html"""
        return self.fecha
