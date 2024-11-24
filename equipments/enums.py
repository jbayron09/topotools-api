from graphene import Enum

from equipments.choices import EQUIPMENT_TYPES_CHOICES
from snipets.graphql.enums import choices_to_enum

EquipmentType = Enum("EquipmentType",
                         choices_to_enum(EQUIPMENT_TYPES_CHOICES))
