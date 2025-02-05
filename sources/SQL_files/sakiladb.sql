--------------------------------------------------------------------------------
-- Use the Sakila database for all operations.
--------------------------------------------------------------------------------
USE sakila;

--------------------------------------------------------------------------------
-- Section 1: Retrieving Data Using SQL SELECT Statement
--------------------------------------------------------------------------------
-- 1.1 SQL SELECT Statement Capabilities
-- Retrieve all columns from the actor table.
SELECT * 
FROM actor
LIMIT 10;

-- Retrieve specific columns with aliasing and an arithmetic expression.
SELECT actor_id        AS ID, 
       first_name      AS FirstName, 
       last_name       AS LastName,
       (LENGTH(first_name) + LENGTH(last_name)) AS CombinedNameLength
FROM actor
LIMIT 10;

-- 1.2 Generating Data Reports
-- Report: Count the number of films per rating.
SELECT rating, COUNT(*) AS FilmCount
FROM film
GROUP BY rating;

-- 1.3 Selecting All Columns vs. Specific Columns
-- All columns (using *)
SELECT * FROM language LIMIT 5;
-- Specific columns with column heading defaults (or aliases).
SELECT language_id, name AS LanguageName
FROM language
LIMIT 5;

-- 1.4 Arithmetic Operators and Precedence
-- Calculate an adjusted rental rate and demonstrate operator precedence.
SELECT title, rental_rate,
       rental_rate + 1 * 2 AS WithoutParentheses,   -- Multiplication happens before addition.
       (rental_rate + 1) * 2 AS WithParentheses
FROM film
LIMIT 10;

--------------------------------------------------------------------------------
-- Section 2: Restricting and Sorting Data
--------------------------------------------------------------------------------
-- 2.1 Using WHERE Clause to Limit Data Retrieval
-- Retrieve films released after 2005.
SELECT title, release_year, rental_rate
FROM film
WHERE release_year > 2005;

-- 2.2 Comparison and Logical Operators in WHERE Clause
-- Retrieve films released after 2005 and in English.
SELECT title, release_year, rental_rate
FROM film
WHERE release_year > 2005 
  AND language_id = (SELECT language_id FROM language WHERE name = 'English');

-- 2.3 Rules of Precedence for Operators
-- Without parentheses: 'AND' is evaluated before 'OR'.
SELECT title, release_year, rental_rate
FROM film
WHERE release_year > 2005 OR language_id = (SELECT language_id FROM language WHERE name = 'English')
  AND rental_rate > 2.00;

-- With parentheses to group conditions explicitly.
SELECT title, release_year, rental_rate
FROM film
WHERE (release_year > 2005 OR language_id = (SELECT language_id FROM language WHERE name = 'English'))
  AND rental_rate > 2.00;

-- 2.4 Using Character String Literals in WHERE Clause
-- Retrieve actor with the first name 'PENELOPE'.
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'PENELOPE';

-- 2.5 Sorting Data Using ORDER BY Clause
-- Sort films by title in ascending order.
SELECT title, rental_rate
FROM film
ORDER BY title ASC;

-- Sort films by rental_rate in descending order.
SELECT title, rental_rate
FROM film
ORDER BY rental_rate DESC;

--------------------------------------------------------------------------------
-- Section 3: Single-Row Functions for Data Manipulation
--------------------------------------------------------------------------------
-- 3.1 Differences Between Single-Row and Multiple-Row Functions
-- Single-row functions operate on each row individually (e.g., UPPER); aggregate functions work over groups.
-- (See Section 4 for aggregate examples.)

-- 3.2 String Manipulation Functions (UPPER, LOWER, INITCAP)
-- Convert actor first names to uppercase and lowercase.
SELECT first_name, 
       UPPER(first_name) AS UpperCaseFirstName, 
       LOWER(first_name) AS LowerCaseFirstName
FROM actor
LIMIT 10;

-- Simulate INITCAP for a single word: capitalizing the first letter.
SELECT first_name,
       CONCAT(UPPER(LEFT(first_name, 1)), LOWER(SUBSTRING(first_name, 2))) AS InitCapFirstName
FROM actor
LIMIT 10;

-- 3.3 Numeric Functions (ROUND, TRUNCATE, MOD)
-- Round and truncate the rental_rate, and calculate a modulus.
SELECT title, rental_rate,
       ROUND(rental_rate, 1) AS RoundedRate,
       TRUNCATE(rental_rate, 1) AS TruncatedRate,
       MOD(rental_rate * 10, 3) AS RentalRateMod
FROM film
LIMIT 10;

-- 3.4 Date Functions (SYSDATE, TO_DATE, TO_CHAR equivalents)
-- In MySQL, use NOW() for current date and time.
SELECT NOW() AS CurrentDateTime;

