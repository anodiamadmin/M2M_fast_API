-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               12.0.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.11.0.7065
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table micro2move.tokens
CREATE TABLE IF NOT EXISTS `tokens` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `token` varchar(512) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  KEY `ix_tokens_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table micro2move.tokens: ~2 rows (approximately)
INSERT INTO `tokens` (`id`, `user_id`, `token`) VALUES
	(18, 2, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyfQ._gCJnNHUpkjngQu0goAjddY3LftjY6C__JuAnXzw6Ps'),
	(25, 6, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2fQ.Ch3Ut1eXpk4nWPpCm1qspdJlWkbvkhfmp0MbxXj3EBI');

-- Dumping structure for table micro2move.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `hashed_password` varchar(255) NOT NULL,
  `date_of_birth` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  KEY `ix_users_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table micro2move.users: ~4 rows (approximately)
INSERT INTO `users` (`id`, `full_name`, `email`, `hashed_password`, `date_of_birth`) VALUES
	(1, 'Sayan Basak', 'sayan@anodiam.com', '$argon2id$v=19$m=65536,t=3,p=4$5JzTuvee816LsRYihLB2Dg$hX7UUsZBYFMH1vDpveQQMaGjnrTzT2gmNnRiE0nNsLo', '2001-11-11'),
	(4, 'Atish Roy', 'royatish005@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$HKM0hpByrtVaq3XuvbfWGg$0DVYhEEEXN/h3oebZE6mstyOaUg7u+6znZ1t6ZtoXS4', '2003-08-27'),
	(5, 'Alekhya Banerjee', 'alekhyabanodiam@gmail.com', '$argon2id$v=19$m=65536,t=3,p=4$FOJcK4XQGqO0Nqb03huj1A$sHrHHFm8nb+XT/QovilLxlLTdbTctStkyG3vy9Ni7RA', '2004-08-11'),
	(6, 'Sayan', 'sayan@mail.com', '$argon2id$v=19$m=65536,t=3,p=4$y9m711prTQmhdG6t1ToHQA$4DLGjrx2IlbxAGwuuRjQaqanxeJ6cyiAZeTG3n8vAmw', '2010-01-16');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
