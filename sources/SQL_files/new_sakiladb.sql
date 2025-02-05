--------------------------------------------------------------------------------
-- Use the Sakila database for all operations.
--------------------------------------------------------------------------------
USE sakila;

--------------------------------------------------------------------------------
-- Section 1: Basic Queries
--------------------------------------------------------------------------------
-- Retrieve all customer details
SELECT * FROM customer LIMIT 10;

-- Retrieve specific columns from the customer table
SELECT customer_id, first_name, last_name, email FROM customer LIMIT 10;

-- Retrieve films released after 2005
SELECT title, release_year FROM film WHERE release_year > 2005;

--------------------------------------------------------------------------------
-- Section 2: Handling NULL Values
--------------------------------------------------------------------------------
-- Find customers whose email is missing
SELECT customer_id, first_name, last_name FROM customer WHERE email IS NULL;

-- Replace NULL values in email with 'Unknown'
SELECT customer_id, COALESCE(email, 'Unknown') AS email FROM customer;

-- Enforce NOT NULL constraint on email column
ALTER TABLE customer MODIFY email VARCHAR(50) NOT NULL;

--------------------------------------------------------------------------------
-- Section 3: Date Functions
--------------------------------------------------------------------------------
-- Get current date and time
SELECT NOW();

-- Extract year from rental date
SELECT rental_id, rental_date, YEAR(rental_date) AS rental_year FROM rental;

-- Calculate days since customer creation
SELECT customer_id, DATEDIFF(NOW(), create_date) AS days_active FROM customer;

-- Retrieve rentals made in the last 30 days
SELECT * FROM rental WHERE rental_date >= DATE_SUB(NOW(), INTERVAL 30 DAY);

--------------------------------------------------------------------------------
-- Section 4: Aggregation Functions
--------------------------------------------------------------------------------
-- Count total customers in the database
SELECT COUNT(*) AS total_customers FROM customer;

-- Get the highest rental rate of any film
SELECT MAX(rental_rate) AS highest_rental_rate FROM film;

-- Find the average length of films
SELECT AVG(length) AS average_length FROM film;

-- Calculate total revenue from payments
SELECT SUM(amount) AS total_revenue FROM payment;

-- Count number of films per category
SELECT c.name AS category, COUNT(f.film_id) AS total_films
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY total_films DESC;

--------------------------------------------------------------------------------
-- Section 5: Joins
--------------------------------------------------------------------------------
-- Retrieve rental details along with customer names
SELECT r.rental_id, c.first_name, c.last_name, r.rental_date
FROM rental r
INNER JOIN customer c ON r.customer_id = c.customer_id;

-- Find customers who have never rented a movie
SELECT c.customer_id, c.first_name, c.last_name, r.rental_id
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
WHERE r.rental_id IS NULL;

--------------------------------------------------------------------------------
-- Section 6: UNION & UNION ALL
--------------------------------------------------------------------------------
-- Combine first names of customers and staff (removes duplicates)
SELECT first_name FROM customer
UNION
SELECT first_name FROM staff;

-- Combine first names of customers and staff (includes duplicates)
SELECT first_name FROM customer
UNION ALL
SELECT first_name FROM staff;

--------------------------------------------------------------------------------
-- Section 7: Subqueries (SELECT in SELECT)
--------------------------------------------------------------------------------
-- Retrieve the most rented movie(s)
SELECT title FROM film
WHERE film_id = (SELECT film_id FROM rental GROUP BY film_id ORDER BY COUNT(*) DESC LIMIT 1);

-- Retrieve customers who spent above the average rental payment
SELECT customer_id, SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
HAVING total_spent > (SELECT AVG(amount) FROM payment);

-- Retrieve films with rental rates higher than the average
SELECT title, rental_rate FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

-- Find customers who have rented a film from the 'Action' category
SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM customer c
WHERE EXISTS (
    SELECT 1 FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film_category fc ON i.film_id = fc.film_id
    JOIN category cat ON fc.category_id = cat.category_id
    WHERE c.customer_id = r.customer_id AND cat.name = 'Action'
);

--------------------------------------------------------------------------------
-- Section 8: Advanced Use Cases
--------------------------------------------------------------------------------
-- Find the top 5 most rented movies
WITH MovieRentals AS (
    SELECT f.title, COUNT(r.rental_id) AS rental_count
    FROM film f
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    GROUP BY f.title
)
SELECT * FROM MovieRentals ORDER BY rental_count DESC LIMIT 5;

-- Rank customers by total rental payments
SELECT customer_id, SUM(amount) AS total_spent,
       RANK() OVER (ORDER BY SUM(amount) DESC) AS rank_position
FROM payment
GROUP BY customer_id;

--------------------------------------------------------------------------------
-- End of SQL Script
--------------------------------------------------------------------------------
