import json
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.apps import apps


def getModel(model_name):
    '''get model Object by string

    Args:
        model_name (string): Symbol/Model Name

    Returns:
        Object: Model Object for queryset
    '''
    cont = ContentType.objects.get(model=model_name)
    ModelObject = apps.get_model(cont.app_label, model_name)
    return ModelObject


class StockSerializer(serializers.Serializer):
    """Serializer for stock data

    Attributes:
        itemask (Datetime)
        itembid (Int)
        itemchange (Decimal)
        itemfreq (Int)
        itemmarketcap (Int)
        itemprice (Int)
        itemtime (Int)
        itemturnover (Int)
        itemvolume (Int)
    """

    itemtime = serializers.DateTimeField()
    itemprice = serializers.IntegerField(max_value=None, min_value=None)
    itemchange = serializers.DecimalField(3, 2, coerce_to_string=None, max_value=None, min_value=None)
    itemturnover = serializers.IntegerField(max_value=None, min_value=None)
    itemmarketcap = serializers.IntegerField(max_value=None, min_value=None)
    itemvolume = serializers.IntegerField(max_value=None, min_value=None)
    itemfreq = serializers.IntegerField(max_value=None, min_value=None)
    itemask = serializers.IntegerField(max_value=None, min_value=None)
    itembid = serializers.IntegerField(max_value=None, min_value=None)

    def create(self, validated_data):
        ModelObject = self.context.get('model')
        return ModelObject.objects.create(**validated_data)
