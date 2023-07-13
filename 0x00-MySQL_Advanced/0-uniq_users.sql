-- a  SQL script that creates a tabel users
CREATE TABLE IF NOT EXISTS users(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
);
