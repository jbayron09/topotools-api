from django.contrib import admin

from equipments.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "serial_number", "created_at")
    fields = [field.name for field in Equipment._meta.get_fields() if not field.auto_created and field.editable]
    search_fields = ('id',)
    list_filter = ("equipment_type", "brand")
    ordering = ('-created_at',)
    readonly_fields = ()
