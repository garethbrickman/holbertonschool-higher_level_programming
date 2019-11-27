-- Lists all shows containing at least one of the same genres
SELECT ts.title, tg.genre_id
FROM tv_shows as ts
INNER JOIN tv_show_genres as tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id
;
