from django_filters import FilterSet

from equipments.models import Equipment


class EquipmentFilterSet(FilterSet):
    class Meta:
        model = Equipment
        fields = {
            "name": ["exact", "icontains"]
        }
