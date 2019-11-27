-- Lists all shows containing at least one of the same genres
-- Displays NULL if none overlap
SELECT ts.title, tg.genre_id
FROM tv_shows as ts
LEFT JOIN tv_show_genres as tg
ON ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC
;
