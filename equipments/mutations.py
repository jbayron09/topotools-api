from graphene import relay, Field, String, Float
from graphql import GraphQLError
from graphql_relay import from_global_id

from equipments.enums import EquipmentType
from equipments.models import Equipment
from equipments.nodes import EquipmentNode


class EquipmentFieldBase:
    name = String(required=True)
    serial_number = String(required=True)
    brand = String(required=False)
    model = String(required=False)
    equipment_type = EquipmentType(required=False)
    distance_constant = Float(required=True)
    distance_ppm = Float(required=True)
    angle = Float(required=True)
    direction = Float(required=True)
    azimuth_bearing = Float(required=True)
    zenith = Float(required=True)
    elev_diff_constant = Float(required=True)
    elev_diff_ppm = Float(required=True)
    horiz_instrument_error = Float(required=True)
    horiz_target_error = Float(required=True)
    vertical_error = Float(required=True)


class CreateEquipment(relay.ClientIDMutation):
    equipment = Field(EquipmentNode)

    class Input(EquipmentFieldBase):
        pass

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user
        equipment = Equipment(user=user)

        for field, value in input.items():
            if hasattr(value, "value"):
                value = value.value

            setattr(equipment, field, value)

        equipment.save()
        return CreateEquipment(equipment=equipment)


class UpdateEquipment(relay.ClientIDMutation):
    equipment = Field(EquipmentNode)

    class Input(EquipmentFieldBase):
        id = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, **input):
        _, decoded_id = from_global_id(id)

        try:
            equipment = Equipment.objects.get(id=decoded_id)
        except Equipment.DoesNotExist:
            raise GraphQLError("Equipment not found.")

        for field, value in input.items():
            if hasattr(value, "value"):
                value = value.value

            setattr(equipment, field, value)

        equipment.save()
        return UpdateEquipment(equipment=equipment)
