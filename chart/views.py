from rest_framework import generics
from django_filters import rest_framework
from rest_framework import filters

from .models import Data, Information, Granularity, DataType, Location, ReferencePeriod
from .serializers import DataSerializer, InformationSerializer, GranularitySerializer, LocationSerializer, ReferencePeriodSerializer

from .filters import ReferencePeriodFilter, DataFilter

class DataView(generics.ListAPIView):
	queryset = Data.objects.all()

	serializer_class = DataSerializer

	filter_backends = (rest_framework.DjangoFilterBackend,)
	filter_class = DataFilter

class InformationView(generics.ListAPIView):
	queryset = Information.objects.all()

	serializer_class = InformationSerializer

class LocationView(generics.ListAPIView):
	queryset = Location.objects.all()

	serializer_class = LocationSerializer

class GranularityView(generics.ListAPIView):
	queryset = Granularity.objects.all()

	serializer_class = GranularitySerializer

	filter_backends = (rest_framework.DjangoFilterBackend,)
	filter_fields = '__all__'

class ReferencePeriodView(generics.ListAPIView):
	queryset = ReferencePeriod.objects.all()

	serializer_class = ReferencePeriodSerializer

	filter_backends = (rest_framework.DjangoFilterBackend,)
	filter_class = ReferencePeriodFilter
