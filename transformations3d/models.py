from django.conf import settings
from django.db import models
from transformations3d.choices import TRANSFORMATION_TYPE_CHOICES
from transformations3d.constants import transformation_types as types
from transformations3d.validators import validate_points


class Transformation3d(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transformations3d",
        verbose_name="Usuario"
    )

    name = models.CharField(max_length=255, verbose_name="Nombre de la transformación")
    description = models.TextField(blank=True, verbose_name="Descripción")
    transformation_type = models.CharField(
        max_length=20,
        choices=TRANSFORMATION_TYPE_CHOICES,
        verbose_name="Tipo de transformación",
        default=types.HELMERT,
    )

    parameters = models.JSONField(verbose_name="Parámetros de transformación", blank=True)
    results = models.JSONField(verbose_name="Resultados de la transformación", blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_transformation_type_display()}"


class TransformationPoints(models.Model):
    transformation = models.OneToOneField(
        Transformation3d,
        on_delete=models.CASCADE,
        related_name="transformation_points",
        verbose_name="Puntos de transformación"
    )

    origin_points = models.JSONField(
        verbose_name="Puntos de Origen",
        validators=[validate_points]
    )
    destination_points = models.JSONField(
        verbose_name="Puntos de Destino",
        validators=[validate_points]
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return f"Puntos de {self.transformation.name} ({self.transformation.get_transformation_type_display()})"
