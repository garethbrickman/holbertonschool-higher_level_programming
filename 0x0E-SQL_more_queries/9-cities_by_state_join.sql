-- Lists all cities found in db and right joins their records to states
SELECT c.id, c.name, s.name
FROM cities AS c
RIGHT JOIN states AS s
ON s.id = c.state_id
ORDER BY c.id ASC
;
