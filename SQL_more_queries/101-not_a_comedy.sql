-- Import the database dump from hbtn_0d_tvshows to your MySQL server.
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
WHERE t.`title` NOT IN
(
    SELECT DISTINCT t2.`title`
    FROM `tv_shows` AS t2
    INNER JOIN `tv_show_genres` AS s
    ON s.`show_id` = t2.`id`
    INNER JOIN `tv_genres` AS g
    ON g.`id` = s.`genre_id`
    WHERE g.`name` = "Comedy"
)
ORDER BY t.`title`;
