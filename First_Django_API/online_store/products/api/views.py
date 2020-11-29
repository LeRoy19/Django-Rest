from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Manufacturer
from ..api.serializers import ManufacturerSerializer


@api_view(["GET", "POST"])
def manufacturer_list_create_api_view(request):

    if request.method == "GET":
        manufactures = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufactures, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def manufacturer_detail_api_view(request, pk):

    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist:
        return Response({"error": {
            "code": 404,
            "message": "Article not found!",

        }}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ManufacturerSerializer(manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
