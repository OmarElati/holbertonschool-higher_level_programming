-- Import the database dump from hbtn_0d_tvshows to your MySQL server.
USE `hbtn_0d_tvshows`;

SELECT `tv_genres.name`
FROM `tv_genres`
LEFT JOIN (
    SELECT `tv_genres.id`
    FROM `tv_genres`
    JOIN `tv_show_genres` ON `tv_show_genres.genre_id` = `tv_genres.id`
    JOIN `tv_shows` ON `tv_shows.id` = `tv_show_genres.show_id`
    WHERE `tv_shows.title` = 'Dexter'
) AS `dexter_genres` ON `dexter_genres.id` = `tv_genres.id`
WHERE `dexter_genres.id` IS NULL
ORDER BY `tv_genres.name` ASC;
