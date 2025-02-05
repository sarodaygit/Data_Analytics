-- Use the world database for all subsequent operations.
USE world;

--------------------------------------------------------------------------------
-- 1. Retrieving Data Using SQL SELECT Statement
--------------------------------------------------------------------------------

-- a. Selecting all columns from the country table
SELECT * FROM country;

-- b. Selecting specific columns: Name and Population
SELECT Name, Population FROM country;

--------------------------------------------------------------------------------
-- 2. Generating Data Reports with Aggregate Functions and Grouping
--------------------------------------------------------------------------------

-- Report: Count the number of countries per continent.
SELECT Continent, COUNT(*) AS NumberOfCountries
FROM country
GROUP BY Continent;

-- Report: Average population per continent (ordered descending).
SELECT Continent, AVG(Population) AS AveragePopulation
FROM country
GROUP BY Continent
ORDER BY AveragePopulation DESC;

--------------------------------------------------------------------------------
-- 3. Using Column Heading Defaults and Aliases
--------------------------------------------------------------------------------

-- The following query uses default column headings.
SELECT Name, Population FROM country
WHERE Population > 50000000;

-- This query uses aliases to provide more descriptive column headings.
SELECT Name AS CountryName, Population AS TotalPopulation
FROM country
WHERE Population > 50000000
ORDER BY TotalPopulation DESC;

--------------------------------------------------------------------------------
-- 4. Arithmetic Operators and Operator Precedence
--------------------------------------------------------------------------------

-- Calculate 5% of the population for each country.
SELECT Name, Population, Population * 0.05 AS FivePercentPopulation
FROM country;

-- Demonstrate operator precedence:
-- Without parentheses: multiplication occurs before addition.
SELECT Name, Population,
       Population + 1000 * 2 AS WithoutParentheses,
       (Population + 1000) * 2 AS WithParentheses
FROM country;

--------------------------------------------------------------------------------
-- 5. Using the DESCRIBE Command to View Table Structure
--------------------------------------------------------------------------------

-- Display the structure of the "country" table.
DESCRIBE country;

--------------------------------------------------------------------------------
-- 6. Advanced Example: Joining Tables and Subqueries
--------------------------------------------------------------------------------

-- Example: For each country, count the number of cities.
-- This assumes a join between the 'country' and 'city' tables.
SELECT c.Name AS CountryName, COUNT(ci.ID) AS NumberOfCities
FROM country c
JOIN city ci ON c.Code = ci.CountryCode
GROUP BY c.Code
ORDER BY NumberOfCities DESC;

--------------------------------------------------------------------------------
-- End of SQL Script
--------------------------------------------------------------------------------
