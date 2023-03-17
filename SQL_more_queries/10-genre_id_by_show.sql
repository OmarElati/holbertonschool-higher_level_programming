-- Import the database dump from hbtn_0d_tvshows to your MySQL server.
SELECT title, genre_id 
FROM (
    SELECT ts.title, tsg.genre_id, COUNT(*) AS genre_count 
    FROM tv_shows ts 
    JOIN tv_show_genres tsg ON ts.id = tsg.show_id 
    GROUP BY ts.id, tsg.genre_id
) AS subquery 
WHERE genre_count > 0 
ORDER BY title, genre_id ASC;
