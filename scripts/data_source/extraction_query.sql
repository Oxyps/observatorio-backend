/* select relevant data from chart_data table */
/* order by information and granularity to generate json files */
SELECT i.nickname AS "information_nickname", t.datatype AS "information_datatype", l.name AS "location_name", l.location_type, g.granularity, r.in_date, r.until_date, d.data FROM chart_data d JOIN chart_location l ON d.id_location=l.id_ibge JOIN chart_granularity g ON d.id_granularity=g.id JOIN chart_referenceperiod r ON d.id_referenceperiod=r.id JOIN chart_information i ON d.id_information=i.id JOIN chart_datatype t ON i.id_datatype=t.id ORDER BY 1, 5;
