-- CSQL script that creates a function SafeDiv that divides (and returns)
-- the first by the second number or returns 0 if the second number is equal to 0

CREATE FUNCTION SafeDiv(a INT, b INT)
DELIMITER $$
BEGIN
	DECLARE val FLOAT;
	IF b = 0
	THEN
	RETURN 0;
END IF;
SET val = a/b;
RETURN val;
END;$$
DELIMITER ;$$
