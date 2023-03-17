-- Import in hbtn_0c_0 database this table dump.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
