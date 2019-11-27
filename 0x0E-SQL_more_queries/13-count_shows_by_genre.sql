-- Lists all genres with number of shows in each
SELECT t.name as genre, COUNT(g.genre_id) AS number_of_shows FROM tv_genres t
INNER JOIN tv_show_genres g
ON t.id = g.genre_id
ON g.show_id = s.id
INNER JOIN tv_shows s
ON g.show_id = s.id
GROUP BY genre
ORDER BY number_of_shows DESC
;
