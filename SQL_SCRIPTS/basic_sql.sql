USE traineeshipDB 
GO
--DDL statement
CREATE TABLE riya.table_person_test( ID int NOT NULL PRIMARY KEY,
Name NVARCHAR(50) NOT NULL ,
Email NVARCHAR(50) NOT NULL,
GenderID int )
GO

CREATE TABLE riya.table_gender( ID int NOT NULL PRIMARY KEY,
Gender nvarchar(50) NOT NULL );

SELECT
	*
FROM
	riya.table_person;

SELECT
	*
FROM
	riya.table_gender;

--Alter Table by Adding column 
ALTER TABLE riya.table_employee_record ADD Salary int;

ALTER TABLE riya.table_person ADD Age int;

--Alter Table by Dropping column 
ALTER TABLE riya.table_person Drop COLUMN Age;

----Alter Table by Adding column with a default value
ALTER TABLE riya.table_person ADD CONSTRAINT default_value_const DEFAULT 18 FOR Age;

--Drop the default constraint 
ALTER TABLE riya.table_gender DROP CONSTRAINT default_value_const;

--Default value of 18 is set when inserting a row.
INSERT INTO riya.table_person (ID, Name, Email, GenderID, Age) VALUES (6,'Nail', 'n@n.com', 1, 19);


--Adding a foreign key constraint  (In Person table Gender Id is the Foreign Key that points to Primary key for Gender Table)
ALTER TABLE riya.table_person ADD CONSTRAINT table_person_GenderID_FK FOREIGN KEY(GenderID) REFERENCES riya.table_gender(ID);


--Droping the foreign constraint(Same Method to delete all constraints)
ALTER TABLE riya.table_person DROP CONSTRAINT table_person_GenderID_FK;

--Adding a Unique constraint 
ALTER TABLE riya.table_gender ADD CONSTRAINT UC_Gender UNIQUE(Gender);

--Droping the Unique constraint
ALTER TABLE riya.table_gender DROP CONSTRAINT UC_Gender;


--Adding a Check Constraint
ALTER TABLE riya.table_person 
ADD CONSTRAINT Check_person_age CHECK (Age>=18); 

--Adding a Foreign Key constraint With a referential intergrity: SET Null, SET Defalut, Cascade:If the primary key pointing to foreign key is another table are deleted--> All the row with foreign values are set to null, default or deleted resp.
ALTER TABLE riya.table_person ADD CONSTRAINT fk_set_null_table_person FOREIGN KEY (GenderID) REFERENCES riya.table_gender(ID) ON
DELETE
	CASCADE ON
	UPDATE
	CASCADE;

ALTER TABLE riya.table_person DROP CONSTRAINT fk_set_null_table_person;


DELETE
	riya.table_gender
WHERE
	ID = 3;


-- Identity Columns (Auto Increment0) --> IDENTITY(1,1) = (Identity seed->start value, Identity Increment->increases by)

CREATE TABLE riya.sample_person( 
PersonID int IDENTITY(1,1) PRIMARY KEY, --personid AUTOINCREMENT PRIMARY KEY 
First_name nvarchar(50) NOT NULL,
Last_name nvarchar(50) NOT NULL );

INSERT INTO riya.sample_person VALUES ('Riya', 'Karanjit');
INSERT INTO riya.sample_person VALUES ('Ram', 'Krishna');
INSERT INTO riya.sample_person VALUES ('Hari', 'Lal');


SELECT * FROM riya.sample_person;

DELETE FROM riya.sample_person WHERE PersonID = 1;

INSERT INTO riya.sample_person VALUES ( 'Riya', 'Karanjit'); --Its inserted to next id

-- To insert the data to PersonID = 1 IDENTITY_INSERT ON and specify column list

SET IDENTITY_INSERT riya.sample_person ON ;

INSERT INTO riya.sample_person (PersonID, First_name, Last_name) VALUES (1, 'Ram', 'Hari');


-- If we delete the entire records from table the id starts from next id (PersonId=5), to start from id = 1:
DELETE FROM riya.sample_person; 
SET IDENTITY_INSERT riya.sample_person OFF ;


INSERT INTO riya.sample_person VALUES ( 'Riya', 'Karanjit'); 

DBCC CHECKIDENT(riya.sample_person, RESEED, 0); -- now id starts from 1


--SELECT STATEMENT 
SELECT Name, Age FROM riya.table_person tp ;

SELECT Name, Age FROM riya.table_person tp WHERE Id=2 AND Age >= 20;

