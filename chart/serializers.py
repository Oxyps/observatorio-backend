from rest_framework import serializers

from .models import Data, Information, Granularity, DataType, Location, ReferencePeriod

class DataSerializer(serializers.ModelSerializer):

    class Meta:

        model = Data
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Information
        fields = '__all__'

class GranularitySerializer(serializers.ModelSerializer):

    class Meta:

        model = Granularity
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Location
        fields = '__all__'

class ReferencePeriodSerializer(serializers.ModelSerializer):

    class Meta:

        model = ReferencePeriod
        fields = '__all__'
