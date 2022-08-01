from django.urls import path
from .views import CityListView, CityDeleteView

urlpatterns = [
    path(route='', view=CityListView.as_view(), name="cities"),
    path(route='city-delete/<int:pk>/',
         view=CityDeleteView.as_view(), name="city-delete"),
]
