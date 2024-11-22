from graphene import relay
from graphene_django import DjangoObjectType

from equipments.filterset import EquipmentFilterSet
from equipments.models import Equipment


class EquipmentNode(DjangoObjectType):
    class Meta:
        model = Equipment
        filterset_class = EquipmentFilterSet
        interfaces = (relay.Node,)
