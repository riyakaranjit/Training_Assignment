USE test_db;

CREATE SCHEMA fc_rw;
CREATE SCHEMA fc_master;
CREATE SCHEMA fc_facts;
CREATE SCHEMA QA;

DROP TABLE fc_rw.fc_balance_summary ;
DROP TABLE fc_rw.fc_account_master ;
DROP TABLE fc_rw.fc_transaction_base ;

CREATE TABLE fc_rw.fc_balance_summary(
tran_date date,
account_number varchar(max),
lcy_amount NUMERIC(20,2),
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
); 

CREATE TABLE fc_rw.fc_account_master(
account_number varchar(max),
customer_code varchar(max),
branch int,
product varchar(max),
product_category varchar(max),
acc_open_date date,
active_flag int,
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
);


CREATE TABLE fc_rw.fc_transaction_base(
tran_date date,
account_number varchar(max),
transaction_code varchar(max),
dc_indicator varchar(5),
description1 varchar(max),
is_salary int,
lcy_amount int,
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
);


CREATE TABLE fc_facts.fc_balance_facts(
account_number varchar(max),
avg_monthly_balance float,
std_monthly_balance float,
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
); 

SELECT * FROM fc_facts.fc_balance_facts ORDER BY account_number;

CREATE TABLE fc_facts.fc_transaction_base_facts(
account_number varchar(max),
avg_monthly_deposit float,
std_monthly_deposit float,
avg_monthly_withdraw float,
std_monthly_withdraw float,
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
); 
SELECT * FROM fc_facts.fc_transaction_base_facts 
ORDER BY account_number;

DROP TABLE fc_facts.fc_balance_last_3_days;
CREATE TABLE fc_facts.fc_balance_last_3_days(
account_number varchar(max),
tran_date date,
balance float,
balance_before_1_day float,
balance_before_2_days float,
balance_before_3_days float,
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
); 

SELECT * FROM fc_facts.fc_balance_last_3_days;

DROP TABLE fc_master.fc_clients ;
CREATE TABLE fc_master.fc_clients (
id int IDENTITY(1,1),  
customer_code varchar(max),
active_flag int,
created_by varchar(20) ,
created_on datetime ,
modified_by varchar(max) ,
modified_on datetime 
)
;

SELECT count(*) FROM fc_master.fc_clients ;

CREATE TABLE fc_master.fc_tables (
id int,  
Source_schema varchar(50),
Source_table varchar(50),
Destination_schema varchar(50),
Destination_table varchar(50)
);

SELECT * FROM fc_master.fc_tables;

CREATE TABLE fc_master.fc_fields_mapping  (
id int,  
Table_id int,
Source_field varchar(50),
Destination_field varchar(50)
);
SELECT * FROM fc_master.fc_fields_mapping ;
SELECT * FROM riya.fc_fields_mapping ;

INSERT INTO fc_master.fc_fields_mapping VALUES (3,3,'lcy_amount', 'balance');


CREATE TABLE fc_facts.fc_score (
account_number varchar(50),
customer_code varchar(20),
confidence_percentage int
);
SELECT * FROM fc_facts.fc_score;

CREATE TABLE fc_facts.fc_config (
id int,  
field varchar(50),
[sign] varchar(5),
Value int
);

SELECT * FROM fc_facts.fc_config;

DELETE FROM fc_facts.fc_config;

------

--creating trigger to update to the current timestamp for every update
CREATE TRIGGER riya.trgAfterUpdate_transbasefacts ON test_db.riya.fc_transaction_base_facts
AFTER INSERT, UPDATE 
AS
  UPDATE test_db.riya.fc_transaction_base_facts
  SET modified_on = GETDATE()
  FROM Inserted i;
 
 --
 UPDATE riya.testing_fc_account_master
SET branch = 19
WHERE account_number = '02XYZXYZ10017560004';
 ----------------------

SELECT
	tftb.account_number ,
	avg(lcy_amount) avg_value,
	MONTH(tftb.tran_date) Mnth,
	year(tftb.tran_date) year1
FROM
	riya.fc_balance_summary tftb
--	WHERE tftb.account_number = '02XYZXYZ10017500606'
GROUP BY tftb.account_number , Month(tftb.tran_date), year(tftb.tran_date)
ORDER BY tftb.account_number ;

-----SELECT STMTS
SELECT * FROM fc_rw.fc_transaction_base;
SELECT * FROM fc_rw.fc_account_master ORDER BY customer_code;
SELECT * FROM fc_rw.fc_balance_summary;
SELECT count(*) FROM fc_facts.fc_balance_facts ;
SELECT count(*) FROM fc_facts.fc_transaction_base_facts ;
SELECT count(*) FROM fc_facts.fc_balance_last_3_days;
SELECT * FROM riya.fc_clients;
SELECT * FROM test_db.riya.fc_tables;
---
WITH e AS
(
     SELECT *,
         ROW_NUMBER() OVER
         (
             PARTITION BY account_number 
             ORDER BY tran_date DESC
         ) AS Recency
     FROM riya.fc_balance_summary fbs 
)
SELECT *
FROM e
WHERE Recency < 4;

----
SELECT
	destination_schema,
	destination_table,
	CONCAT('SELECT ', string_agg(concat(ffm.Source_field, ' as ', ffm.Destination_field), ','), ' FROM ', Source_schema, '.', Source_table) AS query
FROM
	fc_master.fc_tables ft
JOIN fc_master.fc_fields_mapping ffm ON
	ft.id = ffm.table_id
GROUP BY
	destination_schema,
	destination_table,
	Source_schema,
	Source_table;
---
SELECT
	concat('SELECT * FROM fc_facts.fc_score WHERE ', string_agg(concat(field, [sign], [Value]), ' and '), ' ;') AS query
FROM
	fc_facts.fc_config;




;