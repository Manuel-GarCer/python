-- CREAR UNA BASE DE DATOS
CREATE DATABASE dbprueba;

-- SELECCIONAR BASE DE DATOS A USAR
USE dbprueba;

-- CREANDO LA TABLA tblpersona
CREATE TABLE `dbprueba`.`tblpersona` (
  `id_persona` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(50) NULL,
  `apellido` VARCHAR(50) NULL,
  `tipo_doc` CHAR(1) NULL, -- 1 : DNI - 2 : CARD. EXTRANGERIA - 3 : PASAPORTE
  `num_docu` CHAR(12) NULL,
  `direccion` VARCHAR(250) NULL,
  `telefono` VARCHAR(50) NULL,
  `fec_nacimiento` DATE NULL,
  `genero` CHAR(1) NULL, -- M : MASCULINO - F : FEMENINO
  `estado` CHAR(1) NULL, -- 1 : HABILITADO - 2 : DESHABILITADO - 3 : ELIMINADO
  PRIMARY KEY (`id_persona`));
  
  -- INSERTANDO DATOS A LA TABLA
INSERT INTO `dbprueba`.`tblpersona` 
(`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) 
VALUES 
('Eduardo', 'Tolentino', '1', '12345678', 'Jr. Lima 321', '987654321', '1995-12-12', 'M', '1');

INSERT INTO `dbprueba`.`tblpersona` 
(`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `estado`, `genero`) 
VALUES 
('Karen', 'Quispe', '1', '87654323', 'Jr. Ayacucho 322', '987654323', '1995-11-14', '1', 'F');

-- ACTUALIZANDO CAMPOS DE LA TABLA
UPDATE `dbprueba`.`tblpersona` 
SET 
`num_docu` = '87654323', 
`direccion` = 'Jr. Ayacucho 322', 
`fec_nacimiento` = '1995-11-14' 
WHERE (`id_persona` = '3');

-- CONSULTANDO DATOS DE LA TABLA
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM `dbprueba`.`tblpersona`;
-- ESTADO HABILITADO
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM `dbprueba`.`tblpersona`
WHERE estado = '1';
-- ESTADO DESHABILITADO
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM `dbprueba`.`tblpersona`
WHERE estado = '2';
-- ESTADO ELIMINADO
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM `dbprueba`.`tblpersona`
WHERE estado = '3' AND nombre = 'Karen';

SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM `dbprueba`.`tblpersona`
WHERE NOT genero = 'M';

-- CONSULTAS CON QUERYS AGRUPADOS
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM `dbprueba`.`tblpersona`
WHERE (estado = '3' OR estado = '1') AND genero = 'M';

-- ELIMINAR DATOS DE LA TABLA
DELETE FROM `dbprueba`.`tblpersona` WHERE idpersona = '30';

-- DATOS tblpersona
INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Eduardo', 'Tolentino', '1', '87654321', 'Direccion 01', '987654321', '1995-12-12', 'M', '1');
INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Carlos', 'Diaz', '1', '87654322', 'Direccion 02', '987654322', '1995-11-22', 'M', '1');
INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Maria', 'Gonzales', '1', '87654323', 'Direccion 03', '987654323', '1995-10-05', 'F', '1');

INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Sara', 'Perez', '1', '87654324', 'Direccion 04', '987654324', '1995-10-06', 'F', '1'); 
INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Marta', 'Rojas', '1', '87654325', 'Direccion 05', '987654325', '1995-10-07', 'F', '1');
INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Jose', 'Quispe', '1', '87654326', 'Direccion 06', '987654326', '1995-10-08', 'M', '1'); 
INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Marcos', 'Camargo', '1', '87654327', 'Direccion 07', '987654327', '1995-10-09', 'M', '1'); 
INSERT INTO `dbprueba`.`tblpersona` (`nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('Luis', 'Prado', '1', '87654328', 'Direccion 08', '987654328', '1995-10-10', 'M', '1');

SELECT * FROM dbprueba.tblestudiante;

INSERT INTO `dbprueba`.`tblpersona` (`idpersona`, `nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('9', 'Luis', 'Quinto', '1', '87654329', 'Direccion 09', '987654329', '1995-10-11', 'M', '1'); 
INSERT INTO `dbprueba`.`tblpersona` (`idpersona`, `nombre`, `apellido`, `tipo_doc`, `num_docu`, `direccion`, `telefono`, `fec_nacimiento`, `genero`, `estado`) VALUES ('10', 'Liliana', 'Perez', '1', '87654330', 'Direccion 10', '987654330', '1995-10-12', 'F', '1');


-- Datos tblseccion
INSERT INTO `dbprueba`.`tblseccion` (`nombre`, `descripcion`) VALUES ('A', 'Alumnos con notas de 20 a 17');
INSERT INTO `dbprueba`.`tblseccion` (`nombre`, `descripcion`) VALUES ('B', 'Alumnos con notas de 16 a 14');
INSERT INTO `dbprueba`.`tblseccion` (`nombre`, `descripcion`) VALUES ('C', 'Alumnos con notas de 13 a 0');

-- DATOS DE tblEstudiante
INSERT INTO `dbprueba`.`tblestudiante` (`idpersona`, `idseccion`, `estado`) VALUES ('5', '1', '1');
INSERT INTO `dbprueba`.`tblestudiante` (`idestudiante`, `idpersona`, `idseccion`, `estado`) VALUES ('4', '4', '2', '1');
INSERT INTO `dbprueba`.`tblestudiante` (`idestudiante`, `idpersona`, `idseccion`, `estado`) VALUES ('5', '5', '2', '1');
INSERT INTO `dbprueba`.`tblestudiante` (`idestudiante`, `idpersona`, `idseccion`, `estado`) VALUES ('6', '6', '2', '1');
INSERT INTO `dbprueba`.`tblestudiante` (`idestudiante`, `idpersona`, `idseccion`, `estado`) VALUES ('7', '7', '3', '1');
INSERT INTO `dbprueba`.`tblestudiante` (`idestudiante`, `idpersona`, `idseccion`, `estado`) VALUES ('8', '8', '3', '1');
INSERT INTO `dbprueba`.`tblestudiante` (`idestudiante`, `idpersona`, `idseccion`, `estado`) VALUES ('9', '9', '2', '1');
INSERT INTO `dbprueba`.`tblestudiante` (`idestudiante`, `idpersona`, `idseccion`, `estado`) VALUES ('10', '10', '3', '1');




-- Listar todos los registros donde NombreSeccion sea igual a C y B
SELECT P.nombre, P.apellido, CONCAT(P.nombre, ' ', P.apellido) AS 'nombrescompletos', S.nombre AS 'nombreseccion', S.descripcion
FROM dbprueba.tblestudiante AS E
INNER JOIN dbprueba.tblpersona AS P
	ON P.idpersona = E.idpersona
INNER JOIN dbprueba.tblseccion AS S
	ON S.idseccion = E.idseccion
WHERE S.nombre = 'C' OR S.nombre = 'B';


-- Listar todos los registros donde Apellido sea igual a Perez y NombreSeccion sea igual a C
SELECT P.nombre, P.apellido, CONCAT(P.nombre, ' ', P.apellido) AS 'nombrescompletos', S.nombre AS 'nombreseccion', S.descripcion
FROM dbprueba.tblestudiante AS E
INNER JOIN dbprueba.tblpersona AS P
	ON P.idpersona = E.idpersona
INNER JOIN dbprueba.tblseccion AS S
	ON S.idseccion = E.idseccion
WHERE P.apellido = 'Perez' 
	AND S.nombre = 'C';
    
-- autor Listar todos los registros donde Apellido comience con P y Nombres que contengan L
SELECT P.nombre, P.apellido, CONCAT(P.nombre, ' ', P.apellido) AS 'nombrescompletos', S.nombre AS 'nombreseccion', S.descripcion
FROM dbprueba.tblestudiante AS E
INNER JOIN dbprueba.tblpersona AS P
	ON P.idpersona = E.idpersona
INNER JOIN dbprueba.tblseccion AS S
	ON S.idseccion = E.idseccion
WHERE P.apellido LIKE 'P%'
	AND P.nombre LIKE '%L%';
    
-- =============================
-- ORDER BY
-- =============================
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM `dbprueba`.`tblpersona`
WHERE NOT genero = 'M'
ORDER BY idpersona DESC;

-- =============================
-- NULL
-- =============================
SELECT idseccion, nombre, descripcion
FROM tblseccion
WHERE descripcion IS NOT NULL;

-- =============================
-- LIMIT
-- =============================
SELECT *
FROM tblpersona
WHERE estado = '1'
LIMIT 4;

-- =============================
-- MIN - MAX
-- =============================
SELECT MIN(idpersona)
FROM tblpersona;

SELECT MAX(idpersona)
FROM tblpersona;

-- =============================
-- IN
-- =============================
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM tblpersona
WHERE genero IN ('F','M');

SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM tblpersona
WHERE idpersona IN (SELECT idpersona FROM tblestudiante WHERE estado = '1');

-- =============================
-- BETWEEN
-- =============================
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM tblpersona
WHERE fec_nacimiento BETWEEN '1995-10-01' AND '1995-10-10';

-- =============================
-- EXISTS
-- =============================
SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
FROM tblpersona
WHERE EXISTS (SELECT idpersona FROM tblestudiante WHERE estado = '1');

DELIMITER //
CREATE PROCEDURE sp_persona_select()
BEGIN
	SELECT idpersona, nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado
    FROM tblpersona;
END //
DELIMITER ;

CALL sp_persona_select();


DELIMITER //
CREATE PROCEDURE sp_persona_insert(
	c_nombre varchar(50), 
    c_apellido varchar(50), 
    c_tipo_doc char(1), 
    c_num_docu char(12), 
    c_direccion varchar(250), 
    c_telefono varchar(50), 
    f_fec_nacimiento date, 
    c_genero char(1), 
    c_estado char(1)
)
BEGIN
	INSERT INTO tblpersona
		(nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado)
    VALUES
		(c_nombre, c_apellido, c_tipo_doc, c_num_docu, c_direccion, c_telefono, f_fec_nacimiento, c_genero, c_estado);
END //
DELIMITER ;

CALL sp_persona_insert('Marta', 'Toledo', '1', '87654333', 'Direccion 13', '987654333', '1995-05-21', 'F', '1');

-- =============================
-- TRANSACCIONES
-- =============================
START TRANSACTION;
	-- SCRIPT SQL
    INSERT INTO tblpersona
		(nombre, apellido, tipo_doc, num_docu, direccion, telefono, fec_nacimiento, genero, estado)
    VALUES
		('Dario', 'De la Cruz', '1', '87654335', 'Direccion 15', '987654335', '1995-05-25', 'M', '1');
ROLLBACK;
COMMIT;
