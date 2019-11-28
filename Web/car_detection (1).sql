-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 25, 2019 at 11:28 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `car_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `car`
--

CREATE TABLE `car` (
  `car_id` int(11) NOT NULL,
  `speed` varchar(50) DEFAULT NULL,
  `car_colors` varchar(100) DEFAULT NULL,
  `car_category` varchar(100) DEFAULT NULL,
  `car_brand` varchar(100) DEFAULT NULL,
  `car_time` varchar(100) DEFAULT NULL,
  `car_image` varchar(200) DEFAULT NULL,
  `car_vid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`car_id`, `speed`, `car_colors`, `car_category`, `car_brand`, `car_time`, `car_image`, `car_vid`) VALUES
(55, '59.25222312045271', 'WHITE', 'Car_Type_1', 'HONDA', NULL, '/img/car_1.png', 10),
(56, '77.86072478914235', 'WHITE', 'Car_Type_3', 'OTHER', NULL, '/img/car_2.png', 10),
(57, '73.27038280588351', 'GRAY', 'Car_Type_3', 'TOYOTA', NULL, '/img/car_3.png', 10),
(58, '81.30029755657878', 'WHITE', 'Car_Type_1', 'TOYOTA', NULL, '/img/car_4.png', 10),
(59, '56.615997567480164', 'BLUE', 'Car_Type_2', 'TOYOTA', NULL, '/img/car_5.png', 10),
(60, '66.66499281996106', 'WHITE', 'Car_Type_3', 'HONDA', NULL, '/img/car_6.png', 10),
(61, '86.52164896754671', 'GRAY', 'Car_Type_2', 'TOYOTA', NULL, '/img/car_7.png', 10),
(62, '90.65924667065795', 'BLUE', 'Car_Type_2', 'OTHER', NULL, '/img/car_8.png', 10),
(63, '82.7513111714174', 'WHITE', 'Car_Type_3', 'OTHER', NULL, '/img/car_9.png', 10),
(64, '52.4302369292097', 'GRAY', 'Car_Type_2', 'OTHER', NULL, '/img/car_10.png', 10),
(65, '47.690527113734504', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_11.png', 10),
(66, '59.25222312045271', 'WHITE', 'Car_Type_1', 'HONDA', NULL, '/img/car_1.png', 11),
(67, '77.86072478914235', 'WHITE', 'Car_Type_3', 'OTHER', NULL, '/img/car_2.png', 11),
(68, '73.27038280588351', 'GRAY', 'Car_Type_3', 'TOYOTA', NULL, '/img/car_3.png', 11),
(69, '81.30029755657878', 'WHITE', 'Car_Type_1', 'TOYOTA', NULL, '/img/car_4.png', 11),
(70, '56.615997567480164', 'BLUE', 'Car_Type_2', 'TOYOTA', NULL, '/img/car_5.png', 11),
(71, '66.66499281996106', 'WHITE', 'Car_Type_3', 'HONDA', NULL, '/img/car_6.png', 11),
(72, '86.52164896754671', 'GRAY', 'Car_Type_2', 'TOYOTA', NULL, '/img/car_7.png', 11),
(73, '90.65924667065795', 'BLUE', 'Car_Type_2', 'OTHER', NULL, '/img/car_8.png', 11),
(74, '82.7513111714174', 'WHITE', 'Car_Type_3', 'OTHER', NULL, '/img/car_9.png', 11),
(75, '52.4302369292097', 'GRAY', 'Car_Type_2', 'OTHER', NULL, '/img/car_10.png', 11),
(76, '47.690527113734504', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_11.png', 11),
(77, '52.17007907679919', 'WHITE', 'Car_Type_1', 'HONDA', NULL, '/img/car_12.png', 11),
(78, '63.07081893339348', 'WHITE', 'Car_Type_3', 'OTHER', NULL, '/img/car_13.png', 11),
(79, '53.39683255601605', 'WHITE', 'Saloon', 'HONDA', NULL, '/img/car_14.png', 11),
(80, '76.06402360360086', 'WHITE', 'SUV', 'OTHER', NULL, '/img/car_15.png', 11),
(81, '57.66673365945722', 'GRAY', 'SUV', 'TOYOTA', NULL, '/img/car_16.png', 11),
(82, '73.9107834102567', 'WHITE', 'Saloon', 'TOYOTA', NULL, '/img/car_17.png', 11),
(83, '51.74790797694489', 'BLUE', 'PickUp', 'TOYOTA', NULL, '/img/car_18.png', 11),
(84, '63.8177794171906', 'WHITE', 'SUV', 'HONDA', NULL, '/img/car_19.png', 11),
(85, '70.63222554723643', 'GRAY', 'PickUp', 'TOYOTA', NULL, '/img/car_20.png', 11),
(86, '77.19118513632996', 'BLUE', 'PickUp', 'OTHER', NULL, '/img/car_21.png', 11),
(87, '78.67012461269928', 'WHITE', 'SUV', 'OTHER', NULL, '/img/car_22.png', 11),
(88, '54.959854080160106', 'GRAY', 'PickUp', 'OTHER', NULL, '/img/car_23.png', 11),
(89, '49.81042654028448', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_24.png', 11),
(90, '56.03715266346161', 'GRAY', 'other_Car', 'MISZUBISHI', NULL, '/img/car_25.png', 11),
(91, '69.5172560392227', 'GRAY', 'PickUp', 'ISUZU', NULL, '/img/car_26.png', 11),
(92, '60.17864246831513', 'GRAY', 'other_Car', 'TOYOTA', NULL, '/img/car_27.png', 11),
(93, '68.64801706627651', 'GRAY', 'PickUp', 'CHEVRORET', NULL, '/img/car_28.png', 11),
(94, '63.92161423097846', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_29.png', 11),
(95, '53.28651680256584', 'GRAY', 'PickUp', 'OTHER', NULL, '/img/car_30.png', 11),
(96, '70.34753400874509', 'GRAY', 'other_Carother_Car', 'ISUZU', NULL, '/img/car_31.png', 11),
(97, '61.78115909749263', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_32.png', 11),
(98, '61.12399580448366', 'BLUE', 'SUV', 'TOYOTA', NULL, '/img/car_33.png', 11),
(99, '58.88700491196512', 'GRAY', 'PickUp', 'TOYOTA', NULL, '/img/car_34.png', 11),
(100, '67.23917166821808', 'GRAY', 'SUV', 'OTHER', NULL, '/img/car_35.png', 11),
(101, '63.220473389033955', 'GRAY', 'SUV', 'TOYOTA', NULL, '/img/car_36.png', 11),
(102, '56.03193173034968', 'GRAY', 'PickUp', 'SUZUKI', NULL, '/img/car_37.png', 11),
(103, '56.06977572277173', 'GRAY', 'SUV', 'TOYOTA', NULL, '/img/car_38.png', 11),
(104, '65.3147121845454', 'GRAY', 'PickUp', 'OTHER', NULL, '/img/car_39.png', 11),
(105, '74.17753299075144', 'GRAY', 'other_Car', 'TOYOTA', NULL, '/img/car_40.png', 11),
(106, '80.85140324399009', 'GRAY', 'PickUp', 'TOYOTA', NULL, '/img/car_41.png', 11),
(107, '62.72502321970775', 'GRAY', 'SUV', 'OTHER', NULL, '/img/car_42.png', 11),
(108, '53.39683255601605', 'WHITE', 'Saloon', 'HONDA', NULL, '/img/car_1.png', 12),
(109, '76.06402360360086', 'WHITE', 'SUV', 'OTHER', NULL, '/img/car_2.png', 12),
(110, '57.66673365945722', 'GRAY', 'SUV', 'TOYOTA', NULL, '/img/car_3.png', 12),
(111, '73.9107834102567', 'WHITE', 'Saloon', 'TOYOTA', NULL, '/img/car_4.png', 12),
(112, '51.74790797694489', 'BLUE', 'PickUp', 'TOYOTA', NULL, '/img/car_5.png', 12),
(113, '63.8177794171906', 'WHITE', 'SUV', 'HONDA', NULL, '/img/car_6.png', 12),
(114, '70.63222554723643', 'GRAY', 'PickUp', 'TOYOTA', NULL, '/img/car_7.png', 12),
(115, '77.19118513632996', 'BLUE', 'PickUp', 'OTHER', NULL, '/img/car_8.png', 12),
(116, '78.67012461269928', 'WHITE', 'SUV', 'OTHER', NULL, '/img/car_9.png', 12),
(117, '54.959854080160106', 'GRAY', 'PickUp', 'OTHER', NULL, '/img/car_10.png', 12),
(118, '49.81042654028448', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_11.png', 12),
(119, '56.03715266346161', 'GRAY', 'other_Car', 'MISZUBISHI', NULL, '/img/car_12.png', 12),
(120, '69.5172560392227', 'GRAY', 'PickUp', 'ISUZU', NULL, '/img/car_13.png', 12),
(121, '60.17864246831513', 'GRAY', 'other_Car', 'TOYOTA', NULL, '/img/car_14.png', 12),
(122, '68.64801706627651', 'GRAY', 'PickUp', 'CHEVRORET', NULL, '/img/car_15.png', 12),
(123, '63.92161423097846', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_16.png', 12),
(124, '53.28651680256584', 'GRAY', 'PickUp', 'OTHER', NULL, '/img/car_17.png', 12),
(125, '70.34753400874509', 'GRAY', 'other_Carother_Car', 'ISUZU', NULL, '/img/car_18.png', 12),
(126, '61.78115909749263', 'GRAY', 'other_Car', 'OTHER', NULL, '/img/car_19.png', 12),
(127, '61.12399580448366', 'BLUE', 'SUV', 'TOYOTA', NULL, '/img/car_20.png', 12),
(128, '58.88700491196512', 'GRAY', 'PickUp', 'TOYOTA', NULL, '/img/car_21.png', 12),
(129, '67.23917166821808', 'GRAY', 'SUV', 'OTHER', NULL, '/img/car_22.png', 12),
(130, '63.220473389033955', 'GRAY', 'SUV', 'TOYOTA', NULL, '/img/car_23.png', 12),
(131, '56.03193173034968', 'GRAY', 'PickUp', 'SUZUKI', NULL, '/img/car_24.png', 12),
(132, '56.06977572277173', 'GRAY', 'SUV', 'TOYOTA', NULL, '/img/car_25.png', 12),
(133, '65.3147121845454', 'GRAY', 'PickUp', 'OTHER', NULL, '/img/car_26.png', 12),
(134, '74.17753299075144', 'GRAY', 'other_Car', 'TOYOTA', NULL, '/img/car_27.png', 12),
(135, '80.85140324399009', 'GRAY', 'PickUp', 'TOYOTA', NULL, '/img/car_28.png', 12),
(136, '62.72502321970775', 'GRAY', 'SUV', 'OTHER', NULL, '/img/car_29.png', 12);

-- --------------------------------------------------------

--
-- Table structure for table `video`
--

CREATE TABLE `video` (
  `video_id` int(11) NOT NULL,
  `video_time` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `video`
--

INSERT INTO `video` (`video_id`, `video_time`) VALUES
(10, 'Project2'),
(11, 'present'),
(12, 'pro');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`car_id`),
  ADD KEY `car_vid` (`car_vid`);

--
-- Indexes for table `video`
--
ALTER TABLE `video`
  ADD PRIMARY KEY (`video_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `car`
--
ALTER TABLE `car`
  MODIFY `car_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=137;
--
-- AUTO_INCREMENT for table `video`
--
ALTER TABLE `video`
  MODIFY `video_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `car`
--
ALTER TABLE `car`
  ADD CONSTRAINT `fk1` FOREIGN KEY (`car_vid`) REFERENCES `video` (`video_id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
