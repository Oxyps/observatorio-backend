from django_filters import rest_framework as filters

from .models import ReferencePeriod, Data

class ReferencePeriodFilter(filters.FilterSet):
	class Meta:
		model = ReferencePeriod
		fields = [
			'in_date_gt',
			'until_date_lte'
		]

	in_date_gt = filters.DateFilter(field_name='in_date', lookup_expr='gt')
	until_date_lte = filters.DateFilter(field_name='until_date', lookup_expr='lte')

class DataFilter(filters.FilterSet):
	class Meta:
		model = Data
		fields = [
			'information_nickname',
			'location_name',
			'granularity',
			'in_date_gt',
			'until_date_lte'
		]

	information_nickname = filters.CharFilter(field_name='id_information__nickname', label='information_nickname')
	location_name = filters.CharFilter(field_name='id_location__name', label='location_name')
	granularity = filters.CharFilter(field_name='id_granularity__granularity', label='granularity')
	in_date_gt = filters.DateFilter(field_name='id_referenceperiod__in_date', label='in_date_gt', lookup_expr='gt')
	until_date_lte = filters.DateFilter(field_name='id_referenceperiod__until_date', label='until_date_lte', lookup_expr='lte')
