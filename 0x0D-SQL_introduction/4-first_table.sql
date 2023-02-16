-- Create a table called 'first_table in database
--  If the table 'first_table' already exists,
--  the script shouldn't fail
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
