DROP TABLE IF EXISTS users;

CREATE TABLE users (
                              id INT AUTO_INCREMENT  PRIMARY KEY,
                              first_name VARCHAR(250) NOT NULL,
                              last_name VARCHAR(250) NOT NULL,
                              email VARCHAR(250) NOT NULL
);

INSERT INTO users (first_name, last_name, email) VALUES
('James', 'Smith', 'james.smith@jmail.com'),
('John', 'Doe', 'john.doe@jmail.com'),
('Claire', 'Pollock', 'claire.pollock@jmail.com');