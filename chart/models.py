from django.db import models

class Granularity(models.Model):
	class Meta():
		db_table = 'granularity'

	def __str__(self):
		return self.granularity

	granularity = models.CharField(max_length=20)

class ReferencePeriod(models.Model):
	class Meta():
		db_table = 'referenceperiod'

	def __str__(self):
		return f'{self.in_date} / {self.until_date}'

	in_date = models.DateField()
	until_date = models.DateField()

class Location(models.Model):
	class Meta():
		db_table = 'location'

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
	class Meta():
		db_table = 'datatype'

	def __str__(self):
		return self.datatype

	datatype = models.CharField(max_length=20)

class Information(models.Model):
	class Meta():
		db_table = 'information'

	def __str__(self):
		return f'{self.nickname} - {self.datatype}'

	nickname = models.CharField(max_length=15)
	shortname = models.CharField(max_length=100)
	longname = models.CharField(max_length=256)
	definition = models.TextField(max_length=2048)
	datatype = models.ForeignKey('DataType', on_delete=models.DO_NOTHING, db_column='id_datatype')

class Data(models.Model):
	class Meta:
		db_table = 'data'

	def __str__(self):
		return f'{self.information} - {self.location} - {self.referenceperiod} - {self.granularity} - {self.data}'

	information = models.ForeignKey('Information', on_delete=models.DO_NOTHING, db_column='id_information')
	referenceperiod = models.ForeignKey('ReferencePeriod', on_delete=models.DO_NOTHING, db_column='id_referenceperiod')
	location = models.ForeignKey('Location', on_delete=models.DO_NOTHING, db_column='id_location')
	granularity = models.ForeignKey('Granularity', on_delete=models.DO_NOTHING, db_column='id_granularity')
	data = models.FloatField()
