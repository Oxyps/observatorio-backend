from django.contrib import admin

from .models import DataType, Granularity, ReferencePeriod, Location, Information, Data

admin.site.register(DataType)
admin.site.register(Granularity)
admin.site.register(ReferencePeriod)
admin.site.register(Location)
admin.site.register(Information)
admin.site.register(Data)
