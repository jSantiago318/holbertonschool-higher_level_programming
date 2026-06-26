-- Lists records of second_table with a non-empty name, by descending score
SELECT score, name FROM second_table WHERE name <> '' ORDER BY score DESC;
