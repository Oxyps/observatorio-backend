"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import DataView, InformationView, GranularityView, DataTypeView, LocationView, ReferencePeriodView

urlpatterns = [
    path('data/', DataView.as_view(), name='data-list'),
    path('datatype/', DataTypeView.as_view(), name='datatype-list'),
    path('information/', InformationView.as_view(), name='information-list'),
    path('location/', LocationView.as_view(), name='location-list'),
    path('granularity/', GranularityView.as_view(), name='granularity-list'),
    path('referenceperiod/', ReferencePeriodView.as_view(), name='referenceperiod-list'),
]
