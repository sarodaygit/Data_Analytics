--------------------------------------------------------------------------------
-- Use the Sakila database for all operations.
--------------------------------------------------------------------------------
USE sakila;

--------------------------------------------------------------------------------
-- SECTION 1: Data Manipulation Language (DML)
--------------------------------------------------------------------------------
-- For these examples, we create a separate table to safely practice INSERT, UPDATE,
-- DELETE, and transaction controls without affecting Sakila’s sample data.

-- Drop the table if it already exists.
DROP TABLE IF EXISTS training_dml;

-- Create a table for DML examples.
CREATE TABLE training_dml (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    value DECIMAL(10,2) NOT NULL
) ENGINE=InnoDB;

-- Inserting Data: Add new rows using the INSERT statement.
INSERT INTO training_dml (description, value) VALUES ('Initial Insert', 100.00);
INSERT INTO training_dml (description, value) VALUES ('Second Insert', 200.00);

-- Begin a transaction to demonstrate UPDATE, SAVEPOINT, and ROLLBACK.
START TRANSACTION;
    -- Insert a new record.
    INSERT INTO training_dml (description, value) VALUES ('Transaction Insert', 300.00);
    -- Set a savepoint after the insert.
    SAVEPOINT sp_after_insert;
    -- Update the inserted record.
    UPDATE training_dml 
    SET value = 350.00 
    WHERE description = 'Transaction Insert';
    -- Roll back to the savepoint to undo the update (the inserted row remains at its original value).
    ROLLBACK TO SAVEPOINT sp_after_insert;
    -- Commit the transaction.
COMMIT;

-- Update Statement Example: Increase the value of the 'Initial Insert' row.
UPDATE training_dml
SET value = value + 50
WHERE description = 'Initial Insert';

-- Delete Statement Example: Remove the row with 'Second Insert'.
DELETE FROM training_dml
WHERE description = 'Second Insert';

-- View the current state of the training_dml table.
SELECT * FROM training_dml;

--------------------------------------------------------------------------------
-- SECTION 2: Data Definition Language (DDL) - Creating and Managing Tables
--------------------------------------------------------------------------------
-- Overview: DDL involves creating, modifying, and dropping database objects.

-- Drop the training_ddl table if it exists.
DROP TABLE IF EXISTS training_ddl;

-- Creating a Table with Columns and Constraints:
CREATE TABLE training_ddl (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Primary key for the table',
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 0),         -- Check constraint (supported in MySQL 8.0+)
    email VARCHAR(100) UNIQUE,          -- Unique constraint to prevent duplicate emails.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB COMMENT='A table for DDL training examples';

-- Modifying the Table:
-- 1. Add a new column 'status' with a default value.
ALTER TABLE training_ddl
ADD COLUMN status VARCHAR(20) DEFAULT 'active' AFTER email;

-- 2. Modify the 'age' column to use a smaller integer type.
ALTER TABLE training_ddl
MODIFY COLUMN age SMALLINT;

-- 3. Drop the 'status' column.
ALTER TABLE training_ddl
DROP COLUMN status;

-- Managing Indexes:
-- Create an index on the email column.
CREATE INDEX idx_email ON training_ddl (email);

-- Drop the index.
DROP INDEX idx_email ON training_ddl;

--------------------------------------------------------------------------------
-- SECTION 3: Advanced SQL - Working with Data Dictionary Views
--------------------------------------------------------------------------------
-- MySQL provides metadata about database objects via the INFORMATION_SCHEMA.
-- Example: List all tables in the current (sakila) database.
SELECT TABLE_NAME, TABLE_TYPE
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'sakila';

-- Example: List columns, their data types, and nullability for the 'film' table.
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'sakila'
  AND TABLE_NAME = 'film';

-- Example: List foreign key constraints for tables in the Sakila database.
SELECT CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'sakila'
  AND REFERENCED_TABLE_NAME IS NOT NULL;

--------------------------------------------------------------------------------
-- SECTION 4: Managing Schema Objects
--------------------------------------------------------------------------------
-- Demonstrating common schema management tasks on existing tables.

-- 4.1 Adding, Modifying, and Dropping Columns:
-- For demonstration, add a temporary column to the 'film' table.
ALTER TABLE film
ADD COLUMN demo_column VARCHAR(50) DEFAULT 'demo';

-- Modify the new column's default value.
ALTER TABLE film
MODIFY COLUMN demo_column VARCHAR(50) DEFAULT 'updated_demo';

-- Drop the temporary column.
ALTER TABLE film
DROP COLUMN demo_column;

-- 4.2 Enabling and Disabling Constraints:
-- MySQL does not support directly disabling constraints.
-- To "disable" a foreign key constraint, you would drop it and later re-create it.
-- Example (for demonstration only; ensure you know the constraint name before dropping):
-- SELECT CONSTRAINT_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
--    WHERE TABLE_NAME = 'film_category' AND REFERENCED_TABLE_NAME IS NOT NULL;
-- Suppose the constraint name is 'fk_film_category_film', then:
-- ALTER TABLE film_category DROP FOREIGN KEY fk_film_category_film;
-- Later, re-create the constraint:
-- ALTER TABLE film_category
-- ADD CONSTRAINT fk_film_category_film FOREIGN KEY (film_id) REFERENCES film(film_id);

-- 4.3 Creating and Removing Indexes:
-- (See Section 2 above for index creation and removal examples.)

-- 4.4 Performing Flashback Operations:
-- Flashback features are specific to Oracle and are not available in MySQL.
-- In MySQL, similar outcomes can be achieved using backups or point-in-time recovery,
-- but there is no direct SQL command for a flashback operation.

--------------------------------------------------------------------------------
-- End of SQL Script
--------------------------------------------------------------------------------
