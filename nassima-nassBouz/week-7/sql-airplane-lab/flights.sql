CREATE TABLE airlines (
  id int,
  name varchar(255) DEFAULT NULL,
  alias varchar(255) DEFAULT NULL,
  iata varchar(255) DEFAULT NULL,
  icao varchar(255) DEFAULT NULL,
  callsign varchar(255) DEFAULT NULL,
  country varchar(255) DEFAULT NULL,
  active varchar(255) DEFAULT NULL
);

CREATE TABLE airports (
  id int,
  name varchar(255) DEFAULT NULL,
  city varchar(255) DEFAULT NULL,
  country varchar(255) DEFAULT NULL,
  iata_faa varchar(255) DEFAULT NULL,
  icao varchar(255) DEFAULT NULL,
  latitude varchar(255) DEFAULT NULL,
  longitude varchar(255) DEFAULT NULL,
  altitude varchar(255) DEFAULT NULL,
  utc_offset varchar(255) DEFAULT NULL,
  dst varchar(255) DEFAULT NULL,
  tz varchar(255) DEFAULT NULL
);

CREATE TABLE routes (
  airline_code varchar(255) DEFAULT NULL,
  airline_id int DEFAULT NULL,
  origin_code varchar(255) DEFAULT NULL,
  origin_id int DEFAULT NULL,
  dest_code varchar(255) DEFAULT NULL,
  dest_id int DEFAULT NULL,
  codeshare varchar(255) DEFAULT NULL,
  stops int DEFAULT NULL,
  equipment varchar(255) DEFAULT NULL
);

-- 1
select id, name from airports where
name like 'John F Kennedy%' or name like '%De Gaulle'
-- 2
select * from routes where origin_code='JFK' and dest_code='CDG'
-- 3
SELECT COUNT(id)
FROM airports where country='Canada'
-- 4

SELECT name from airports 
where country in ('Canada', 'Algeria','Ghana') 
order by country
-- 5
select a.name , b.name 
from routes r, airlines a , airports b
where a.id = r.airline_id
and r.origin_code = b.iata_faa
and a.name ='Germania'