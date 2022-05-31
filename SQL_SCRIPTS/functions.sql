
----------------STRING FUNTIONS-------------------------------------------------------

--ASCII -- returns the ascii values of the first character of column value
 SELECT
	ASCII(Name) NumberCodeofFirstChar
FROM
	riya.table_employee_record ter ;
-- CHAR -- Convert ascii value to character (0-255)
 SELECT
	CHAR(65) char_65,
	CHAR(90) char_90;
--LTRIM , RTRIM-- removes leading spaces from a string from left and right resp.
 SELECT
	RTRIM('Hello  ') ,
	LTRIM('    World');
--LOWER, UPPER -- Changing the case to lowercase or uppercase
 SELECT
	LOWER('Hello World') AS lower_case,
	UPPER('Hello World') AS upper_case;
--LEFT, RIGHT -- Extract 5 strings from left or right
 SELECT
	LEFT('Hello World',
	5) ,
	RIGHT('Hello World',
	5);
-- CHARINDEX -- it searches for a substring in a string, and returns the position, if substring not found returns 0 

--(substring, string, position where search will start--optional)
 SELECT
	CHARINDEX('World',
	'Hello World'),
	CHARINDEX('World',
	'Hello World',
	8)
--CONCAT --max of 254 inputs
 SELECT
	CONCAT('Hello', ' World', ' Here I am.');
--CONCAT_WS -- concat with separator
 SELECT
	CONCAT_WS('-',
	'United States',
	'New York',
	'Europe');
--REVERSE --returns the reverse order of that string
 SELECT
	REVERSE('ecnalubma') reversed;
--REPLICATE
 SELECT
	REPLICATE('hi ',
	3) Replicated;
--REPLACE -->REPLACE(input_string, substring to be replaced, new_substring); 
 SELECT
	REPLACE( 'Good Morning', 'Morning', 'Evening' ) replaced;
--PATINDEX --PATINDEX ( '%pattern%' (wildcard char) , input_string ) --position of the first occurrence of a pattern in a string
 SELECT
	PATINDEX('%ern%',
	'SQL Pattern Index') POSITION;
--LEN --length of a string (counts leading spaces, but not trailing spaces)
 SELECT
	LEN(' Hello_WORLD ');

SELECT
	LEN('2017-08');
--STUFF --deletes a part of a string and then inserts a substring into the string, beginning at a specified position

--STUFF ( input_string , start_position for delete and insert , length to delete , replace_with_substring )
 SELECT
	STUFF('SQL Tutorial',
	1 ,
	3,
	'SQL Server') RESULT;
--SUBSTRING -- extracts a substring with a specified length starting from a location in an input string

--SUBSTRING(input_string, start, length);
 SELECT
	SUBSTRING('SQL Server SUBSTRING', 5, 6) sunstringed;
--SPACE -- returns a string of repeated spaces SPACE(count)
 SELECT
	'John' + SPACE(1) + 'Doe' full_name;
----------------DATE FUNTIONS-------------------------------------------------------

--DAY
 SELECT
	DAY('2017/08/13 09:08') AS DayOfMonth;

SELECT
	--Returns 1 if time only specified
 DAY('10:20:30');
--MONTH
 SELECT
	MONTH('2017/08/25') AS MONTH;
--YEAR
 SELECT
	YEAR('2019-02-01');
--DATEPART --DATEPART ( date_part , input_date )
 DECLARE @d DATETIME = '2019-01-01 14:30:14';

SELECT
	DATEPART(YEAR, @d) YEAR,
	DATEPART(quarter, @d) quarter,
	DATEPART(MONTH, @d) MONTH,
	DATEPART(DAY, @d) DAY,
	DATEPART(HOUR, @d) HOUR,
	DATEPART(MINUTE, @d) MINUTE,
	DATEPART(SECOND, @d) SECOND;
--DATENAME -- returns a specified part if date. For year(year, yyy, yy), Minute(minute, mi, n), etc
 SELECT
	DATENAME(yyyy, '2017/08/25') AS YEAR,
	DATENAME(n, '2017/08/25 08:36') AS MINUTE;
--DATEFDIFF --difference between two dates in years, months, weeks.
--DATEDIFF( date_part that you wan to compare , start_date , end_date)
 DECLARE @start_dt DATETIME2 = '2019-12-31 23:59:59.9998888',
@end_dt DATETIME2 = '2020-01-20 00:00:00.0000000';

SELECT
	DATEDIFF(YEAR, @start_dt, @end_dt) diff_in_year,
	DATEDIFF(quarter, @start_dt, @end_dt) diff_in_quarter,
	DATEDIFF(MONTH, @start_dt, @end_dt) diff_in_month,
	DATEDIFF(dayofyear, @start_dt, @end_dt) diff_in_dayofyear,
	DATEDIFF(DAY, @start_dt, @end_dt) diff_in_day,
	DATEDIFF(week, @start_dt, @end_dt) diff_in_week,
	DATEDIFF(HOUR, @start_dt, @end_dt) diff_in_hour,
	DATEDIFF(MINUTE, @start_dt, @end_dt) diff_in_minute,
	DATEDIFF(SECOND, @start_dt, @end_dt) diff_in_second,
	DATEDIFF(millisecond, @start_dt, @end_dt) diff_in_millisecond;
--DATEADD -- adds a number to a specified date part of an input date

--DATEADD (date_part , value , input_date ) 
 SELECT
	DATEADD(SECOND, 1, '2018-12-31 23:50:30') RESULT;

SELECT
	DATEADD(DAY, 1, '2018-12-31 23:59:59') RESULT;
----------------MATH FUNTIONS-------------------------------------------------------

--ABS
 SELECT
	ABS(-243.5);
--CEILING --return the smallest integer value that is not smaller than X
 SELECT
	CEILING(25.75),
	CEILING (-6.56);
--POWER
 SELECT
	POWER(3, 3);
--ROUND
 SELECT
	ROUND(5.693893, 2);
--RAND -- returns a random number between 0 (inclusive) and 1 (exclusive)
 SELECT
	RAND(3);
--FLOOR --return the largest integer value that is not greater than X
 SELECT
	FLOOR(25.75) AS FloorValue;
--SQUARE
 SELECT
	SQUARE(64);
--SQRT
 SELECT
	SQRT(49);
