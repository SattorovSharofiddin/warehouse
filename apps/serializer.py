# serializers.py
from rest_framework import serializers


class WarehouseSerializer(serializers.Serializer):
    warehouse_id = serializers.IntegerField()
    material_name = serializers.CharField()
    qty = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductMaterialSerializer(serializers.Serializer):
    material_name = serializers.CharField()
    qty = serializers.FloatField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    warehouse_id = serializers.IntegerField(allow_null=True)


class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_qty = serializers.IntegerField()
    product_materials = ProductMaterialSerializer(many=True)
