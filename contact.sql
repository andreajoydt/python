DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name TEXT,
    contact TEXT
);

INSERT INTO contacts (name, contact)
VALUES ('ivan marie', '09396203319');
