# Lab - Postgres

## Setup

1. Create a new database called `flights`, connect to it, and run the following code:

  ```sql
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
  ```

1. You can check if above tables are created by running command `\dt` in your psql shell. 

2. Clone this repo and copy [airlines.csv](airlines.csv),  [airports.csv](airports.csv),  and [routes.csv](routes.csv) to your Desktop directory on your computer.

1. Run the following code, substituting your computer's username for mine.  If you're unsure of the full path, `cd` to your Desktop and `pwd`.

  ```sql
  COPY routes FROM '/Users/<your-username>/Desktop/routes.csv' DELIMITER ',' CSV;
  COPY airports FROM '/Users/<your-username>/Desktop/airports.csv' DELIMITER ',' CSV;
  COPY airlines FROM '/Users/<your-username>/Desktop/airlines.csv' DELIMITER ',' CSV;
  ```

1. You should now have seeded three tables with flight data. Run `SELECT * FROM <table-name> LIMIT 10;` to confirm.

## Goal

1. Select airport code for airports LIKE 'John F Kennedy' or 'De Gaulle'. 
2. Select all the flights originating from 'JFK' AND going to 'CDG'.
3. Find out the NUMBER of airports in Canada.
4. Select airport names IN the following countries- Algeria, Ghana, Ethiopia, order by country.  
5. Select all the airports that airlines 'Germania' flies from.

## Bonus

If you want to practice writing SQL queries more. Create an account on hackerrank.com and follow this link- 

https://www.hackerrank.com/domains/sql?badge_type=sql&filters%5Bdifficulty%5D%5B%5D=easy&filters%5Bsubdomains%5D%5B%5D=select 
