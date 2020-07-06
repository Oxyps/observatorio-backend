from os import path
import json

with open(path.abspath('scripts/data_source/data.json')) as file:
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
	if key in new_source:
		new_source[key].append(locations_data)
	else:
		new_source[key] = [locations_data]

for key in new_source:
	with open(path.abspath(f'scripts/new_data/{key}.json'), 'w') as file:
		json.dump(new_source[key], file, indent=2)
