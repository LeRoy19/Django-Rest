from django.urls import path
from ..api.views import *

urlpatterns = [
    path("manufacturers/", manufacturer_list_create_api_view, name="manufacturer-list"),
    path("manufacturers/<int:pk>/", manufacturer_detail_api_view, name="manufacturer-detail")
]