SELECT DISTINCT Name, Age FROM riya.table_person tp ORDER BY Name, Age DESC ;

SELECT * FROM riya.table_person tp WHERE GenderID IS NULL ;

SELECT * FROM riya.table_person tp WHERE Name LIKE 'm%' ; -- starts with m
SELECT * FROM riya.table_person tp WHERE Name LIKE 'J_hn' ; 
SELECT * FROM riya.table_person tp WHERE Name LIKE '[JR]%' ; --start with J or R
SELECT * FROM riya.table_person tp WHERE Name LIKE '[^JR]%' ; -- doesnot start with J or R

 SELECT TOP 3 * FROM riya.table_person ; 
 SELECT TOP 50 PERCENT * FROM riya.table_person WHERE GenderID =1; 

--SELECT INTO --> copies data from one table into a new table.
DRop table riya.backup_table_person;
SELECT Name, Age INTO riya.backup_table_person FROM riya.table_person; --(USE IN To sepecify )

SELECT Count(Age), Name FROM riya.table_person tp GROUP BY Name ORDER BY 1 DESC; 


--Joins
SELECT
	Name,
	Age,
	tg.Gender
FROM
	riya.table_person tp
JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID
--WHERE
--	tg.Gender = "@Gender"
--	AND tp.Age >= @Age
ORDER BY tg.Gender;

--Left Join-- Returns all records from the left table, and the matched records from the right table 
SELECT
	*
FROM
	riya.table_person tp
LEFT JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID;

--Right join -- Returns all the record from the right table and the matched record from left table
SELECT
	*
FROM
	riya.table_person tp
RIGHT JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID;

--Full Join -- Returns all records when there is a match in either left or right table
SELECT
	*
FROM
	riya.table_person tp
FULL JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID;

CREATE TABLE riya.table_employee_record(EmployeeID int IDENTITY(1,1) PRIMARY KEY,
Name NVARCHAR(50) NOT NULL ,
ManagerID int );

--Changing the NOT NULL constraint to NULL
ALTER TABLE riya.table_employee_record ALTER COLUMN Name nvarchar(50) NULL;


INSERT INTO riya.table_employee_record VALUES ('Riya', 1);
INSERT INTO riya.table_employee_record VALUES ('Ram', 10);
INSERT INTO riya.table_employee_record (Name) VALUES ('Hari');


SELECT * FROM riya.table_employee_record;


--Different ways of replacing NULL
--ISNULL
SELECT
	EmployeeID,
	Name,
	ISNULL(ManagerID,
	0) AS ManagerID
FROM
	riya.table_employee_record;

ALTER TABLE riya.table_employee_record ADD Surname nvarchar(50);

--CASE statemnet
SELECT
	EmployeeID,
	Name,
	CASE
		WHEN ManagerID IS NULL THEN 0
		ELSE ManagerID
	END,
	CASE
		WHEN Department IS NULL THEN 'No Dept'
		ELSE Department
	END
FROM
	riya.table_employee_record ter ;


--COALESCE--> it returns us the first Not Null value.
SELECT
	EmployeeID,
	COALESCE(Name, Surname) AS Name,
	COALESCE(ManagerID,
	0) AS ManagerID,
	COALESCE(Department,
	'Not Assigned') AS Department,
FROM
	riya.table_employee_record;



-- Stored Procedure

CREATE PROCEDURE riya.SpGetRecords
AS
BEGIN
	SELECT
	Name,
	Age,
	tg.Gender
FROM
	riya.table_person tp
JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID
END ;

riya.spGetRecords;
EXECUTE riya.spGetRecords;

--Drop a procedure
DROP PROC SpGetRecords;
DROP PROC SpGetRecordswithGender;

--With parameters
CREATE PROCEDURE riya.SpGetRecordswithGender
@Gender nvarchar(20)
AS
BEGIN
	SELECT
	Name,
	Age,
	tg.Gender
FROM
	riya.table_person tp
JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID
WHERE tg.Gender = @Gender
END ;

EXEC riya.SpGetRecordswithGender 'Female' -- Positional Argument order is important if many argument present


EXEC sp_helptext riya.SpGetRecords;

CREATE PROCEDURE riya.SpGetRecordswithGender
@Gender nvarchar(20), @Age int
--WITH ENCRYPTION --This proc can't be view now.
AS
BEGIN
	SELECT
	Name,
	Age,
	tg.Gender
FROM
	riya.table_person tp
JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID
WHERE tg.Gender = @Gender AND tp.Age >= @Age
END ;
EXECUTE riya.SpGetRecordswithGender @Gender='Female',@Age=20; --Keyword Argument, Order is not necessary

--Alter Stored Procedure
ALTER PROCEDURE riya.SpGetRecordswithGender @Gender nvarchar(20),
@Age int AS BEGIN
SELECT
	Name,
	Age,
	tg.Gender
FROM
	riya.table_person tp
JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID
WHERE
	tg.Gender = @Gender
	AND tp.Age >= @Age
ORDER BY tg.Gender
END ;
EXECUTE riya.SpGetRecordswithGender @Gender='Female', @Age=18

--Stored Procedure with Output parameter
CREATE PROCEDURE riya.SpGetRecordswithGenderCount @Gender nvarchar(20),
@EmployeeCount int OUTPUT AS BEGIN
SELECT
	@EmployeeCount = COUNT(tp.ID) 
FROM
	riya.table_person tp
JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID
WHERE
	tg.Gender = @Gender
END ;

EXEC sp_helptext 'riya.SpGetRecordswithGender'


--Execute the stored Procedure with Output Parameter
DECLARE @EmployeeTotal int 
--EXECUTE riya.SpGetRecordswithGenderCount 'Male',@EmployeeTotal OUTPUT --If Output is not passed @EmployeeTotal is Null
EXECUTE riya.SpGetRecordswithGenderCount @Gender = 'Male',@EmployeeCount = @EmployeeTotal OUTPUT --kw arguments
IF (@EmployeeTotal IS NULL) 
	PRINT '@EmployeeTotal is Null'
ELSE 
	PRINT '@EmployeeTotal is Not Null is: ' 
	PRINT @EmployeeTotal
	
EXEC sp_help 'riya.SpGetRecordswithGenderCount'

EXEC sp_depends 'riya.SpGetRecordswithGenderCount'


-- Whenever you execute a stored procedure, it returns a integer status variable. 0=success and non-zero = failure
--Returns the total count of employee using an output parameter
CREATE PROC riya.spGetTotalCountofEmployees1
@TotalCount int OUTPUT 
AS BEGIN 
	SELECT @TotalCount = COUNT(ID) FROM riya.table_person tp 
END;

DECLARE @EmployeeTotalCount int 
EXECUTE riya.spGetTotalCountofEmployees1 @EmployeeTotalCount OUTPUT --kw arguments
SELECT @EmployeeTotalCount

--Returns the total count of employee using return 
CREATE PROC riya.spGetTotalCountofEmployees2
AS BEGIN 
	RETURN (SELECT COUNT(ID) FROM riya.table_person tp)
END;

DECLARE @EmployeeTotalCount int 
EXECUTE @EmployeeTotalCount = riya.spGetTotalCountofEmployees2 --the return must always be one value else error
SELECT @EmployeeTotalCount



--User Defined Functions(UDF)
--Scalar UDF = May or may not have parameters, but always returns a single scalar value of any data type except text, image, timestamp


DECLARE @DOB DATE DECLARE @Age INT SET
@DOB = '8/26/2021' 
SET @Age = DATEDIFF(YEAR, @DOB, GETDATE()) -
CASE
	WHEN (MONTH(@DOB) > MONTH(GETDATE()))
	OR (MONTH(@DOB) = MONTH(GETDATE()))
	AND (DAY(@DOB) > DAY(GETDATE())) THEN 1
	ELSE 0
END
SELECT
	@Age

CREATE FUNCTION riya.calculate_age(@DOB Date) RETURNS int
--WITH ENCRYPTION
 AS BEGIN DECLARE @Age INT SET
@Age = DATEDIFF(YEAR, @DOB, GETDATE()) -
CASE
	WHEN (MONTH(@DOB) > MONTH(GETDATE()))
	OR (MONTH(@DOB) = MONTH(GETDATE()))
	AND (DAY(@DOB) > DAY(GETDATE())) THEN 1
	ELSE 0
END RETURN @Age
END

--WITH SCHEMABINDING --Function is bound to the db objects that it references. The base object cannot be changed in any ways that affects the function definition. the function must be modified or dropped to remove the dependencies.

CREATE FUNCTION riya.getpersonbyID(@id int)
RETURNS nvarchar(50)
WITH SCHEMABINDING
AS BEGIN 
	RETURN (SELECT Name FROM riya.table_person tp WHERE id = @id)
END;

SELECT riya.getpersonbyID(1);

DROP TABLE riya.table_person ;

