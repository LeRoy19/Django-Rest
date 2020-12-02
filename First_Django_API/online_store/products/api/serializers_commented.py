from rest_framework import serializers
from ..models import Manufacturer
# from datetime import datetime
# from django.utils import timesince

"""
Serializers are classes that allows rest API to accept and comprehend different kind of requests
"""

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        exclude = ("id",)
        # fields = "__all__" # all the fields of our model
        # fiels = ("name", ... ,)

        # generates an extra field
        # time_since_publication = serializers.SerializerMethodField()

    # def get_time_since_publication(self, object):
    #     return timesince(object.publication_date, datetime.now())

    def validate(self, data):
        """
        Chek that name and location are different
        :param data: data that must be checked
        :return: data
        """

        if data["name"] == data["location"]:
            raise serializers.ValidationError("Name and Location must be different!")
        return data

    def validate_name(self, value):
        """
        Check that the name is shorter than 101 characters
        :param value: name that must be checked
        :return: value
        """

        if len(value) > 100:
            raise serializers.ValidationError("The name is longer that 100 characters!")
        return value


# class ManufacturerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     location = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.location = validated_data.get('location', instance.location)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         return Manufacturer.objects.create(**validated_data)
#
#     def validate(self, data):
#         """
#         Chek that name and location are different
#         :param data: data that must be checked
#         :return: data
#         """
#
#         if data["name"] == data["location"]:
#             raise serializers.ValidationError("Name and Location must be different!")
#         return data
#
#     def validate_name(self, value):
#         """
#         Check that the name is shorter than 101 characters
#         :param value: name that must be checked
#         :return: value
#         """
#
#         if len(value) > 100:
#             raise serializers.ValidationError("The name is longer that 100 characters!")
#         return value


"""
An example of serialization:
>>> from products.models import Manufacturer
>>> from products.api.serializers import ManufacturerSerializer
>>> manufacturer_instance = Manufacturer.objects.first()
>>> manufacturer_instance
<Manufacturer: Sony>

>>> serializer = ManufacturerSerializer(manufacturer_instance)
>>> serializer
ManufacturerSerializer(<Manufacturer: Sony>):
    id = IntegerField(read_only=True)
    name = CharField()
    location = CharField()
    active = BooleanField()
>>> serializer.data
{'id': 1, 'name': 'Sony', 'location': 'Italy', 'active': True}

>>> from rest_framework.renderers import JSONRenderer
>>> json = JSONRenderer().render(serializer.data)
>>> json
b'{"id":1,"name":"Sony","location":"Italy","active":true}'

Deserialization: 
>>> import io
>>> from rest_framework.parsers import JSONParser
>>> stream = io.BytesIO(json)
>>> data = JSONParser().parse(stream)
>>> data
{'id': 1, 'name': 'Sony', 'location': 'Italy', 'active': True}

>>> serializer = ManufacturerSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([('name', 'Sony'), ('location', 'Italy'), ('active', True)])
>>> serializer.save()
{'name': 'Sony', 'location': 'Italy', 'active': True}
<Manufacturer: Sony>
>>> Manufacturer.objects.all()
<QuerySet [<Manufacturer: Sony>, <Manufacturer: Sony>]>

We saved another instances of Manufacturer
"""
