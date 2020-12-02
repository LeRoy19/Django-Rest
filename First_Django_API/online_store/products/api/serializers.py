from rest_framework import serializers
from ..models import Manufacturer, Product
# from datetime import datetime
# from django.utils import timesince


class ManufacturerSerializer(serializers.ModelSerializer):

    products = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="product-detail")

    class Meta:
        model = Manufacturer
        exclude = ("id",)

    def validate(self, data):
        """
        Chek that name and location are different
        :param data: data that must be checked
        :return: data
        """

        if data["name"] == data["location"]:
            raise serializers.ValidationError("Name and Location must be different!")
        return data

    @staticmethod
    def validate_name(value):
        """
        Check that the name is shorter than 101 characters
        :param value: name that must be checked
        :return: value
        """

        if len(value) > 100:
            raise serializers.ValidationError("The name is longer that 100 characters!")
        return value


class ProductSerializer(serializers.ModelSerializer):

    # Display the name of the manufacturer instead his id
    # manufacturer = serializers.StringRelatedField()

    # make nested request
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = "__all__"
