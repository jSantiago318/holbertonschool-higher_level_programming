-- Creates the table force_name (if missing) with a non-nullable name column
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
