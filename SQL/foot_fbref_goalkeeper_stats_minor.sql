-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: foot
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `fbref_goalkeeper_stats_minor`
--

DROP TABLE IF EXISTS `fbref_goalkeeper_stats_minor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fbref_goalkeeper_stats_minor` (
  `index` bigint DEFAULT NULL,
  `Player` text,
  `Nation` text,
  `Pos` text,
  `Squad` text,
  `Age` bigint DEFAULT NULL,
  `Born` bigint DEFAULT NULL,
  `MP` bigint DEFAULT NULL,
  `Starts` bigint DEFAULT NULL,
  `Min` bigint DEFAULT NULL,
  `90s` double DEFAULT NULL,
  `GA` bigint DEFAULT NULL,
  `GA90` double DEFAULT NULL,
  `SoTA` bigint DEFAULT NULL,
  `Saves` bigint DEFAULT NULL,
  `Save%` double DEFAULT NULL,
  `W` bigint DEFAULT NULL,
  `D` bigint DEFAULT NULL,
  `L` bigint DEFAULT NULL,
  `CS` bigint DEFAULT NULL,
  `CS%` double DEFAULT NULL,
  `PKatt` bigint DEFAULT NULL,
  `PKA` bigint DEFAULT NULL,
  `PKsv` bigint DEFAULT NULL,
  `PKm` bigint DEFAULT NULL,
  `Save%Penalty` double DEFAULT NULL,
  `Gls` bigint DEFAULT NULL,
  `Ast` bigint DEFAULT NULL,
  `G-PK` bigint DEFAULT NULL,
  `PK` bigint DEFAULT NULL,
  `CrdY` bigint DEFAULT NULL,
  `CrdR` bigint DEFAULT NULL,
  `Gls/90` double DEFAULT NULL,
  `Ast/90` double DEFAULT NULL,
  `G+A` double DEFAULT NULL,
  `G-PK/90` double DEFAULT NULL,
  `G+A-PK` double DEFAULT NULL,
  `Mn/MP` bigint DEFAULT NULL,
  `Min%` double DEFAULT NULL,
  `Mn/Start` bigint DEFAULT NULL,
  `Compl` bigint DEFAULT NULL,
  `Subs` bigint DEFAULT NULL,
  `Mn/Sub` double DEFAULT NULL,
  `unSub` bigint DEFAULT NULL,
  `PPM` double DEFAULT NULL,
  `onG` bigint DEFAULT NULL,
  `onGA` bigint DEFAULT NULL,
  `+/-` bigint DEFAULT NULL,
  `+/-90` double DEFAULT NULL,
  `On-Off` double DEFAULT NULL,
  `2CrdY` bigint DEFAULT NULL,
  `Fls` bigint DEFAULT NULL,
  `Fld` bigint DEFAULT NULL,
  `Off` bigint DEFAULT NULL,
  `Crs` bigint DEFAULT NULL,
  `Int` bigint DEFAULT NULL,
  `TklW` bigint DEFAULT NULL,
  `PKwon` double DEFAULT NULL,
  `PKcon` double DEFAULT NULL,
  `OG` bigint DEFAULT NULL,
  `League Name` text,
  `League ID` bigint DEFAULT NULL,
  `Season` text,
  KEY `ix_fbref_goalkeeper_stats_minor_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fbref_goalkeeper_stats_minor`
--

LOCK TABLES `fbref_goalkeeper_stats_minor` WRITE;
/*!40000 ALTER TABLE `fbref_goalkeeper_stats_minor` DISABLE KEYS */;
INSERT INTO `fbref_goalkeeper_stats_minor` VALUES (17,'Alexandre Olliero','fr FRA','GK','Pau FC',25,1996,15,15,1350,15,16,1.07,50,36,72,6,3,6,5,33.3,2,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.4,15,16,-1,-0.07,NULL,0,1,3,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(19,'Anthony Racioppi','ch SUI','GK','Dijon',22,1998,1,1,90,1,1,1,6,5,83.3,0,0,1,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,0,0,0,90,6.7,90,1,0,NULL,14,0,0,1,-1,-1,-0.57,0,0,0,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(14,'Axel Maraval','fr FRA','GK','Dunkerque',28,1993,10,9,811,9,12,1.33,39,28,71.8,1,3,5,1,11.1,1,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,81,60.1,90,9,1,1,5,0.9,7,12,-5,-0.55,-0.72,0,0,2,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(20,'Baptiste Reynet','fr FRA','GK','Dijon',31,1990,14,14,1260,14,20,1.43,50,33,66,5,1,8,3,21.4,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,93.3,90,14,0,NULL,0,1.14,14,20,-6,-0.43,0.57,0,0,2,0,0,2,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(25,'Baptiste Valette','fr FRA','GK','Nancy',29,1992,3,3,270,3,4,1.33,12,8,66.7,0,2,1,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,0,0,0,90,20,90,3,0,NULL,12,0.67,3,4,-1,-0.33,0.58,0,0,2,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(13,'Benjamin Leroy','fr FRA','GK','Ajaccio',32,1989,13,13,1170,13,7,0.54,29,25,82.8,7,3,3,8,61.5,3,2,1,0,33.3,0,0,0,0,1,0,0,0,0,0,0,90,86.7,90,13,0,NULL,0,1.85,14,7,7,0.54,-0.46,0,1,1,0,0,1,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(15,'Brice Maubleu','fr FRA','GK','Grenoble',31,1989,15,15,1350,15,18,1.2,59,42,71.2,6,3,6,6,40,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.4,15,18,-3,-0.2,NULL,0,0,4,0,0,1,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(12,'Donovan Léon','gf GUF','GK','Auxerre',29,1992,15,15,1350,15,15,1,55,41,74.5,8,5,2,7,46.7,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.93,25,15,10,0.67,NULL,0,1,4,0,0,1,2,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(1,'Enzo Basilio','fr FRA','GK','Guingamp',27,1994,15,15,1350,15,20,1.33,50,33,66,4,6,5,3,20,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.2,18,20,-2,-0.13,NULL,0,1,1,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(22,'François-Joseph Sollacaro','fr FRA','GK','Ajaccio',27,1994,2,2,180,2,1,0.5,3,2,66.7,1,1,0,1,50,0,0,0,0,NULL,0,0,0,0,1,0,0,0,0,0,0,90,13.3,90,2,0,NULL,11,2.33,5,1,4,2,1.62,0,0,0,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(7,'Ivan Filipović','hr CRO','GK','Paris FC',26,1994,2,2,180,2,2,1,7,5,71.4,1,0,1,1,50,0,0,0,0,NULL,0,0,0,0,0,0,0,0,0,0,0,90,13.3,90,2,0,NULL,9,1.5,1,2,-1,-0.5,-0.81,0,0,0,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(24,'Jérémy Vachoux','fr FRA','GK','Dunkerque',27,1994,6,6,539,6,6,1,29,22,79.3,3,1,2,2,33.3,0,0,0,0,NULL,0,0,0,0,1,0,0,0,0,0,0,90,39.9,90,5,0,NULL,6,1.67,7,6,1,0.17,0.72,0,0,1,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(16,'Lionel Mpasi','cd COD','GK','Rodez Aveyron',27,1994,15,15,1350,15,16,1.07,37,24,62.2,5,4,6,5,33.3,3,2,1,0,33.3,0,0,0,0,2,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.27,16,16,0,0,NULL,0,1,3,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(3,'Lucas Chevalier','fr FRA','GK','Valenciennes',20,2001,8,8,720,8,11,1.37,35,26,74.3,3,2,3,2,25,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,53.3,90,8,0,NULL,0,1.38,8,11,-3,-0.37,0.63,0,0,1,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(5,'Lucas Dias','fr FRA','GK','Nîmes',22,1999,4,3,315,3.5,8,2.29,20,12,60,0,0,3,0,0,0,0,0,0,NULL,0,0,0,0,0,0,0,0,0,0,0,79,23.3,90,3,1,45,11,0.25,4,8,-4,-1.14,-1.32,0,0,0,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(18,'Maxence Prevot','fr FRA','GK','Sochaux',24,1997,15,15,1350,15,8,0.53,39,29,79.5,8,4,3,8,53.3,0,0,0,0,NULL,0,0,0,0,1,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.87,14,8,6,0.4,NULL,0,0,4,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(6,'Maxime Dupé','fr FRA','GK','Toulouse',28,1993,15,15,1350,15,13,0.87,41,30,73.2,8,6,1,8,53.3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,100,90,15,0,NULL,0,2,32,13,19,1.27,NULL,0,0,0,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(23,'Nathan Trott','eng ENG','GK','Nancy',22,1998,12,12,1080,12,20,1.67,59,39,66.1,2,4,6,2,16.7,1,0,0,1,NULL,0,0,0,0,1,0,0,0,0,0,0,90,80,90,12,0,NULL,2,0.83,9,20,-11,-0.92,-0.58,0,1,2,0,0,1,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(11,'Nicolas Lemaître','fr FRA','GK','Quevilly-Rouen',24,1997,15,15,1350,15,19,1.27,61,43,70.5,4,5,6,3,20,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.13,13,19,-6,-0.4,NULL,0,1,4,0,0,0,1,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(10,'Per Kristian Bråtveit','no NOR','GK','Nîmes',25,1996,12,12,1035,11.5,11,0.96,37,26,70.3,4,5,3,5,41.7,0,0,0,0,NULL,0,0,0,0,0,0,0,0,0,0,0,86,76.7,86,11,0,NULL,1,1.42,13,11,2,0.17,1.32,0,0,1,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(2,'Quentin Braat','fr FRA','GK','Niort',24,1997,15,15,1350,15,16,1.07,53,37,71.7,6,3,6,6,40,2,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.4,16,16,0,0,NULL,0,1,2,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(9,'Régis Gurtner','fr FRA','GK','Amiens',34,1986,15,15,1350,15,16,1.07,54,39,72.2,2,8,5,7,46.7,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,100,90,15,0,NULL,0,0.93,14,16,-2,-0.13,NULL,0,0,5,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(21,'Rémy Riou','fr FRA','GK','Caen',34,1987,15,15,1350,15,16,1.07,62,47,75.8,4,5,6,5,33.3,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1.13,16,16,0,0,NULL,0,1,5,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(0,'Saturnin Allagbé','bj BEN','GK','Valenciennes',27,1993,7,7,630,7,11,1.57,25,15,56,1,2,4,2,28.6,1,0,1,0,100,0,0,0,0,0,0,0,0,0,0,0,90,46.7,90,7,0,NULL,2,0.71,4,11,-7,-1,-0.63,0,0,0,0,0,0,2,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(26,'Thomas Vincensini','fr FRA','GK','Bastia',28,1993,15,15,1350,15,16,1.07,47,34,72.3,3,6,6,4,26.7,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,100,90,15,0,NULL,0,1,12,16,-4,-0.27,NULL,0,0,2,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(4,'Vincent Demarconnay','fr FRA','GK','Paris FC',38,1983,13,13,1170,13,13,1,34,22,64.7,6,3,4,4,30.8,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90,86.7,90,13,0,NULL,1,1.62,17,13,4,0.31,0.81,0,0,8,0,0,0,0,NULL,NULL,0,'Ligue-2',60,'2021-2022'),(8,'Yahia Fofana','fr FRA','GK','Le Havre',21,2000,15,15,1350,15,8,0.53,51,44,86.3,6,7,2,9,60,1,1,0,0,0,0,1,0,0,1,0,0,0.07,0.07,0,0.07,90,100,90,15,0,NULL,0,1.67,14,8,6,0.4,NULL,0,1,9,0,0,1,0,NULL,NULL,0,'Ligue-2',60,'2021-2022');
/*!40000 ALTER TABLE `fbref_goalkeeper_stats_minor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-24 10:34:10
