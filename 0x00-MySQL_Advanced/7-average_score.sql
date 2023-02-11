-- script that creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id)
DELIMITER $$
BEGIN
	DECLARE avg_score FLOAT;
	SELECT AVG(score) INTO avg_score FROM corrections where corrections.user_id = user_id;
	UPDATE users SET users.average_score = avg_score WHERE users.id = user_id;
END;$$
DELIMITER ;
