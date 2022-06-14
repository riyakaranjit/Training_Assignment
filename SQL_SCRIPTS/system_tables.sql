SELECT
	schema_name(t.schema_id) AS schema_name,
	t.name AS table_name
FROM
	sys.tables t
WHERE
	schema_name(t.schema_id) = 'riya'
ORDER BY
	table_name;
	
----
Select TABLE_SCHEMA, TABLE_NAME
    , Stuff(
        (
        Select ', ' + C.COLUMN_NAME
        From INFORMATION_SCHEMA.COLUMNS As C
        Where C.TABLE_SCHEMA = T.TABLE_SCHEMA
            And C.TABLE_NAME = T.TABLE_NAME
        Order By C.ORDINAL_POSITION
        For Xml Path('')
        ), 1, 2, '') As Columns
From INFORMATION_SCHEMA.TABLES As T
WHERE TABLE_SCHEMA = 'riya';

--
Select TABLE_SCHEMA, TABLE_NAME
    , Stuff(
        (
        Select ', ' + C.COLUMN_NAME
        From INFORMATION_SCHEMA.COLUMNS As C
        Where C.TABLE_SCHEMA = T.TABLE_SCHEMA
            And C.TABLE_NAME = T.TABLE_NAME
        Order By C.ORDINAL_POSITION
        For Xml Path('')
        ), 1, 2, '') As Columns
From INFORMATION_SCHEMA.TABLES As T

--

SELECT
	T.TABLE_SCHEMA,
	T.TABLE_NAME,
	cu.COLUMN_NAME AS Primary_key_col
FROM
	INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS cu
JOIN INFORMATION_SCHEMA.TABLES AS T ON
	cu.TABLE_SCHEMA = T.TABLE_SCHEMA
	AND cu.TABLE_NAME = T.TABLE_NAME
WHERE
	OBJECTPROPERTY(OBJECT_ID(cu.CONSTRAINT_SCHEMA + '.' + QUOTENAME(cu.CONSTRAINT_NAME)),
	'IsPrimaryKey') = 1
	AND T.TABLE_SCHEMA = 'riya';

--
SELECT
	'TRUNCATE TABLE' + ' ' + '[' + T.TABLE_SCHEMA + '.' + T.TABLE_NAME + ']' + ';'
FROM
	INFORMATION_SCHEMA.TABLES AS T
WHERE
	 T.TABLE_SCHEMA = 'riya';

--
SELECT
	'SELECT * FROM' + ' ' + '[' + T.TABLE_SCHEMA + '.' + T.TABLE_NAME + ']' + ';'
FROM
	INFORMATION_SCHEMA.TABLES AS T
WHERE
	 T.TABLE_SCHEMA = 'riya';
	
--Hierarchy level
WITH HierarchyLvl AS (
SELECT
	ID,
	Name,
	MgrID ,
	1 AS LEVEL
FROM
	riya.table_generate_hierarchy tgh
WHERE
	MgrID IS NULL
UNION ALL
SELECT
	e.ID,
	e.Name ,
	e.MgrID ,
	LEVEL + 1
FROM
	riya.table_generate_hierarchy e
INNER JOIN HierarchyLvl d ON
	e.MgrID = d.ID )
SELECT
	emp.Name,
	Isnull(mgr.name,
	'HEAD') AS Manager,
	emp.Level
FROM
	HierarchyLvl emp
LEFT JOIN HierarchyLvl mgr ON
	emp.MgrID = mgr.ID;
	

