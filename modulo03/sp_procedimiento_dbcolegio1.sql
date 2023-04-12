USE dbcolegio;

DELIMITER //
CREATE PROCEDURE sp_alumnocurso_select()
BEGIN
	SELECT CONCAT(A.Nombres, ' ', A.Apellidos) AS alumno_nombre_completo, A.Genero AS alumno_genero, 
			C.Nombre AS curso_nombre, C.Descripcion AS curso_descripcion
    FROM tblalumno_curso AS AC
    INNER JOIN tblalumno AS A
		ON A.idAlumno = AC.idAlumno
	INNER JOIN tblCurso AS C
		ON C.idCurso = AC.idCurso;
END //
DELIMITER ;

