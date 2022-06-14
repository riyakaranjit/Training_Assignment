SELECT * FROM sys.objects o ;
-----
SELECT
	*
FROM
	sys.indexes i
WHERE
	OBJECT_NAME(object_id) = N'riya.table_person';

SELECT
	*
FROM
	sys.allocation_units au ;
---
SELECT
	*
FROM
	sys.databases;

EXEC sp_databases;
---

-- list of all tables in the selected database in the specific schema
 SELECT
	*
FROM
	INFORMATION_SCHEMA.TABLES t
WHERE
	t.TABLE_SCHEMA = 'riya';
-- list of all constraints in the selected database
 SELECT
	*
FROM
	INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
WHERE
	tc.TABLE_SCHEMA = 'riya';
-----
 SELECT
	t.TABLE_NAME,
	tc.CONSTRAINT_NAME,
	tc.CONSTRAINT_TYPE
FROM
	INFORMATION_SCHEMA.TABLES t
INNER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON
	t.TABLE_NAME = tc.TABLE_NAME
WHERE
	t.TABLE_SCHEMA = 'riya'
ORDER BY
	t.TABLE_NAME ASC,
	tc.CONSTRAINT_TYPE DESC;
-- join tables and constraints data to coun the number of primary, foreign and unique keys
 SELECT
	t.TABLE_NAME,
	SUM(CASE WHEN tc.CONSTRAINT_TYPE = 'PRIMARY KEY' THEN 1 ELSE 0 END) AS primary_key,
	SUM(CASE WHEN tc.CONSTRAINT_TYPE = 'UNIQUE' THEN 1 ELSE 0 END) AS unique_key,
	SUM(CASE WHEN tc.CONSTRAINT_TYPE = 'FOREIGN KEY' THEN 1 ELSE 0 END) AS foreign_key
FROM
	INFORMATION_SCHEMA.TABLES t
LEFT JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc ON
	t.TABLE_NAME = tc.TABLE_NAME
WHERE
	t.TABLE_SCHEMA = 'riya'
GROUP BY
	t.TABLE_NAME
ORDER BY
	t.TABLE_NAME ASC;
---   

-- Lists all the tables and each of its column 
 SELECT
	c.TABLE_NAME ,
	c.COLUMN_NAME
FROM
	INFORMATION_SCHEMA.COLUMNS c
WHERE
	c.TABLE_SCHEMA = 'riya';

-- Count of columns in each databases
SELECT
	table_name,
	count(*) AS column_count
FROM
	information_schema.columns
WHERE
	 TABLE_SCHEMA = 'riya'
GROUP BY
	table_name
ORDER BY
	table_name;
-- List of each column of specific tables
 SELECT
	c.TABLE_NAME ,
	c.COLUMN_NAME
FROM
	INFORMATION_SCHEMA.COLUMNS c
WHERE
	c.TABLE_SCHEMA = 'riya'
	AND c.TABLE_NAME = 'table_employee_record';
-- Row Count
SELECT
	quotename(schema_name(sobj.schema_id)) + '.' + quotename(sobj.name) AS table_name,
	sum(sptn.rows) AS row_count
FROM
	sys.objects AS sobj
INNER JOIN sys.partitions AS sptn ON
	sobj.object_id = sptn.object_id
WHERE
	sobj.type = 'U'
	AND sobj.is_ms_shipped = 0x0
	AND schema_name(sobj.schema_id) = 'riya'
GROUP BY
	sobj.schema_id,
	sobj.name
ORDER BY
	table_name;











