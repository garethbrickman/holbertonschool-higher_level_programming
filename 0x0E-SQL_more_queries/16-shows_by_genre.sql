-- Lists all genres linked with shows
SELECT ts.title, tv_genres.name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres
ON ts.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
ORDER BY ts.title, tv_genres.name
;
