from django_filters import rest_framework as filters

from .models import ReferencePeriod

class ReferencePeriodFilter(filters.FilterSet):
	class Meta:
		model = ReferencePeriod
		fields = '__all__'

	in_date_gt = filters.DateFilter(field_name='in_date', lookup_expr='gt')
	until_date_lte = filters.DateFilter(field_name='until_date', lookup_expr='lte')
