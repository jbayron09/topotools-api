from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField

from equipments.mutations import CreateEquipment, UpdateEquipment
from equipments.nodes import EquipmentNode


class Query(ObjectType):
    equipment = relay.Node.Field(EquipmentNode)
    equipments = DjangoFilterConnectionField(EquipmentNode)


class Mutation(ObjectType):
    create_equipment = CreateEquipment.Field()
    update_equipment = UpdateEquipment.Field()
