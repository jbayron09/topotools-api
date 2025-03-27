from django.contrib import admin
from transformations3d.models import Transformation3d, TransformationPoints


@admin.register(Transformation3d)
class Transformation3dAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "transformation_type", "user", "created_at")
    fields = [field.name for field in Transformation3d._meta.get_fields() if not field.auto_created and field.editable]
    search_fields = ("id", "name", "user__username")
    list_filter = ("transformation_type", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(TransformationPoints)
class TransformationPointsAdmin(admin.ModelAdmin):
    list_display = ("id", "transformation", "created_at")
    fields = ["transformation", "origin_points", "destination_points", "created_at", "updated_at"]
    search_fields = ("transformation__name",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
