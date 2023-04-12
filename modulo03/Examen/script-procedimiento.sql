USE dbmatricula;

DELIMITER //
CREATE PROCEDURE sp_matriculas_select()
BEGIN
	SELECT *
    FROM matriculas AS M
    INNER JOIN estudiantes AS E
		ON E.idEstudiantes = M.idEstudiantes
	INNER JOIN clases AS C
		ON C.idClases = M.idClases;
END //

DELIMITER ;

