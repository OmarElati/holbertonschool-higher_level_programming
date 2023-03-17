-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server.
SELECT g.`name`, SUM(r.`rate`) AS `rating`
FROM `tv_genres` g
INNER JOIN `tv_show_genres` s ON g.`id` = s.`genre_id`
INNER JOIN `tv_show_ratings` r ON s.`show_id` = r.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC;