--Invoke the UDF
SELECT riya.calculate_age('8/26/2021')

SELECT * , riya.calculate_age(DOB) AS Age FROM riya.table_person tp WHERE riya.calculate_age(DOB) > 18;

EXEC sp_helptext 'riya.calculate_age'

--Drop UDF
DROP FUNCTION dbo.calculate_age

SELECT CHAR(65) AS CodeToCharacter; 

 SELECT CAST(25.65 AS int);  --converts a value (of any type) into a specified datatype

SELECT CAST('2017-08-25' AS datetime); 


--Deterministic Funtions -- Returns the same result any time they are called with the specific set if inputs and given the same state of database
-- Sqaure, Power, Sum, Avg, Count. All aggregate functions are deteministic.

--Non-Deterministic Funtions -- may return different result each time they are called with the specific set if inputs and given the same state of database
-- Current_timestamp, Getdate(), rand()-- becomes deterministic after giving seed value
SELECT GETDATE(); 


SELECT riya.calculate_age('1/1/2000');
sp_helptext 'riya.calculate_age';

--Temporary tables -- It get created in TempDB and are automatically deleted when they are no longer used. .

--Local temporary table -- #TableName is used. Its available only for the conncetion that has created the table and dropped if that connection is closed.
--If the temp table is created inside the stored procedure, it gets dropped automatically upon the completion of stored procedure execution.
--Each connection can have same local temp table name

CREATE TABLE #TempPersonTable ( PersonID int PRIMARY KEY IDENTITY(1,
1),
LastName varchar(255),
FirstName varchar(255),
City varchar(255) );

INSERT
	INTO
	#TempPersonTable
VALUES ( 'Watson',
'Juan',
'Cleveland'),
( 'Baker',
'Dwayne',
'Fort Wayne'),
( 'Walker',
'Eric',
'Tucson'),
( 'Peterson',
'Bob',
'Indianapolis');

SELECT
	*
FROM
	#TempPersontable;

--Check the existence of the temporary table by query.
SELECT name FROM tempdb..sysobjects WHERE name LIKE '#TempPersontable%'


--Global Temporary table -- ##TableName is used. Its available for all the conncetion of sql server and dropped only when the last connection referencing the table is destroyed.
--Each connection must have unique global temp table name. They donot have underscore with unique number suffix.
CREATE TABLE ##GlobaltempCustomers (CustomerId INT IDENTITY(1,1) PRIMARY KEY,
CustomerFullName VARCHAR(50),
EMail VARCHAR(50),
CustomerAddress VARCHAR(50),
Country VARCHAR(50));



--Indexes --Can help the query to find data quickly, improving the performance of query with right indexes. 
--If no indexes, the query engine checks every row from first to last in a table. This is Table Scan which is a bad approach.

--Creating Index -- salary index in ascending order each having there own row address is created.  
--SQL Server picks up the row address from the index and directly fetches the record from the table, rather than scanning each row.
CREATE INDEXIX_table_employeerecord_salary ON riya.table_employee_record (Salary ASC);

SELECT IX_table_employeerecord_salary;

sp_HelpIndex 'riya.table_employee_record';

drop index riya.table_employee_record.PK__table_em__7AD04FF18AC8807A ;


--Clustered Index : Determines the physical order of data in a table. Hence, a table can have only one clustered index. Primary create constraint creates clustered indexes automatically if no clustered index exists.

--First delete the primary key clusterred index than you can create.
CREATE CLUSTERED INDEX IX_table_employeerecord_salary_gender ON riya.table_employee_record (Salary ASC, Gender DESC);


--Non-Clustered Index : The data and indexes are stored in different places. The index will have pointers to the storage location of the data. Thats they can have multiple non clustered indexes.
CREATE NONCLUSTERED INDEX IX_table_employeerecord_name ON riya.table_employee_record (Name);

--UNIQUE index ensure the non duplicate values.
--By default when you create a table, the primary key is taken as clustered unique index. To create any other key, first drop that index and create a the unique clustered index as:
CREATE UNIQUE CLUSTERED INDEX IX_table_employeerecord_name_surname ON
tblEmployee(Name,
Surname)

--NONCLUSTERED UNIQUE INDEX
CREATE UNIQUE CLUSTERED INDEX IX_table_employeerecord_name_surname ON
tblEmployee(Name,
Surname)

--A unique index gets created behind the scenes  when you add a unique constraint.
ALTER TABLE tblEmployee 
ADD CONSTRAINT UQ_tblEmployee_City 
UNIQUE NONCLUSTERED (City)


