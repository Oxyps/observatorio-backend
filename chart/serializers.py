from rest_framework import serializers

from .models import Information, Granularity

class InformationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Information
		fields = '__all__'

class GranularitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Granularity
		fields = '__all__'
