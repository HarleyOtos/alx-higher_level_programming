-- lists the number of records with the same score in
-- the table 'second_table'
-- The result should display the 'score' and number of
-- records for this 'score' with the label 'number'.
SELECT score, COUNT(`score`) as number
FROM second_table GROUP BY score ORDER BY score DESC;
