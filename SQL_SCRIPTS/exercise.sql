---Date Formats
DECLARE @Existingdate DATE = GETDATE();  
Select CONVERT(varchar,@Existingdate,1) as [MM/DD/YY], CONVERT(varchar,@Existingdate,2) as [YY.MM.DD], CONVERT(varchar,@Existingdate,3) as [DD/MM/YY], CONVERT(varchar,@Existingdate,4) as [DD.MM.YY], CONVERT(varchar,@Existingdate,5) as [DD-MM-YY];

--min, max, avg and sum of salary for each department
SELECT Department, MIN(Salary) Min_Salary, MAX(Salary) Max_Salary, AVG(Salary) Avg_Salary,  SUM(Salary) Sum_Salary
FROM riya.table_employee_record  ter
GROUP BY Department;


----
CREATE TABLE riya.table_salary_entry( Name nvarchar(10) NOT NULL,
Salary int NOT NULL );

INSERT
	INTO
	riya.table_salary_entry
VALUES('A',
20000);

INSERT
	INTO
	riya.table_salary_entry
VALUES('B',
20000),
('C',
34000),
('D',
90000),
('E',
45000),
('F',
60000),
('G',
87000),
('A',
24000),
('D',
90000);

-- Find all employees having duplicate entries 
SELECT * FROM riya.table_salary_entry tse ;

SELECT
	Name,
	Salary,
	COUNT(*)
FROM
	riya.table_salary_entry
GROUP BY
	Name,
	Salary
HAVING
	COUNT(*)>1;

---Alternate
SELECT
	* ,
	ROW_NUMBER() OVER ( PARTITION BY Name,
	Salary
ORDER BY
	Name) AS row_num
FROM
	riya.table_salary_entry
WHERE
	row_num > 1;
--
WITH delete_entry_cte AS(
SELECT
	* ,
	ROW_NUMBER() OVER ( PARTITION BY Name,
	Salary
ORDER BY
	Name) AS row_num
FROM
	riya.table_salary_entry
) DELETE FROM delete_entry_cte WHERE row_num > 1;

SELECT 
	*
FROM
	riya.table_salary_entry;
---
SELECT * FROM riya.table_employee_record ter ;

--nth highest salary employee in each department
SELECT Department, Name, Salary, 
ROW_NUMBER() OVER(PARTITION BY Department ORDER BY Salary Desc) AS seq
FROM riya.table_employee_record;

--nth highest salary ALternate solution
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


--employees with salary more than their managers salary: using self join
SELECT employee.*
FROM riya.table_employee_record AS employee
JOIN riya.table_employee_record AS manager ON manager.EmployeeID = employee.ManagerID 
WHERE employee.Salary > manager.Salary ;


--Swap Gender 
SELECT * FROM riya.table_employee_record ter ;


UPDATE
	riya.table_employee_record
SET
	Gender = (
	CASE
		WHEN Gender = 'Male' THEN 'Female'
		WHEN Gender = 'Female' THEN 'Male'
		ELSE 'Unknown'
	END );

SELECT * FROM riya.table_employee_record ter ;

--Stored Procedure with Gender as Parameter;
EXEC sp_helptext 'riya.SpGetRecordswithGender';

EXECUTE riya.SpGetRecordswithGender @Gender='Female', @Age=18

---SQL query to generate level of hierarchy

CREATE TABLE riya.table_generate_hierarchy(
ID int IDENTITY(1,1) PRIMARY KEY,
Name nvarchar(50) NOT NULL,
MgrID int,
LEVEL int NOT NULL,
);

SELECT * FROM riya.table_generate_hierarchy;

SELECT
	employee.*
FROM
	riya.table_generate_hierarchy AS employee
JOIN riya.table_generate_hierarchy AS manager ON
	manager.ID = employee.MgrID
ORDER BY
	employee.level;


---Insert and Update Trigger
CREATE TABLE riya.AuditDataEmployeeRecord(
ID int IDENTITY(1,1) PRIMARY KEY,
AuditData nvarchar(150) 
);


--Insert
CREATE TRIGGER tr_employeerecord_forInsert ON
riya.table_employee_record FOR
INSERT
	AS BEGIN DECLARE @ID int
