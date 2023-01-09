from django.contrib import admin
from .models import Entity, Property


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass
