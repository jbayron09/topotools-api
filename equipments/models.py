from django.conf import settings
from django.db import models

from equipments.choices import EQUIPMENT_TYPES_CHOICES
from equipments.constants import equipment_types as types


class Equipment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="equipments",
        verbose_name="Usuario propietario"
    )

    # Campos de identificación del equipo
    name = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="Serial del Equipo")
    brand = models.CharField(max_length=100, null=True, verbose_name="Marca del Equipo")
    model = models.CharField(max_length=100, null=True, verbose_name="Modelo del Equipo")
    equipment_type = models.CharField(
        max_length=50,
        null=True,
        verbose_name="Tipo de Equipo",
        choices=EQUIPMENT_TYPES_CHOICES,
        default=types.OTHER
    )

    # Campos técnicos
    distance_constant = models.FloatField(default=0.0, verbose_name="Constante de Distancia (m)")
    distance_ppm = models.FloatField(default=0.0, verbose_name="PPM de Distancia")
    angle = models.FloatField(default=0.0, verbose_name="Ángulo (segundos)")
    direction = models.FloatField(default=0.0, verbose_name="Dirección (segundos)")
    azimuth_bearing = models.FloatField(default=0.0, verbose_name="Azimut / Rumbo (segundos)")
    zenith = models.FloatField(default=0.0, verbose_name="Cenit (segundos)")
    elev_diff_constant = models.FloatField(default=0.0, verbose_name="Constante de Diferencia de Elevación (m)")
    elev_diff_ppm = models.FloatField(default=0.0, verbose_name="PPM de Diferencia de Elevación")
    horiz_instrument_error = models.FloatField(default=0.0, verbose_name="Error Horizontal del Instrumento (m)")
    horiz_target_error = models.FloatField(default=0.0, verbose_name="Error Horizontal del Objetivo (m)")
    vertical_error = models.FloatField(default=0.0, verbose_name="Error Vertical (m)")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.serial_number})"
