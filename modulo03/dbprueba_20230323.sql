CREATE DATABASE  IF NOT EXISTS `dbprueba` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dbprueba`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: dbprueba
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
-- Table structure for table `tblestudiante`
--

DROP TABLE IF EXISTS `tblestudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblestudiante` (
  `idestudiante` int NOT NULL AUTO_INCREMENT,
  `idpersona` int NOT NULL,
  `idseccion` int NOT NULL,
  `estado` char(1) DEFAULT NULL,
  PRIMARY KEY (`idestudiante`,`idpersona`,`idseccion`),
  KEY `idpersona_idx` (`idpersona`),
  KEY `idseccion_idx` (`idseccion`),
  CONSTRAINT `idpersona` FOREIGN KEY (`idpersona`) REFERENCES `tblpersona` (`idpersona`),
  CONSTRAINT `idseccion` FOREIGN KEY (`idseccion`) REFERENCES `tblseccion` (`idseccion`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblestudiante`
--

LOCK TABLES `tblestudiante` WRITE;
/*!40000 ALTER TABLE `tblestudiante` DISABLE KEYS */;
INSERT INTO `tblestudiante` VALUES (1,1,1,'1'),(2,2,1,'1'),(3,3,1,'1'),(4,4,2,'1'),(5,5,2,'1'),(6,6,2,'1'),(7,7,3,'1'),(8,8,3,'1'),(9,9,2,'1'),(10,10,3,'1');
/*!40000 ALTER TABLE `tblestudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblpersona`
--

DROP TABLE IF EXISTS `tblpersona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblpersona` (
  `idpersona` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `tipo_doc` char(1) DEFAULT NULL,
  `num_docu` char(12) DEFAULT NULL,
  `direccion` varchar(250) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `fec_nacimiento` date DEFAULT NULL,
  `genero` char(1) DEFAULT NULL,
  `estado` char(1) DEFAULT NULL,
  PRIMARY KEY (`idpersona`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblpersona`
--

LOCK TABLES `tblpersona` WRITE;
/*!40000 ALTER TABLE `tblpersona` DISABLE KEYS */;
INSERT INTO `tblpersona` VALUES (1,'Eduardo','Tolentino','1','87654321','Direccion 01','987654321','1995-12-12','M','1'),(2,'Carlos','Diaz','1','87654322','Direccion 02','987654322','1995-11-22','M','1'),(3,'Maria','Gonzales','1','87654323','Direccion 03','987654323','1995-10-05','F','1'),(4,'Sara','Perez','1','87654324','Direccion 04','987654324','1995-10-06','F','1'),(5,'Marta','Rojas','1','87654325','Direccion 05','987654325','1995-10-07','F','1'),(6,'Jose','Quispe','1','87654326','Direccion 06','987654326','1995-10-08','M','1'),(7,'Marcos','Camargo','1','87654327','Direccion 07','987654327','1995-10-09','M','1'),(8,'Luis','Prado','1','87654328','Direccion 08','987654328','1995-10-10','M','1'),(9,'Luis','Quinto','1','87654329','Direccion 09','987654329','1995-10-11','M','1'),(10,'Liliana','Perez','1','87654330','Direccion 10','987654330','1995-10-12','F','1');
/*!40000 ALTER TABLE `tblpersona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblseccion`
--

DROP TABLE IF EXISTS `tblseccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblseccion` (
  `idseccion` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `descripcion` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`idseccion`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblseccion`
--

LOCK TABLES `tblseccion` WRITE;
/*!40000 ALTER TABLE `tblseccion` DISABLE KEYS */;
INSERT INTO `tblseccion` VALUES (1,'A','Alumnos con notas de 20 a 17'),(2,'B','Alumnos con notas de 16 a 14'),(3,'C','Alumnos con notas de 13 a 0');
/*!40000 ALTER TABLE `tblseccion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-23 22:15:58
