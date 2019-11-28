-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 10, 2019 at 10:14 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `projectcar`
--

CREATE TABLE `projectcar` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `speed` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `projectcar`
--

INSERT INTO `projectcar` (`id`, `name`, `speed`, `color`, `path`) VALUES
(135, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(136, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(137, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(138, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(139, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(140, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(141, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(142, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(143, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(144, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(145, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(146, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(147, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(148, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(149, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(150, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(151, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(152, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg'),
(153, 'Bank_Nanthawat', '100', 'Black', 'images/bankdark.jpg'),
(154, 'Arts_Phisanurat', '99', 'white', 'images/arts.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `projectcar`
--
ALTER TABLE `projectcar`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `projectcar`
--
ALTER TABLE `projectcar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
