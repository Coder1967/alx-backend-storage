-- script that creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student

CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id)
DELIMITER $$
BEGIN
	DECLARE avg_score FLOAT;
	SELECT AVG(score) INTO avg_score FROM corrections;
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END;$$
DELIMITER ;
