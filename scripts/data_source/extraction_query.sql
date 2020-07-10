/* select relevant data from chart_data table */
/* order by information and granularity to generate json files */

SELECT
    i.nickname AS "information_nickname",
    t.datatype AS "information_datatype",
	l.id_ibge, l.name AS "location_name", l.location_type,
	g.granularity,
    r.in_date, r.until_date,
	d.data
FROM
    data d JOIN location l ON d.id_location=l.id_ibge
    JOIN granularity g ON d.id_granularity=g.id
    JOIN referenceperiod r ON d.id_referenceperiod=r.id
    JOIN information i ON d.id_information=i.id
    JOIN datatype t ON i.id_datatype=t.id
ORDER BY 1, 3, 6;