-- Convert a string to a date using STR_TO_DATE (similar to Oracle's TO_DATE).
SELECT STR_TO_DATE('31-12-2022', '%d-%m-%Y') AS ConvertedDate;

-- Format the current date using DATE_FORMAT (similar to Oracle's TO_CHAR for dates).
SELECT DATE_FORMAT(NOW(), '%W, %M %d, %Y') AS FormattedDate;

--------------------------------------------------------------------------------
-- Section 4: Aggregate Functions and Grouping Data
--------------------------------------------------------------------------------
-- 4.1 Using COUNT, SUM, AVG, MAX, MIN Functions
-- Retrieve overall film statistics.
SELECT COUNT(*) AS TotalFilms,
       SUM(rental_rate) AS TotalRentalRate,
       AVG(rental_rate) AS AvgRentalRate,
       MAX(rental_rate) AS MaxRentalRate,
       MIN(rental_rate) AS MinRentalRate
FROM film;

-- 4.2 Grouping Data Using GROUP BY Clause
-- Count the number of films per rating.
SELECT rating, COUNT(*) AS FilmCount
FROM film
GROUP BY rating;

-- 4.3 Filtering Grouped Data Using HAVING Clause
-- Show ratings that have more than 10 films.
SELECT rating, COUNT(*) AS FilmCount
FROM film
GROUP BY rating
HAVING COUNT(*) > 10;

--------------------------------------------------------------------------------
-- Section 5: Joins & Subqueries
--------------------------------------------------------------------------------
-- 5.1 Using Joins to Retrieve Data from Multiple Tables
-- Inner Join: List film titles with their language names.
SELECT f.title, l.name AS Language
FROM film f
INNER JOIN language l ON f.language_id = l.language_id
LIMIT 10;

-- Outer Join (Left Join): Retrieve all films with their categories if available.
SELECT f.title, c.name AS Category
FROM film f
LEFT JOIN film_category fc ON f.film_id = fc.film_id
LEFT JOIN category c ON fc.category_id = c.category_id
LIMIT 10;

-- Cross Join: Combine actors and films (limited to 5 rows for demonstration).
SELECT a.first_name, a.last_name, f.title
FROM actor a
CROSS JOIN film f
LIMIT 5;

-- Self Join: Find pairs of films with the same rental rate.
SELECT a.title AS Film1, b.title AS Film2, a.rental_rate
FROM film a
JOIN film b ON a.rental_rate = b.rental_rate AND a.film_id <> b.film_id
LIMIT 10;

-- 5.2 Writing Subqueries to Solve Queries
-- Single-Row Subquery: Retrieve the film(s) with the maximum rental_rate.
SELECT title, rental_rate
FROM film
WHERE rental_rate = (SELECT MAX(rental_rate) FROM film);

-- Multiple-Row Subquery: Retrieve films with rental_rate above the average.
SELECT title, rental_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

-- Using IN: Retrieve films whose language is either 'English' or 'Italian'.
SELECT title, rental_rate
FROM film
WHERE language_id IN (
    SELECT language_id 
    FROM language 
    WHERE name IN ('English', 'Italian')
);

-- Using EXISTS: Retrieve categories that have films with a rental_rate greater than 3.00.
SELECT c.name AS Category
FROM category c
WHERE EXISTS (
  SELECT 1
  FROM film_category fc
  JOIN film f ON fc.film_id = f.film_id
  WHERE fc.category_id = c.category_id AND f.rental_rate > 3.00
);

-- Using ALL: Retrieve films whose rental_rate is greater than every film in the 'Action' category.
SELECT title, rental_rate
FROM film
WHERE rental_rate > ALL (
    SELECT f2.rental_rate
    FROM film f2
    JOIN film_category fc2 ON f2.film_id = fc2.film_id
    JOIN category c2 ON fc2.category_id = c2.category_id
    WHERE c2.name = 'Action'
)
LIMIT 10;


-- Sakila SQL Training - Aggregation, Joins, UNION, NULL Handling, and Date Functions

-- 1. Aggregation Functions
SELECT COUNT(*) AS total_customers FROM customer;
SELECT MAX(rental_rate) AS highest_rental_rate FROM film;
SELECT AVG(length) AS average_length FROM film;
SELECT SUM(amount) AS total_revenue FROM payment;
SELECT c.name AS category, COUNT(f.film_id) AS total_films
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY total_films DESC;

-- 2. Joins
SELECT r.rental_id, c.first_name, c.last_name, r.rental_date
FROM rental r
INNER JOIN customer c ON r.customer_id = c.customer_id;
SELECT c.customer_id, c.first_name, c.last_name, r.rental_id
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
WHERE r.rental_id IS NULL;

-- 3. UNION & UNION ALL
SELECT first_name FROM customer
UNION
SELECT first_name FROM staff;
SELECT first_name FROM customer
UNION ALL
SELECT first_name FROM staff;

-- 4. Handling NULL Values
SELECT customer_id, first_name, last_name FROM customer WHERE email IS NULL;
SELECT customer_id, COALESCE(email, 'Unknown') AS email FROM customer;
ALTER TABLE customer MODIFY email VARCHAR(50) NOT NULL;

-- 5. Date Functions
SELECT NOW();
SELECT rental_id, rental_date, YEAR(rental_date) AS rental_year FROM rental;
SELECT customer_id, DATEDIFF(NOW(), create_date) AS days_active FROM customer;
SELECT * FROM rental WHERE rental_date >= DATE_SUB(NOW(), INTERVAL 30 DAY);

-- 6. Advanced Use Cases
WITH MovieRentals AS (
    SELECT f.title, COUNT(r.rental_id) AS rental_count
    FROM film f
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    GROUP BY f.title
)
SELECT * FROM MovieRentals ORDER BY rental_count DESC LIMIT 5;

SELECT customer_id, SUM(amount) AS total_spent,
       RANK() OVER (ORDER BY SUM(amount) DESC) AS rank_position
FROM payment
GROUP BY customer_id;


--------------------------------------------------------------------------------
-- End of SQL Script
--------------------------------------------------------------------------------
