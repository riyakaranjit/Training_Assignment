USE traineeshipDB;

CREATE SCHEMA fc_raw;

DROP TABLE fc_raw.fc_balance_summary ;
DROP TABLE fc_raw.fc_account_master ;
DROP TABLE fc_raw.fc_transaction_base ;

CREATE TABLE fc_raw.fc_balance_summary(
--tran_date date,
acc_number varchar(max),
balance NUMERIC(20,2),
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
); 

CREATE TABLE fc_raw.fc_account_master(
acc_number varchar(max),
cust_code varchar(max),
--branch int,
--product varchar(max),
--product_category varchar(max),
--acc_open_date date,
--active_flag int,
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
);



CREATE TABLE fc_raw.fc_transaction_base(
--tran_date date,
acc_number varchar(max),
--transaction_code varchar(max),
--dc_indicator varchar(5),
--description1 varchar(max),
--is_salary int,
balance int,
created_by varchar(20) DEFAULT 'riya' NOT null,
created_on datetime DEFAULT CURRENT_TIMESTAMP,
modified_by varchar(max) DEFAULT NULL,
modified_on datetime DEFAULT NULL 
);



SELECT * FROM fc_raw.fc_transaction_base;
SELECT * FROM fc_raw.fc_account_master;
SELECT * FROM fc_raw.fc_balance_summary;


SELECT count(*) FROM fc_raw.fc_transaction_base;
SELECT count(*) FROM fc_raw.fc_account_master;
SELECT count(*) FROM fc_raw.fc_balance_summary;


