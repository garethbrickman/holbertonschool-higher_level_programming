-- Lists all shows containing at least one of the same genres
SELECT ts.title, tv_show_genres.genre_id
FROM tv_shows as ts
INNER JOIN tv_show_genres
ON ts.id = tv_show_genres.show_id
ORDER BY ts.title ASC, tv_show_genres.genre_id ASC
;
