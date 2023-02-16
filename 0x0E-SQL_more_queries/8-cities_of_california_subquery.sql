-- lists all the cities of 'California'
-- The states table contains only one record
-- where 'name' = 'California'
-- Results sorted in ascending order by 'cities.id'
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
);
