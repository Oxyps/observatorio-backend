from rest_framework import generics
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Information, Location, Granularity
from .serializers import InformationSerializer, GranularitySerializer
from .search_injsons import search_location_data_injson

class SearchDataView(APIView):
	def get(self, request, format=None):
		params = request.query_params

		if 'information_nickname' in params:
			information = params['information_nickname']
			if 	'location_name' in params:
				location_name = params['location_name']
				if 'location_type' in params:
					location_type = params['location_type']
					if 'in_date_gt' in params:
						in_date = params['in_date_gt']
						if 'until_date_lte' in params:
							until_date = params['until_date_lte']
							if 'granularity' in params:
								granularity = params['granularity']

								try:
									response = search_location_data_injson(information, location_name, location_type, in_date, until_date, granularity)
									return Response(response)
								except FileNotFoundError:
									return Response({
										'detail': f'no data for location_type={{{location_type}}} and location_name={{{location_name}}}. check names syntax. must exist in the database.'
									}, status=HTTP_404_NOT_FOUND)
								except ValueError:
									return Response({
										'detail': f'check in_date={{{in_date}}} and until_date={{{until_date}}} syntax. format: yyyy-mm-dd. {{y}}, {{m}} and {{d}} must be 10 base numbers.'
									}, status=HTTP_404_NOT_FOUND)
		return Response({
			'detail': 'must have all query params: {information_nickname}, {location_name}, {location_type}, {in_date_gt}, {until_date_lte}, {granularity}.'
		}, status=HTTP_400_BAD_REQUEST)

class InformationView(generics.ListAPIView):
	queryset = Information.objects.all()

	serializer_class = InformationSerializer

class LocationView(generics.ListAPIView):
	def get(self, request, format=None):
		locations = Location.objects.all()

		response = {}

		for location in locations:
			if(not location.location_type in response):
				response[location.location_type] = []

			response[location.location_type].append({
				'id': location.id_ibge,
				'name': location.name
			})

		return Response(response)

class GranularityView(generics.ListAPIView):
	queryset = Granularity.objects.all()

	serializer_class = GranularitySerializer
