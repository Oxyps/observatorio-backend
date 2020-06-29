from rest_framework import generics

from .models import Data, Information, Granularity, DataType, Location, ReferencePeriod
from .serializers import DataSerializer, InformationSerializer, GranularitySerializer, DataTypeSerializer, LocationSerializer, ReferencePeriodSerializer

class DataView(generics.ListAPIView):
	queryset = Data.objects.all()
	serializer_class = DataSerializer

class InformationView(generics.ListAPIView):
	queryset = Information.objects.all()
	serializer_class = InformationSerializer

class DataTypeView(generics.ListAPIView):
	queryset = DataType.objects.all()
	serializer_class = DataTypeSerializer

class LocationView(generics.ListAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class GranularityView(generics.ListAPIView):
	queryset = Granularity.objects.all()
	serializer_class = GranularitySerializer

class ReferencePeriodView(generics.ListAPIView):
	queryset = ReferencePeriod.objects.all()
	serializer_class = ReferencePeriodSerializer
