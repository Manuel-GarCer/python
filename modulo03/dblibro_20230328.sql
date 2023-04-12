CREATE DATABASE DBLibro;
USE DBLibro;

CREATE TABLE autor (
	id_autor int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nombre varchar(150) DEFAULT NULL,
	apellido varchar(150) DEFAULT NULL
);

CREATE TABLE obra (
	id_obra int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	id_autor int(11) NOT NULL,
	titulo varchar(150) DEFAULT NULL,
	publicacion char(4) DEFAULT NULL,
	foreign key (id_autor) references autor(id_autor) ## IMPORTANTE DE COMO SE RELACIONAN
);

SHOW TABLES;

DESCRIBE autor;
DESCRIBE obra;

DROP TABLE autor;
DROP TABLE obra;