--CTE
CREATE TABLE riya.table_manager
(
 ManagerID int Primary Key,
 ManagerName nvarchar(20)
);

Insert into riya.table_manager values (1,'Ram')
Insert into riya.table_manager values (2,'Shyam')
Insert into riya.table_manager values (3,'Hari')
Insert into riya.table_manager values (4,'Sita')


--Number of employees under resp managers
WITH EmployeeCountCte(ManagerID, TotalEmoplyees) AS
(SELECT 
ManagerID, COUNT(*) as TotalEmployees
 from riya.table_employee_record ter 
 group by ManagerID
)
SELECT ManagerName, ecc.TotalEmoplyees
FROM riya.table_manager tm
JOIN EmployeeCountCte ecc
ON tm.ManagerID = ecc.ManagerID;



---Window Functions
--The OVER clause combined with PARTITION BY is used to break up data into partitions. 
-- ORDER BY is optional. PARTITION BY is optional
SELECT Name, Salary, Gender, 
    Sum(Salary) OVER(PARTITION BY Department) AS TotalSal,
    AVG(Salary) OVER(PARTITION BY Department) AS AvgSal,
    MIN(Salary) OVER(PARTITION BY Department) AS MinSal,
    MAX(Salary) OVER(PARTITION BY Department) AS MaxSal
FROM riya.table_employee_record ter ;

--For each partition the row number is reset to 1.
--ROW_NUMBER
SELECT Name, Salary, Gender, 
ROW_NUMBER() Over(PARTITION BY Gender ORDER BY Gender asc) AS row_num
FROM riya.table_employee_record ter ;

--RANK: Rank function skips rankings if there is a tie where as Dense_Rank will not. If you have 5 rows with 2 rows of same rank:
--RANK() returns - 1, 1, 3, 4, 5
--DENSE_RANK returns - 1, 1, 2, 3, 4

SELECT Name, Salary, Gender, 
RANK () Over(ORDER BY Salary DESC) AS rank_num
FROM riya.table_employee_record ter ;

SELECT Name, Salary, Gender, 
RANK () Over(PARTITION BY Gender ORDER BY Salary DESC) AS rank_num
FROM riya.table_employee_record ter 
ORDER BY 


SELECT Name, Salary, Gender, 
DENSE_RANK () Over(ORDER BY Salary DESC) AS denserank_num
FROM riya.table_employee_record ter ;

SELECT Name, Salary, Gender, 
DENSE_RANK () Over(PARTITION BY Gender ORDER BY Salary DESC) AS rank_num
FROM riya.table_employee_record ter

--nth highest salary
--Rank: It will not return rows with second highest salary
WITH highest_salary_cte AS
(
    SELECT Salary, Gender,
           RANK() OVER (PARTITION  BY Gender ORDER BY Salary DESC) AS Salary_Rank
    FROM riya.table_employee_record ter 
)
SELECT TOP 1 Salary FROM highest_salary_cte WHERE Salary_Rank = 2 AND Gender = 'Female'

--Dense Rank: It will not return rows with second highest salary

WITH highest_salary_cte AS
(
    SELECT Salary, Gender,
           DENSE_RANK () OVER (PARTITION  BY Gender ORDER BY Salary DESC) AS Salary_Rank
    FROM riya.table_employee_record ter 
)
SELECT TOP 1 Salary FROM highest_salary_cte WHERE Salary_Rank = 2 AND Gender = 'Female'

 ---ROWNUMBER vs. RANK vs. DENSE_RANK
 SELECT Name, Salary, Gender,
ROW_NUMBER() OVER (ORDER BY Salary DESC) AS RowNumber, -- unique number for each row
RANK() OVER (ORDER BY Salary DESC) AS rankNumber,
DENSE_RANK() OVER (ORDER BY Salary DESC) AS DenseRank
FROM riya.table_employee_record ter ;


--Lead and Lag Function
--Lead: Access subsequent data along with current row data -- LEAD(Column_Name, Offset -- number of rows to lead or lag, Default_Value -- if number of rows to lead or lag goes beyong first or last row.) 
--Lag: Access previous data along with current row data

SELECT
	Name,
	Gender,
	Salary,
	LEAD(Salary,
	1,
	-1) OVER (
	ORDER BY Salary) AS lead,
	LAG(Salary,
	1,
	-1) OVER (
	ORDER BY Salary) AS Lag
FROM
	riya.table_employee_record;

