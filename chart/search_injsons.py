from os import path
from datetime import date
import json

# é possível reduzir a quantia de dados do BD removendo a coluna in_date
# a coluna in_date é irrelevante, desde que tem-se a coluna granularidade
# é possível descobrir a data inicial apenas com a granularidade menos until_date
# prioriza-se o desempenho em memória contra o em processamento

def pt_br(string):
	if string == 'bimonthly':
		return 'bimestral'
	elif string == 'quarterly':
		return 'trimestral'
	elif string == 'half-yearly':
		return 'semestral'
	elif string == 'yearly':
		return 'anual'

def search_location_data_injson(information_param, location_name_param, location_type_param, in_date_param, until_date_param, granularity_param):
	with open(path.abspath(f'scripts/new_data/{location_type_param}_{location_name_param}.json')) as file:
		json_file = json.load(file)

	response = {}
	response_data = []
	response_until_dates = []
	for json_data in json_file:
		if json_data['information_nickname'] != information_param:
			continue

		if json_data['granularity'] != granularity_param:
			break

		in_date_param = str(in_date_param).split('-')
		in_date_json = str(json_data['in_date']).split('-')
		in_date_param = date(int(in_date_param[0]), int(in_date_param[1]), int(in_date_param[2]))
		in_date_json = date(int(in_date_json[0]), int(in_date_json[1]), int(in_date_json[2]))
		if in_date_json <= in_date_param:
			break

		until_date_param = str(until_date_param).split('-')
		until_date_json = str(json_data['until_date']).split('-')
		until_date_param = date(int(until_date_param[0]), int(until_date_param[1]), int(until_date_param[2]))
		until_date_json = date(int(until_date_json[0]), int(until_date_json[1]), int(until_date_json[2]))
		if until_date_json > until_date_param:
			break

		response_data.append(json_data['data'])
		response_until_dates.append(until_date_json.__str__())

	response['until_dates'] = response_until_dates
	response['dataset'] = [
		{
			'label': f'{information_param} - {location_type_param} {location_name_param}, período {pt_br(granularity_param)}',
			'data': response_data
		}
	]

	if len(response_data) == 0:
		response['dataset']['label'] = ''

	return response
