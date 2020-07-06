from rest_framework import generics
from django_filters import rest_framework
from rest_framework import filters

from .models import Information, Location, Granularity
from .serializers import InformationSerializer, LocationSerializer, GranularitySerializer

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
