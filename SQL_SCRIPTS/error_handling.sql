SELECT
	*
FROM
	riya.tblProducts tp ;

SELECT
	*
FROM
	riya.tblProductSales tps ;

DROP TABLE riya.tblProductSales ;

CREATE TABLE riya.tblProductSales ( Id int PRIMARY KEY,
ProductId int,
QuantitySold int );

ALTER TABLE riya.tblProducts ADD QtyAvailable int;

DECLARE @StockAvailable int
SELECT
	@StockAvailable = QtyAvailable
FROM
	riya.tblProducts tp
WHERE
	Id = 1;
--RAISERROR('Error Message', ErrorSeverity, ErrorState) 
--Severity Level = 16 (indicates general errors that can be corrected by user). State = 1-255 but raiseerror can generate error from 1-127
--Throw an error, if the enough stock is not available
 ALTER PROCEDURE riya.spSellProducts @ProductId int,
@QuantityToSell int AS BEGIN
--Check if stock available for the product we want to sell. 
 DECLARE @StockAvailable int
SELECT
	@StockAvailable = QtyAvailable
FROM
	riya.tblProducts tp
WHERE
	Id = @ProductId IF(@StockAvailable < @QuantityToSell) BEGIN RAISERROR('Not enough stock available',
	16,
	1)
END
ELSE BEGIN BEGIN TRAN
--Subtract the quantity sold form quantity available
 UPDATE
	riya.tblProducts
SET
	QtyAvailable = (QtyAvailable-@QuantityToSell)
WHERE
	Id = @ProductId DECLARE @MaxProductSalesId int
--Calculate the Max Product Sales Table Id
 SELECT
	@MaxProductSalesId =
	CASE
		WHEN Max(Id) IS NULL THEN 0
		ELSE Max(Id)
	END
FROM
	riya.tblProductSales tps
	--Increase the Id By 1, Prevent from Primary key Violation
 SET
	@MaxProductSalesId = @MaxProductSalesId + 1
INSERT
	INTO
	riya.tblProductSales (Id,
	ProductId,
	QuantitySold)
VALUES (@MaxProductSalesId,
@ProductId,
@QuantityToSell)
--@@Error return non-zero for failure and 0 for success.
 IF (@@Error <> 0) BEGIN ROLLBACK TRAN PRINT 'Transaction Rollback. Error Occured'
END
ELSE BEGIN COMMIT TRAN PRINT 'Transaction Committed.'
END
END
END;

EXEC riya.spSellProducts @ProductId = 2,
@QuantityToSell = 5;
--@@Error: It is cleared and reset on each statement execution. We need to check the error immediately following the statment being verified or save it to a local variable that can be checked later.
 INSERT
	INTO
	riya.tblProducts
VALUES(2,
'Mobile Phone',
1500,
100) IF(@@ERROR <> 0) PRINT 'Error Occurred'
ELSE PRINT 'No Errors';

INSERT
	INTO
	riya.tblProducts
VALUES(2,
'Mobile Phone',
1500,
100)
--At this point @@ERROR will have a NON ZERO value 
 SELECT
	*
FROM
	riya.tblProducts
	--At this point @@ERROR gets reset to ZERO, because the 
	--select statement successfullyexecuted
 IF(@@ERROR <> 0) PRINT 'Error Occurred'
	ELSE PRINT 'No Errors';

DECLARE @Error int
INSERT
	INTO
	riya.tblProducts
VALUES(2,
'Mobile Phone',
1500,
100) SET
@Error = @@ERROR
SELECT
	*
FROM
	tblProduct IF(@Error <> 0) PRINT 'Error Occurred'
	ELSE PRINT 'No Errors'
