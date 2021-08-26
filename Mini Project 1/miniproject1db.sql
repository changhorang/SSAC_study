CREATE DATABASE  IF NOT EXISTS `miniprojectdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `miniprojectdb`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: miniprojectdb
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `cumulative_confirmed_data`
--

DROP TABLE IF EXISTS `cumulative_confirmed_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cumulative_confirmed_data` (
  `Area` text COLLATE utf8mb4_unicode_ci,
  `Population` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cumulative_confirmed_data`
--

LOCK TABLES `cumulative_confirmed_data` WRITE;
/*!40000 ALTER TABLE `cumulative_confirmed_data` DISABLE KEYS */;
INSERT INTO `cumulative_confirmed_data` VALUES ('검역',5761),('제주',2524),('서울',76814),('인천',11406),('광주',3948),('경북',6866),('부산',11077),('대구',13287),('강원',5268),('경기',68671),('전남',2487),('충북',4991),('충남',6639),('대전',5463),('세종',954),('전북',3441),('경남',9683),('울산',4037),('검역',5761),('제주',2524),('서울',76814),('인천',11406),('광주',3948),('경북',6866),('부산',11077),('대구',13287),('강원',5268),('경기',68671),('전남',2487),('충북',4991),('충남',6639),('대전',5463),('세종',954),('전북',3441),('경남',9683),('울산',4037);
/*!40000 ALTER TABLE `cumulative_confirmed_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cumulative_confirmed_date`
--

DROP TABLE IF EXISTS `cumulative_confirmed_date`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cumulative_confirmed_date` (
  `Date` text COLLATE utf8mb4_unicode_ci,
  `Population` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cumulative_confirmed_date`
--

LOCK TABLES `cumulative_confirmed_date` WRITE;
/*!40000 ALTER TABLE `cumulative_confirmed_date` DISABLE KEYS */;
INSERT INTO `cumulative_confirmed_date` VALUES ('8/19',2050),('8/20',1877),('8/21',1626),('8/22',1417),('8/23',1507),('8/24',2154),('8/25',1882),('8/19',2050),('8/20',1877),('8/21',1626),('8/22',1417),('8/23',1507),('8/24',2154),('8/25',1882);
/*!40000 ALTER TABLE `cumulative_confirmed_date` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'miniprojectdb'
--

--
-- Dumping routines for database 'miniprojectdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-26 18:10:45
