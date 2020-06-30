from django_filters import rest_framework as filters

from .models import ReferencePeriod, Data

class ReferencePeriodFilter(filters.FilterSet):
	class Meta:
		model = ReferencePeriod
		fields = ['in_date_gt', 'until_date_lte']

	in_date_gt = filters.DateFilter(field_name='in_date', lookup_expr='gt')
	until_date_lte = filters.DateFilter(field_name='until_date', lookup_expr='lte')

class DataFilter(filters.FilterSet):
	class Meta:
		model = Data
		fields = [
			'id_information__nickname',
			'id_location__name',
			'id_granularity__granularity',
		]

	in_date_gt = filters.DateFilter(field_name='id_referenceperiod__in_date', lookup_expr='gt')
	until_date_lte = filters.DateFilter(field_name='id_referenceperiod__until_date', lookup_expr='lte')
