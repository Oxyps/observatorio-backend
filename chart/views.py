from rest_framework import generics
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Information, Location, Granularity
from .serializers import InformationSerializer

from .search_injsons import search_location_data_injson, pt_br
from .generate_jsons import generate_json_files, get_stateid_by_ibgeid

class SearchDataView(APIView):
	def get(self, request, format=None):
		params = request.query_params

		if(	'information_nickname' in params and
			'location_name' in params and
			'location_type' in params and
			'location_state' in params and
			'in_date_gt' in params and
			'until_date_lte' in params and
			'granularity' in params
		):
			information = params['information_nickname']
			location_name = params['location_name']
			location_type = params['location_type']
			location_state = params['location_state']
			in_date = params['in_date_gt']
			until_date = params['until_date_lte']
			granularity = params['granularity']

			try:
				response = search_location_data_injson(information, location_name, location_type, location_state, in_date, until_date, granularity)
				return Response(response)
			except FileNotFoundError:
				return Response({
					'error': f'no data for location_type={{{location_type}}}, location_name={{{location_name}}} and location_state={{{location_state}}}. check names syntax. must exist in the database.'
				}, status=HTTP_404_NOT_FOUND)
			except ValueError:
				return Response({
					'error': f'check in_date={{{in_date}}} and until_date={{{until_date}}} syntax. format: yyyy-mm-dd. {{y}}, {{m}} and {{d}} must be 10 base numbers.'
				}, status=HTTP_404_NOT_FOUND)
		return Response({
			'error': 'must have all query params: {information_nickname}, {location_name}, {location_type}, {location_state}, {in_date_gt}, {until_date_lte}, {granularity}.'
		}, status=HTTP_400_BAD_REQUEST)

class InformationView(generics.ListAPIView):
	queryset = Information.objects.all()

	serializer_class = InformationSerializer

class LocationView(APIView):
	def get(self, request, format=None):
		queryset = Location.objects.all()

		response = {}

		for location in queryset:
			if(not location.location_type in response):
				response[location.location_type] = []

			stateid = get_stateid_by_ibgeid(location.id_ibge)
			uf = Location.objects.filter(id_ibge=stateid)[0].nickname

			response[location.location_type].append({
				'id': location.id_ibge,
				'name': location.name,
				'state': uf
			})

		return Response(response)

class GranularityView(APIView):
	def get(self, request, format=None):
		queryset = Granularity.objects.all()

		response = []

		for granularity in queryset:
			response.append({
				'id': granularity.id,
				'granularity': granularity.granularity,
				'granularidade': pt_br(granularity.granularity)
			})

		return Response({"data": response})

class GenerateJsonFilesView(APIView):
	def get(self, request, format=None):
		generate_json_files()
		return Response({'success': 'created json files.'})
