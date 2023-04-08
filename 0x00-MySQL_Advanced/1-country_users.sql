-- script creates a new user table with the unique constraint
-- uses ENUM to set a default column strings

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255),
    `country` ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
