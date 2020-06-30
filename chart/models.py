from django.db import models

class Granularity(models.Model):
	def __str__(self):
		return self.granularity

	granularity = models.CharField(max_length=20)

class ReferencePeriod(models.Model):
	def __str__(self):
		return f'{self.in_date} / {self.until_date}'

	in_date = models.DateField()
	until_date = models.DateField()

class Location(models.Model):
	def __str__(self):
		return self.name

	id_ibge = models.PositiveIntegerField(primary_key=True)
	id_ibge_memberof = models.PositiveIntegerField()
	name = models.CharField(max_length=45)
	nickname = models.CharField(max_length=10)
	location_type = models.CharField(max_length=45)
	geo_latitude = models.FloatField()
	geo_longitude = models.FloatField()

class DataType(models.Model):
	def __str__(self):
		return self.datatype

	datatype = models.CharField(max_length=20)

class Information(models.Model):
	def __str__(self):
		return f'{self.id_datatype.datatype} - {self.nickname}'

	nickname = models.CharField(max_length=15)
	shortname = models.CharField(max_length=100)
	longname = models.CharField(max_length=256)
	definition = models.TextField(max_length=2048)
	id_datatype = models.ForeignKey('DataType', on_delete=models.DO_NOTHING, db_column='id_datatype')

class Data(models.Model):
	class Meta:
		unique_together = (('id_information', 'id_referenceperiod', 'id_location', 'id_granularity'),)

	def __str__(self):
		return f'{self.id_information} - {self.id_location} - {self.id_referenceperiod} - {self.id_granularity} - {self.data}'

	id_information = models.ForeignKey('Information', on_delete=models.DO_NOTHING, db_column='id_information')
	id_referenceperiod = models.ForeignKey('ReferencePeriod', on_delete=models.DO_NOTHING, db_column='id_referenceperiod')
	id_location = models.ForeignKey('Location', on_delete=models.DO_NOTHING, db_column='id_location')
	id_granularity = models.ForeignKey('Granularity', on_delete=models.DO_NOTHING, db_column='id_granularity')
	data = models.FloatField()
