-- Lists top 3 avg temps in cities in Jul, Aug
SELECT city, avg(value) as avg_temp FROM temperatures WHERE (month = 7 OR month = 8)
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
