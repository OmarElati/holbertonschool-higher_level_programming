--
SELECT t.title, SUM(r.rate) AS rating
FROM tv_shows t
JOIN tv_show_ratings r ON t.id = r.show_id
GROUP BY t.title
ORDER BY rating DESC;