SELECT
	@ID =EmployeeID
FROM
	inserted --The magic table available only in the context of triggers in sql server which retains the copy of the row that you have inserted on the specified table. The insert statement after which this event is triggered
INSERT
	INTO
	riya.AuditDataEmployeeRecord
VALUES ('New Employee with EmployeeID = ' + CAST(@ID AS nvarchar(5)) + 'is added at ' + CAST(getdate() AS nvarchar(20)) )
END

INSERT INTO riya.table_employee_record VALUES ('Phoebe', 4, 'Electronics', 'Buffay', 'Female', 80000);


SELECT * FROM riya.AuditDataEmployeeRecord;

--Delete
DROP trigger riya.tr_employeerecord_forDelete;

Create TRIGGER tr_employeerecord_forDelete ON
riya.table_employee_record FOR
DELETE 
	AS BEGIN DECLARE @ID int
SELECT
	@ID =EmployeeID
FROM
	deleted --The magic table available only in the context of triggers in sql server which retains the copy of the row that you have inserted on the specified table. The insert statement after which this event is triggered
INSERT
	INTO
	riya.AuditDataEmployeeRecord
VALUES ('An existing employee with EmployeeID = ' + CAST(@ID AS nvarchar(5)) + 'is deleted at ' + CAST(getdate() AS nvarchar(20)) )
END;


DELETE FROM riya.table_employee_record WHERE EmployeeID=12;


--Count(*) VS Count(1) --> They are exactly the same.
--The COUNT(*) function counts the total rows in the table, including the NULL values
--COUNT(1) assigns the value from the parentheses (i.e 1) to every row in the table, then the same function counts how many times the value in the parenthesis (1) has been assigned. Hence, this will always be equal to the number of rows in the table
SELECT COUNT(*) FROM riya.table_employee_record ter ;
SELECT COUNT(1) FROM riya.table_employee_record ter ;
SELECT COUNT(-10) FROM riya.table_employee_record ter ;
SELECT COUNT('This will have 10 rows') FROM riya.table_employee_record ter ;


--COUNT(column name): It will count all the rows in the specified column while excluding NULL values
SELECT COUNT(Surname) FROM riya.table_employee_record ter ;



---DELETE VS DROP VS TRUNCATE 
--DELETE : DML command removes some or all records from a table. it does not remove the table or its structure from the database. Where clause can be applied. Can be rolled back.
DELETE FROM riya.backup_table_person WHERE Age = 20;

--Truncate: DDL command that also deletes all records from a table without removing table structure, but it doesn’t use the WHERE clause. TRUNCATE is faster than DELETE, as it doesn't scan every record before removing it. 
TRUNCATE TABLE riya.sample_person ;

--DROP: DDL command that deletes the table structure from the database, along with any data stored in the table.



--WHERE VS HAVING
--Where: used with SELECT, UPDATE, DELETE statements.Records extracted who are satisfying the specified condition in WHERE clause. Can be used without Group by. cannot contain aggregate function

--Having: only used with SELECT statement.It filters the records from the groups based on the given condition in the HAVING Clause. Cannot be used without Group by. can contain aggregate function
SELECT Gender, COUNT(Gender) AS TotalGender
FROM riya.table_employee_record ter 
GROUP BY Gender 
HAVING count(Gender)>2;

--For UNION and UNION ALL to work, the Number, Data types, and the order of the columns in the select statements should be same.
--Union 
SELECT Name, Surname FROM riya.table_employee_record ter 
UNION 
SELECT Name, Surname FROM riya.table_person tp ;

--Union All
SELECT Name, Surname FROM riya.table_employee_record ter 
UNION ALL
SELECT Name, Surname FROM riya.table_person tp 
 Order by Name;


-- UNION removes duplicate rows, where as UNION ALL does not. 
--When use UNION, to remove the duplicate rows, sql has to to do a distinct sort, which is time consuming. Hence, Union All is faster.


--JOIN VS UNION
--UNION combines the result-set of two or more select queries into a single result-set which includes all the rows from all the queries in the union, where as JOINS, retrieve data from two or more tables based on logical relationships between the tables. 
--In short, UNION combines rows from 2 or more tables, where JOINS combine columns from 2 or more table.











