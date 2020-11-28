from django.urls import path

from .views import *


urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("active-manufacturers/", active_manufacturer_list, name="active_manufacturer_list"),
    path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer_detail"),
]
