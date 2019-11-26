-- Lists records with s
SELECT score, COUNT(*) 'number'
FROM second_table
WHERE score = score
GROUP BY score
ORDER BY COUNT(*) DESC;
