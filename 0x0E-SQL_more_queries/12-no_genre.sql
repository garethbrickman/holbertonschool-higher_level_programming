-- Lists all shows without at least one of the same genres
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres as tg
ON ts.id = tg.show_id
WHERE tg.show_id IS NULL
ORDER BY ts.title ASC, tg.genre_id ASC
;
