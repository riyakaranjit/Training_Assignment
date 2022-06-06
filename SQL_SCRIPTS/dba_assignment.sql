-- Procedure to get all table info
 CREATE OR ALTER PROC riya.spGetallTableInfo @schema_name nvarchar(20) AS BEGIN
SELECT
	db_name() AS Db_Name,
	t.name AS Table_Name,
	SCHEMA_NAME(t.schema_id) AS Schema_Name,
	au.type_desc AS Allocation_unit_type,
	au.total_pages / 128. AS Size_Allocated_In_MB,
	au.used_pages / 128. AS Size_Usage_In_MB,
	(au.total_pages - au.used_pages) / 128. AS Size_Remaining_In_Mb,
	p.rows AS No_of_Rows,
	p.index_id,
	t.create_date AS Create_Date,
	t.modify_date AS Modify_Date
FROM
	traineeshipDB.sys.allocation_units au
JOIN traineeshipDB.sys.partitions p ON
	au.container_id = p.hobt_id
JOIN traineeshipDB.sys.tables t ON
	t.object_id = p.object_id
WHERE
	SCHEMA_NAME(t.schema_id) = @schema_name
ORDER BY
	Size_Allocated_In_MB DESC
END ;

EXEC riya.spGetallTableInfo 'riya';
----

--Procedure for getting all columns details
CREATE OR ALTER PROC riya.spGetallColumnsInfo @schema varchar(100),
@table varchar(100) AS BEGIN 
DECLARE @fk TABLE (keys varchar(50),
referenced VARCHAR(100)) 
DECLARE @pk TABLE (pk_col_name varchar(20)) 
BEGIN 
INSERT
	INTO
	@pk
SELECT
	CoCU.COLUMN_NAME
FROM
	INFORMATION_SCHEMA.TABLE_CONSTRAINTS TC
JOIN INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE CoCU ON
	CoCU.CONSTRAINT_NAME = TC.CONSTRAINT_NAME
WHERE
	CoCU.TABLE_NAME = @table
	AND TC.CONSTRAINT_TYPE = 'PRIMARY KEY'
INSERT
	INTO
	@fk 
SELECT
	COLUMN_NAME,
	OBJECT_NAME(referenced_object_id)
FROM
	INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE ccu
JOIN sys.foreign_keys ON
	CONSTRAINT_NAME = name
WHERE
	ccu.TABLE_SCHEMA = @schema
	AND ccu.TABLE_NAME = @table
	AND ccu.CONSTRAINT_NAME LIKE 'FK%'
SELECT
	db_name() AS Db,
	OBJECT_NAME(c.object_id) AS Table_Name,
	c.name AS Columns,
	CASE
		c.is_identity WHEN 1 THEN 'Yes'
		ELSE 'No'
	END AS Is_identity,
	CASE
		WHEN pk_col_name IS NULL THEN 'No'
		ELSE 'Yes'
	END AS Is_primary,
	CASE
		WHEN keys IS NULL THEN 'No'
		ELSE 'Yes'
	END AS Is_foreign,
	referenced AS Parent_Table,
	CASE
		c.is_nullable WHEN 0 THEN 'No'
		ELSE 'Yes'
	END AS Is_Nullable,
	t.name AS Data_Type,
	c.max_length AS Max_Length,
	c.precision AS PRECISION
FROM
	sys.columns c
JOIN sys.tables tab ON
c.object_id = tab.object_id
LEFT JOIN @pk ON 
	c.name = pk_col_name 
LEFT JOIN @fk ON
	c.name = keys
JOIN sys.types t ON
	t.user_type_id = c.user_type_id
WHERE tab.name = @table AND schema_name(tab.schema_id) = @schema 
END 
END;

EXEC riya.spGetallColumnsInfo 'riya',
'tblProducts';