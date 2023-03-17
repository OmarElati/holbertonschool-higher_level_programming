-- Import in hbtn_0c_0 database this table dump.
USE hbtn_0c_0;
SELECT city, AVG((temperature - 32) * 5/9) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
