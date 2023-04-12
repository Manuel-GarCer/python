CREATE DATABASE  IF NOT EXISTS `dbcolegio` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dbcolegio`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dbcolegio
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblalumno`
--

DROP TABLE IF EXISTS `tblalumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblalumno` (
  `idAlumno` int NOT NULL AUTO_INCREMENT,
  `Nombres` varchar(45) DEFAULT NULL,
  `Apellidos` varchar(45) DEFAULT NULL,
  `Genero` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idAlumno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblalumno`
--

LOCK TABLES `tblalumno` WRITE;
/*!40000 ALTER TABLE `tblalumno` DISABLE KEYS */;
INSERT INTO `tblalumno` VALUES (1,'Eduardo','Tolentino','M'),(2,'María','Campos','F');
/*!40000 ALTER TABLE `tblalumno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblalumno_curso`
--

DROP TABLE IF EXISTS `tblalumno_curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblalumno_curso` (
  `idAlumnoCurso` int NOT NULL AUTO_INCREMENT,
  `idAlumno` int NOT NULL,
  `idCurso` char(5) NOT NULL,
  PRIMARY KEY (`idAlumnoCurso`,`idAlumno`,`idCurso`),
  KEY `fk_tblAlumno_Curso_tblAlumnos_idx` (`idAlumno`),
  KEY `fk_tblAlumno_Curso_tblCurso1_idx` (`idCurso`),
  CONSTRAINT `fk_tblAlumno_Curso_tblAlumnos` FOREIGN KEY (`idAlumno`) REFERENCES `tblalumno` (`idAlumno`),
  CONSTRAINT `fk_tblAlumno_Curso_tblCurso1` FOREIGN KEY (`idCurso`) REFERENCES `tblcurso` (`idCurso`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblalumno_curso`
--

LOCK TABLES `tblalumno_curso` WRITE;
/*!40000 ALTER TABLE `tblalumno_curso` DISABLE KEYS */;
INSERT INTO `tblalumno_curso` VALUES (1,1,'C0001'),(2,1,'C0002'),(3,2,'C0001'),(4,2,'C0002');
/*!40000 ALTER TABLE `tblalumno_curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblcurso`
--

DROP TABLE IF EXISTS `tblcurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblcurso` (
  `idCurso` char(5) NOT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Descripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idCurso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblcurso`
--

LOCK TABLES `tblcurso` WRITE;
/*!40000 ALTER TABLE `tblcurso` DISABLE KEYS */;
INSERT INTO `tblcurso` VALUES ('C0001','Comunicación','Curso de Comunicación'),('C0002','Matemática','Curso de Matemática');
/*!40000 ALTER TABLE `tblcurso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dbcolegio'
--

--
-- Dumping routines for database 'dbcolegio'
--
/*!50003 DROP PROCEDURE IF EXISTS `sp_alumnocurso_select` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_alumnocurso_select`()
BEGIN
	SELECT CONCAT(A.Nombres, ' ', A.Apellidos) AS alumno_nombre_completo, A.Genero AS alumno_genero, 
			C.Nombre AS curso_nombre, C.Descripcion AS curso_descripcion
    FROM tblalumno_curso AS AC
    INNER JOIN tblalumno AS A
		ON A.idAlumno = AC.idAlumno
	INNER JOIN tblCurso AS C
		ON C.idCurso = AC.idCurso;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-04 20:19:19
