-- Creates the table id_not_null on MySQL server with `id` and `name`.
-- id must be not NULL (default value = 1).
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
