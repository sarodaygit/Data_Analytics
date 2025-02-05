-- Use the world database for all operations.
USE world;

--------------------------------------------------------------------------------
-- 1. String Manipulation Examples
--------------------------------------------------------------------------------

-- Convert country names to uppercase.
SELECT Name, UPPER(Name) AS UpperCaseName
FROM country
LIMIT 5;

-- Convert country names to lowercase.
SELECT Name, LOWER(Name) AS LowerCaseName
FROM country
LIMIT 5;

-- Simulate INITCAP for a single word (for demonstration).
SELECT Name, 
       CONCAT(UPPER(SUBSTRING(Name, 1, 1)), LOWER(SUBSTRING(Name, 2))) AS InitCapName
FROM country
LIMIT 5;

--------------------------------------------------------------------------------
-- 2. Numeric Function Examples
--------------------------------------------------------------------------------

-- Round a numeric literal.
SELECT 123.456 AS Original, ROUND(123.456, 2) AS RoundedValue;

-- Truncate a numeric literal.
SELECT 123.456 AS Original, TRUNCATE(123.456, 2) AS TruncatedValue;

-- Modulo operation example.
SELECT MOD(10, 3) AS Remainder;

--------------------------------------------------------------------------------
-- 3. Date Function Examples
--------------------------------------------------------------------------------

-- Display the current date and time.
SELECT NOW() AS CurrentDateTime;

-- Convert a string to a date using STR_TO_DATE.
SELECT STR_TO_DATE('31-12-2022', '%d-%m-%Y') AS ConvertedDate;

-- Format the current date using DATE_FORMAT.
SELECT DATE_FORMAT(NOW(), '%W, %M %d, %Y') AS FormattedDate;

--------------------------------------------------------------------------------
-- End of Script
--------------------------------------------------------------------------------
