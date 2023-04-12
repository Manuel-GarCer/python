SELECT * FROM dbmatricula.matriculas;

INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0001', '1', 'C0001');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0002', '1', 'C0002');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0003', '1', 'C0003');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0004', '2', 'C0001');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0005', '2', 'C0002');

INSERT INTO `dbmatricula`.`estudiantes` (`Apellidos`, `Nombres`) VALUES ('Perez Martinez', 'Hector Manuel');
INSERT INTO `dbmatricula`.`estudiantes` (`Apellidos`, `Nombres`) VALUES ('Leon Ruiz', 'Pedro Javier');
INSERT INTO `dbmatricula`.`estudiantes` (`Apellidos`, `Nombres`) VALUES ('Idrogo Huaman', 'Oscar Leonidas');
INSERT INTO `dbmatricula`.`estudiantes` (`Apellidos`, `Nombres`) VALUES ('Bartra Barba', 'Maria Eliza');
INSERT INTO `dbmatricula`.`estudiantes` (`Apellidos`, `Nombres`) VALUES ('Chumbe Ortiiz', 'Eriika Milagros');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0006', '2', 'C0003');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0007', '3', 'C0001');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0008', '3', 'C0002');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0009', '3', 'C0003');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0010', '4', 'C0001');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0011', '4', 'C0002');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0012', '4', 'C0003');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0013', '5', 'C0001');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0014', '5', 'C0002');
INSERT INTO `dbmatricula`.`matriculas` (`idMatriculas`, `idEstudiantes`, `idClases`) VALUES ('M0015', '5', 'C0003');

INSERT INTO `dbmatricula`.`clases` (`idClases`, `Titulo`, `Descrpicion`) VALUES ('C0001', 'Matematica', 'Curso de Matematica');
INSERT INTO `dbmatricula`.`clases` (`idClases`, `Titulo`, `Descrpicion`) VALUES ('C0002', 'Comunicacion', 'Curso de Comunicacion');
INSERT INTO `dbmatricula`.`clases` (`idClases`, `Titulo`, `Descrpicion`) VALUES ('C0003', 'Religion', 'Curso de Religion');