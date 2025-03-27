from django.conf import settings
from django.db import models


class Transformation3d(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transformations3d",
        verbose_name="Usuario"
    )
    name = models.CharField(max_length=200, verbose_name="Nombre del Ajuste")
    description = models.TextField(null=True, blank=True, verbose_name="Descripción")
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pendiente"), ("confirmed", "Confirmado")],
        default="pending",
        verbose_name="Estado del Ajuste"
    )

    # Parámetros y resultados en JSON (para mayor flexibilidad)
    parameters = models.JSONField(verbose_name="Parámetros de Transformación")
    results = models.JSONField(null=True, blank=True, verbose_name="Resultados del Ajuste")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"


class AdjustmentPoint(models.Model):
    adjustment = models.ForeignKey(
        Transformation3d,
        on_delete=models.CASCADE,
        related_name="points",
        verbose_name="Ajuste Relacionado"
    )
    origin_points = models.JSONField(verbose_name="Puntos de Origen")  # Lista de puntos [{x, y, z}, ...]
    destination_points = models.JSONField(verbose_name="Puntos de Destino")  # Lista de puntos [{x, y, z}, ...]

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    def __str__(self):
        return f"Puntos de {self.adjustment.name}"
