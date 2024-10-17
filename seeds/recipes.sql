DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    average_cooking_time int,
    rating int
);

INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Recipe 1', 10, 1);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Recipe 2', 20, 2);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Recipe 3', 30, 3);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Recipe 4', 40, 4);
INSERT INTO recipes (name, average_cooking_time, rating) VALUES ('Recipe 5', 60, 5);