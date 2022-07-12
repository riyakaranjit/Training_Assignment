USE test_db;
---
--Point-6: SQL script that generate balance of today and last 3 days for which entry is present.

SELECT
	fbs.account_number account_number,
	fbs.tran_date tran_date ,
	fbs.lcy_amount AS balance,
	LAG(fbs.lcy_amount) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date) AS balance_before_1_day,
	LAG(fbs.lcy_amount,
	2) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date ) AS balance_before_2_days,
	LAG(fbs.lcy_amount,
	3) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date ) AS balance_before_3_days
FROM
	fc_rw.fc_balance_summary fbs
ORDER BY
	account_number,
	tran_date ;
---

---SQL script to compare result generated from point 5(fc_facts.fc_balance_last_3_days in pentaho) and point 6 using column name status for balance of each day
WITH balance_cte AS (
SELECT
	fbs.account_number account_number,
	fam.customer_code customer_code,
	fbs.tran_date tran_date ,
	fbs.lcy_amount AS balance_qa,
	fbld.balance AS balance,
	LAG(fbs.lcy_amount) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date) AS balance_before_1_day_qa,
	fbld.balance_before_1_day balance_before_1_day,
	LAG(fbs.lcy_amount,
	2) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date ) AS balance_before_2_days_qa,
	fbld.balance_before_2_days balance_before_2_days,
	LAG(fbs.lcy_amount,
	3) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date ) AS balance_before_3_days_qa,
	fbld.balance_before_3_days balance_before_3_days
FROM
	fc_rw.fc_balance_summary fbs
JOIN fc_facts.fc_balance_last_3_days fbld ON
	fbld.account_number = fbs.account_number
	AND fbld.tran_date = fbs.tran_date
JOIN fc_rw.fc_account_master fam  ON
	fam.account_number = fbs.account_number
)
SELECT
	account_number,
	tran_date,
	customer_code,
	balance_qa,
	balance,
	balance_before_1_day_qa,
	balance_before_1_day,
	CASE
		WHEN balance_cte.balance_before_1_day = balance_cte.balance_before_1_day_qa THEN 'EQUAL'
		ELSE 'NOT EQUAL'
	END AS balance_before_1_day_status, 
	balance_before_2_days_qa,
	balance_before_2_days,
	CASE
		WHEN balance_cte.balance_before_2_days = balance_cte.balance_before_2_days_qa THEN 'EQUAL'
		ELSE 'NOT EQUAL'
	END AS balance_before_2_days_status, 
	balance_before_3_days_qa,
	balance_before_3_days,	
	CASE
		WHEN balance_cte.balance_before_3_days = balance_cte.balance_before_3_days_qa THEN 'EQUAL'
		ELSE 'NOT EQUAL'
	END AS balance_before_3_days_status
FROM
	balance_cte
ORDER BY
	account_number,
	tran_date ;

---

SELECT * FROM fc_facts.fc_balance_last_3_days;

----
----SQL procedure for point 8.
DROP PROCEDURE IF EXISTS QA.sp_qa_fc_balance_last_3_days;
CREATE OR ALTER PROCEDURE QA.sp_qa_fc_balance_last_3_days
AS
BEGIN 
WITH balance_cte AS (
SELECT
	fbs.account_number account_number,
	fam.customer_code customer_code,
	fbs.tran_date tran_date ,
	fbs.lcy_amount AS balance_qa,
	fbld.balance AS balance,
	LAG(fbs.lcy_amount) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date) AS balance_before_1_day_qa,
	fbld.balance_before_1_day balance_before_1_day,
	LAG(fbs.lcy_amount,
	2) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date ) AS balance_before_2_days_qa,
	fbld.balance_before_2_days balance_before_2_days,
	LAG(fbs.lcy_amount,
	3) OVER ( PARTITION BY fbs.account_number
ORDER BY
	fbs.tran_date ) AS balance_before_3_days_qa,
	fbld.balance_before_3_days balance_before_3_days
FROM
	fc_rw.fc_balance_summary fbs
JOIN fc_facts.fc_balance_last_3_days fbld ON
	fbld.account_number = fbs.account_number
	AND fbld.tran_date = fbs.tran_date
JOIN fc_rw.fc_account_master fam  ON
	fam.account_number = fbs.account_number
)
SELECT
	account_number,
	tran_date,
	customer_code,
	balance_qa,
	balance,
	balance_before_1_day_qa,
	balance_before_1_day,
	CASE
		WHEN balance_cte.balance_before_1_day = balance_cte.balance_before_1_day_qa THEN 'EQUAL'
		ELSE 'NOT EQUAL'
	END AS balance_before_1_day_status, 
	balance_before_2_days_qa,
	balance_before_2_days,
	CASE
		WHEN balance_cte.balance_before_2_days = balance_cte.balance_before_2_days_qa THEN 'EQUAL'
		ELSE 'NOT EQUAL'
	END AS balance_before_2_days_status, 
	balance_before_3_days_qa,
	balance_before_3_days,	
	CASE
		WHEN balance_cte.balance_before_3_days = balance_cte.balance_before_3_days_qa THEN 'EQUAL'
		ELSE 'NOT EQUAL'
	END AS balance_before_3_days_status
INTO QA.qa_fc_balance_last_3_days
FROM
	balance_cte
ORDER BY
	account_number,
	tran_date 
ALTER TABLE QA.qa_fc_balance_last_3_days 
ADD created_by varchar(20) DEFAULT 'riya' NOT NULL,
created_on datetime DEFAULT GETDATE() NOT NULL,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL
END;

SELECT GETDATE(); 
EXEC QA.sp_qa_fc_balance_last_3_days;


CREATE TABLE QA.qa_fc_balance_last_3_days(
account_number varchar(max),
tran_date date,
customer_code varchar(max),
balance_qa float,
balance float,
balance_before_1_day_qa float,
balance_before_1_day float,
balance_before_1_day_status varchar(20),
balance_before_2_days_qa float,
balance_before_2_days float,
balance_before_2_days_status varchar(20),
balance_before_3_days_qa float,
balance_before_3_days float,
balance_before_3_days_status varchar(20),
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
); 


SELECT * FROM QA.qa_fc_balance_last_3_days ;


