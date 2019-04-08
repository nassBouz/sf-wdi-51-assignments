--Select airport code for airports like 'John F Kennedy' and 'De Gaulle'.
SELECT iata_faa
FROM airports
WHERE name LIKE 'John F Kennedy%'
OR  name LIKE '%De Gaulle';

--Select all the flights originating from 'JFK' and going to 'CDG'.
SELECT *
FROM routes
WHERE origin_code = 'JFK'
AND dest_code = 'CDG';

--Find out the number of airports in Canada.
SELECT COUNT(*)
FROM airports
WHERE country LIKE 'Canada';

--Select all the airports that airlines 'Germania' flies from.
SELECT a.name AS airlines, b.name as airports
FROM routes r, airlines a, airports b
WHERE a.id = r.airline_id
AND r.origin_code = b.iata_faa
AND a.name='Germania';

--Select airport names in the following countries- Algeria, Ghana, Ethiopia, order by country.
SELECT a.name, a.city, a.country
FROM airports a
WHERE a.country IN ('Ghana', 'Algeria', 'Ethiopia')
ORDER BY a.country;

