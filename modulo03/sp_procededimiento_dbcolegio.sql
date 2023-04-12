USE dbcolegio;


DELIMITER //
CREATE PROCEDURE sp_alumnocurso_select()
BEGIN
	SELECT *
    FROM tblalumno_curso AS AC
    INNER JOIN tbalumno AS A
		ON A.idAlumno = AC.idAlumno
	INNER JOIN tblCurso AS C
		ON C.idCurso = AC.idCurso;
END //
DELIMITER ;

USE `dbcolegio`;
DROP procedure IF EXISTS `sp_alumnocurso_select`;

USE `dbcolegio`;
DROP procedure IF EXISTS `dbcolegio`.`sp_alumnocurso_select`;
;

DELIMITER $$
USE `dbcolegio`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_alumnocurso_select`()
BEGIN
	SELECT *
    FROM tblalumno_curso AS AC
    INNER JOIN tbalumno AS A
		ON A.idAlumno = AC.idAlumno
	INNER JOIN tblCurso AS C
		ON C.idCurso = AC.idCurso;
        
END$$

DELIMITER ;
;
            