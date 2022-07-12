USE test_db;

CREATE TABLE riya.companies ( company_id INT IDENTITY(1,
1) PRIMARY KEY,
company_name VARCHAR (max) NOT NULL );

CREATE TABLE riya.Employees ( employee_id int IDENTITY(1,
1) PRIMARY KEY,
first_name VARCHAR (max) DEFAULT NULL,
last_name VARCHAR (max) DEFAULT NULL,
email VARCHAR (max) DEFAULT NULL,
phone_number varchar(max) DEFAULT NULL, 
salary int DEFAULT NULL,
company_id int DEFAULT NULL,
FOREIGN KEY(company_id) REFERENCES riya.companies (company_id) ON
DELETE
	CASCADE ON
	UPDATE
		CASCADE );
	
SELECT * FROM riya.companies c;
SELECT * FROM riya.Employees;

SELECT
	e.* ,
	c.company_name
FROM
	riya.Employees e
JOIN riya.companies c ON
	c.company_id = e.company_id ;


--- For Inserting data from csv Sales Data


CREATE TABLE riya.sales ( Order_Line int PRIMARY KEY,
order_ID varchar(max),
Order_Date date,
Ship_Date date,
Ship_Mode varchar(max),
Customer_ID varchar(max),
Product_ID varchar(max),
Sales NUMERIC,
Quantity int,
Discount NUMERIC,
Profit NUMERIC );


SELECT * FROM riya.sales s;

----
CREATE TABLE riya.science_class(
Enrollment_no int ,
Name varchar(max),
science_marks int
);

INSERT INTO riya.science_class VALUES (1,'Popeye', 33);
INSERT INTO riya.science_class VALUES (2,'Olive', 54);
INSERT INTO riya.science_class VALUES (3,'Brurus', 98);

SELECT * FROM riya.science_class;
Delete riya.science_class WHERE Name IS NULL ;


CREATE TABLE riya.Product(
surr_id int PRIMARY KEY,
product_id varchar(max) DEFAULT 'N/A' NOT NULL,
category varchar(max) DEFAULT 'N/A' NOT NULL,
sub_category varchar(max) DEFAULT 'N/A' NOT NULL,
product_name varchar(max) DEFAULT 'N/A' NOT NULL,
start_date date,
end_date date,
version int DEFAULT 1 NOT NULL,
[current] varchar(5) DEFAULT 'Y' NOT NULL,
lastupdate date
);


CREATE TABLE riya.Customer(
surr_id int PRIMARY KEY,
customer_id varchar(max) DEFAULT 'N/A' NOT NULL,
customer_name varchar(max) DEFAULT 'N/A' NOT NULL,
segment varchar(max) DEFAULT 'N/A' NOT NULL,
age int DEFAULT '0' NOT NULL,
city varchar(max) DEFAULT 'N/A' NOT NULL,
state_name varchar(max) DEFAULT 'N/A' NOT NULL,
country varchar(max) DEFAULT 'N/A' NOT NULL,
postal_code varchar(max) DEFAULT 'N/A' NOT NULL,
region varchar(max) DEFAULT 'N/A' NOT NULL
);

CREATE TABLE riya.FinalSales(
order_line int PRIMARY KEY,
order_id varchar(max) DEFAULT 'N/A' NOT NULL,
order_date date DEFAULT '1900-01-01' NOT NULL,
ship_date date DEFAULT '1900-01-01' NOT NULL,
ship_mode varchar(max) DEFAULT 'N/A' NOT NULL,
s_cust_id varchar(max) DEFAULT '0' NOT NULL,
s_prod_id varchar(max) DEFAULT '0' NOT NULL,
sales NUMERIC DEFAULT '0' NOT NULL,
quantity int DEFAULT '0' NOT NULL,
discount NUMERIC DEFAULT '0' NOT NULL,
profit NUMERIC DEFAULT '0' NOT NULL
);

SELECT max(Order_Line) FROM riya.Sales s ;


SELECT * FROM riya.product;
SELECT * FROM riya.customer;
SELECT * FROM riya.finalsales;
--DELETE FROM riya.FinalSales ;
