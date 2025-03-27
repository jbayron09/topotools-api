from graphene import Enum

from transformations3d.choices import TRANSFORMATION_TYPE_CHOICES
from snipets.graphql.enums import choices_to_enum

TransformationTypeEnum = Enum(
    "TransformationTypeEnum",
    choices_to_enum(TRANSFORMATION_TYPE_CHOICES)
)
