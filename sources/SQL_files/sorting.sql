-- Use the world database for all operations.
USE world;

--------------------------------------------------------------------------------
-- 1. Basic Data Restriction using WHERE Clause
--------------------------------------------------------------------------------
SELECT Name, Population
FROM country
WHERE Population > 100000000;

--------------------------------------------------------------------------------
-- 2. Filtering with Comparison and Logical Operators
--------------------------------------------------------------------------------
-- Retrieve countries with population between 50 and 150 million.
SELECT Name, Population
FROM country
WHERE Population >= 50000000 AND Population <= 150000000;

-- Retrieve countries in Asia or Europe with population > 50 million.
SELECT Name, Continent, Population
FROM country
WHERE (Continent = 'Asia' OR Continent = 'Europe')
  AND Population > 50000000;

--------------------------------------------------------------------------------
-- 3. Demonstrating Operator Precedence with Parentheses
--------------------------------------------------------------------------------
-- Without parentheses: precedence might lead to unexpected results.
SELECT Name, Continent, Population
FROM country
WHERE Continent = 'Asia' OR Continent = 'Europe' AND Population > 50000000;

-- With parentheses: explicit grouping.
SELECT Name, Continent, Population
FROM country
WHERE (Continent = 'Asia' OR Continent = 'Europe')
  AND Population > 50000000;

--------------------------------------------------------------------------------
-- 4. Using Character String Literals in WHERE Clause
--------------------------------------------------------------------------------
-- Retrieve the country 'Canada'
SELECT Name, Continent, Population
FROM country
WHERE Name = 'Canada';

--------------------------------------------------------------------------------
-- 5. Sorting Data with ORDER BY
--------------------------------------------------------------------------------
-- Sorting by name in ascending order.
SELECT Name, Population
FROM country
ORDER BY Name ASC;

-- Sorting by population in descending order.
SELECT Name, Population
FROM country
ORDER BY Population DESC;

--------------------------------------------------------------------------------
-- End of Script
--------------------------------------------------------------------------------
