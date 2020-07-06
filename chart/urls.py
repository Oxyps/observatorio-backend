from django.urls import path

from .views import SearchDataView, InformationView, LocationView, GranularityView

urlpatterns = [
    path('search-data/', SearchDataView.as_view(), name='data-list'),

	path('information/', InformationView.as_view(), name='information-list'),
    path('location/', LocationView.as_view(), name='location-list'),
    path('granularity/', GranularityView.as_view(), name='granularity-list'),
]
