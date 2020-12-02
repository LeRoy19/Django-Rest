from django.urls import path
from ..api.views import *


urlpatterns = [
    # path("manufacturers/", manufacturer_list_create_api_view, name="manufacturer-list"),
    # path("manufacturers/<int:pk>/", manufacturer_detail_api_view, name="manufacturer-detail")
    path("manufacturers/", ManufacturerListAPIView.as_view(), name="manufacturer-list"),
    path("manufacturers/<int:pk>/", ManufacturerDetailAPIView.as_view(), name="manufacturer-detail"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("products/", ProductListAPIView.as_view(), name="product-list"),
]
