from rest_framework import serializers
from .models import Property, Entity


class PropertiesField(serializers.Field):

  def to_representation(self, value):
    ret = dict()
    for prop in value.properties.all():
      ret[prop.key] = prop.value
    return ret


class PropertySerializer(serializers.ModelSerializer):
  key = PropertiesField(source='*')

  class Meta:
    model = Property
    fields = ['key', 'value']


class EntitySerializer(serializers.ModelSerializer):
  properties = PropertiesField(source='*', read_only=True)

  class Meta:
    model = Entity
    fields = ['value', 'properties']
