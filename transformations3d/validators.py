from django.core.exceptions import ValidationError


def validate_points(value):
    """
    Valida que el JSONField contenga una lista de puntos con 'x', 'y' y 'z'.
    """
    if not isinstance(value, list):
        raise ValidationError("El valor debe ser una lista de puntos.")

    for point in value:
        if not isinstance(point, dict):
            raise ValidationError("Cada punto debe ser un diccionario con claves 'x', 'y', 'z'.")

        if not all(key in point for key in ('x', 'y', 'z')):
            raise ValidationError("Cada punto debe contener las claves 'x', 'y' y 'z'.")

        if not all(isinstance(point[key], (int, float)) for key in ('x', 'y', 'z')):
            raise ValidationError("Los valores de 'x', 'y' y 'z' deben ser números.")
