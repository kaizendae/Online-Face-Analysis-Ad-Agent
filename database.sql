-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for ads_agent
CREATE DATABASE IF NOT EXISTS `ads_agent` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `ads_agent`;

-- Dumping structure for table ads_agent.ads
CREATE TABLE IF NOT EXISTS `ads` (
  `id` int(11) NOT NULL,
  `gender` text,
  `age` text,
  `image` varchar(191) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- Dumping data for table ads_agent.ads: 20 rows
/*!40000 ALTER TABLE `ads` DISABLE KEYS */;
INSERT INTO `ads` (`id`, `gender`, `age`, `image`) VALUES
	(1, 'Male', '25-64', 'static/2.png'),
	(4, 'Male', '65+', 'static/4.png'),
	(2, 'Female', '15-17', 'static/3.png'),
	(3, 'Female', '18-24', 'static/3.png'),
	(5, 'Female', '65+', 'static/4.png'),
	(6, 'Female', '25-64', 'static/5.png'),
	(7, 'Male', '25-64', 'static/5.png'),
	(8, 'Male', '18-24', 'static/6.png'),
	(9, 'Female', '1-14', 'static/7.png'),
	(10, 'Male', '1-14', 'static/8.png'),
	(11, 'Female', '18-24', 'static/9.png'),
	(12, 'Male', '18-24', 'static/13.png'),
	(13, 'Male', '15-17', 'static/1.png'),
	(14, 'Female', '25-64', 'static/10.jpg'),
	(15, 'Female', '65+', 'static/11.jpg'),
	(16, 'Male', '65+', 'static/12.jpg'),
	(17, 'Male', '1-14', 'static/14.png'),
	(18, 'Female', '1-14', 'static/15.png'),
	(19, 'Male', '15-17', 'static/17.png'),
	(20, 'Female', '15-17', 'static/16.png');
/*!40000 ALTER TABLE `ads` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
