-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.id, cities.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id ASC;
