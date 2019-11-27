-- Lists top 3 max temps in cities
SELECT state, max(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state ASC LIMIT 3;
