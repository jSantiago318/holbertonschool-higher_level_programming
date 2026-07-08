-- Creates the table unique_id (if missing) with a unique id defaulting to 1
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
