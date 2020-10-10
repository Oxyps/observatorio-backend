import json
from os import path

from .models import Location

def get_stateid_by_ibgeid(ibgeid):
	ibgeid = str(ibgeid)
	stateid = ''

	if ibgeid.__len__() >= 4:
		stateid = ibgeid[:2]
		return stateid

	# dont belong to a state
	return 0

def generate_json_files():
	with open(path.abspath('util/data_source/data.json'), encoding='utf-8') as file:
		json_source = json.load(file)

	new_source = {}
	for json_data in json_source:
		locations_data = {
			'information_nickname': json_data['information_nickname'],
			'information_datatype': json_data['information_datatype'],
			'granularity': json_data['granularity'],
			'in_date': json_data['in_date'],
			'until_date': json_data['until_date'],
			'data': json_data['data']
		}

		key = f"{json_data['location_type']}_{json_data['location_name']}"

		stateid = get_stateid_by_ibgeid(json_data['id_ibge'])
		if stateid != 0:
			queryset = Location.objects.filter(id_ibge=stateid)
			uf = queryset[0].nickname
			key += f'_{uf}'

		if not key in new_source:
			new_source[key] = []
		new_source[key].append(locations_data)

	for key in new_source:
		with open(path.abspath(f'util/data_locations/{key}.json'), 'w') as file:
			json.dump(new_source[key], file, indent=2)