SELECT
	Name,
	Gender,
	Salary,
	LEAD(Salary,
	1,
	-1) OVER ( PARTITION BY Gender
ORDER BY
	Salary) AS lead,
	LAG(Salary,
	1,
	-1) OVER ( PARTITION BY Gender
ORDER BY
	Salary) AS Lag
FROM
	riya.table_employee_record;


--FIRST_VALUE AND LAST_VALUE -- retrieves the first or last value from the specified column. 
--For last value rows or range is optional, but for it to work correctly you may have to explicitly specify value. 
--Its deafult value: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW:  range between unbounded preceeding and current row
-- RANGE BETWEEN UNBOUNDED PRECEDING AND  UNBOUNDED FOLLOWING: It's window starts at the first row and ends at the last row.
SELECT
	Name,
	Gender,
	Salary,
	FIRST_VALUE(Name) OVER (
ORDER BY
	Salary) AS first_value,
	LAST_VALUE(Name) OVER (
ORDER BY
	Salary RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_value
FROM
	riya.table_employee_record;

SELECT
	Name,
	Gender,
	Salary,
	FIRST_VALUE(Name) OVER ( PARTITION BY Gender
ORDER BY
	Salary) AS first_value,
	LAST_VALUE(Name) OVER ( PARTITION BY Gender
ORDER BY
	Salary RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_value
FROM
	riya.table_employee_record;

--Views: It is nothing more than a saved SQL Query. It can also be considered as a virtual table as the view itself doesnot store any data by default. 
--Table abstraction by row and column level security. Also, summarized data can be obtained.
CREATE VIEW riya.vwEmployeewithGender AS
SELECT
	Name,
	Age,
	tg.Gender
FROM
	riya.table_person tp
JOIN riya.table_gender tg ON
	tp.GenderID = tg.ID;

DROP VIEW vwEmployeewithGender;

SELECT * FROM riya.vwEmployeewithGender;

--Subqueries

Create Table riya.tblProducts
(
 [Id] int identity primary key,
 [Name] nvarchar(50),
 [Description] nvarchar(250)
);

Create Table riya.tblProductSales
(
 Id int primary key identity,
 ProductId int foreign key references riya.tblProducts(Id),
 UnitPrice int,
 QuantitySold int
);



Insert into riya.tblProducts values ('TV', '52 inch black color LCD TV');
Insert into riya.tblProducts values ('Laptop', 'Very thin black color acer laptop');
Insert into riya.tblProducts values ('Desktop', 'HP high performance desktop');

Insert into riya.tblProductSales values(3, 450, 5);
Insert into riya.tblProductSales values(2, 250, 7);
Insert into riya.tblProductSales values(3, 450, 4);
Insert into riya.tblProductSales values(3, 450, 9);

SELECT * FROM riya.tblProducts;
SELECT * FROM riya.tblProductSales;

	
SELECT
	*
FROM
	riya.tblProducts
WHERE
	Id NOT IN (
	SELECT
		DISTINCT ProductId
	FROM
		riya.tblProductSales);
	
SELECT Name,
(
SELECT
	SUM(QuantitySold)
FROM
	riya.tblProductSales tps
WHERE
	ProductId = tp.Id) AS TotalQuantity
FROM
riya.tblProducts tp
ORDER BY
Name;


--Merge: Allows us to perform Inserts, Updates and Deletes in one statement. 
--Source table: changes that needs to be applied to the Target Table. Target Table: Table that requires changes(insert, update, delete).
--In real time mostly performed are INSERTS and UPDATES, not DELETES.

CREATE TABLE riya.source_table_student( id int PRIMARY KEY,
Name nvarchar(50) );

INSERT
	INTO
	riya.source_table_student
VALUES (1,
'Mike');

INSERT
	INTO
	riya.source_table_student
VALUES (2,
'Sara');


CREATE TABLE riya.target_table_student( id int PRIMARY KEY,
Name nvarchar(50) );

INSERT
	INTO
	riya.target_table_student
VALUES (1,
'Mike M');

INSERT
	INTO
	riya.target_table_student
VALUES (3,
'John');

MERGE riya.target_table_student target
	USING riya.source_table_student src ON
target.id = src.id
WHEN MATCHED THEN 
UPDATE
SET
	target.Name = src.Name
	WHEN NOT MATCHED BY TARGET THEN
INSERT
	(id,
	Name)
VALUES (src.id,
src.Name)
WHEN NOT MATCHED BY SOURCE THEN
DELETE;

SELECT * FROM riya.target_table_student;


















