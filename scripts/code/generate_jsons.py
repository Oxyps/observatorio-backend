from os import path
import json

with open(path.abspath('scripts/data_source/chart_data.json')) as file:
	source = json.load(file)

new_source = {}
for data in source:
	locations_data = {
		'granularity': data['granularity'],
		'until_date': data['until_date'],
		'in_date': data['in_date'],
		'data': data['data']
	}

	key = f"{data['location_type']}_{data['location_name']}"
	if key in new_source:
		new_source[key].append(locations_data)
	else:
		new_source[key] = [locations_data]

for key in new_source:
	with open(path.abspath(f'scripts/new_data/{key}.json'), 'w') as file:
		json.dump(new_source[key], file, indent=2)
