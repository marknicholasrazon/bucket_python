-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2023 at 01:51 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python`
--

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `uniqueId` int(11) NOT NULL,
  `productId` text NOT NULL,
  `product` text NOT NULL,
  `productDescription` text NOT NULL,
  `price` text NOT NULL,
  `category` text NOT NULL,
  `stockQuantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`uniqueId`, `productId`, `product`, `productDescription`, `price`, `category`, `stockQuantity`) VALUES
(1, 'PROD001', 'Laptop', 'High-end laptop with powerful specs.', '1000', 'Electronics', 8),
(2, 'PROD002', 'T-shirt', 'Comfortable cotton t-shirt.', '20', 'Clothing', 49),
(3, 'PROD003', 'Book', 'Bestseller novel by Author.', '15', 'Books', 30),
(4, 'PROD004', 'Smartphone', 'Advanced smartphone with cutting-edge features.', '800', 'Electronics', 20),
(5, 'PROD005', 'Jeans', 'Stylish denim jeans.', '50', 'Clothing', 40),
(6, 'PROD006', 'Headphones', 'High-quality over-ear headphones for immersive audio.', '150', 'Electronics', 15),
(7, 'PROD007', 'Sunglasses', 'Designer sunglasses for a trendy look.', '80', 'Fashion Accessories', 35),
(8, 'PROD008', 'Fitness Tracker', 'Track your fitness activities and monitor your health.', '70', 'Electronics', 25),
(9, 'PROD009', 'Running Shoes', 'Lightweight and comfortable running shoes.', '90', 'Footwear', 30),
(10, 'PROD010', 'Digital Camera', 'Capture stunning photos with this advanced camera.', '600', 'Electronics', 10),
(11, 'PROD011', 'Dress Shirt', 'Formal dress shirt for special occasions.', '45', 'Clothing', 60),
(12, 'PROD012', 'Coffee Maker', 'Brew delicious coffee with this high-quality machine.', '120', 'Appliances', 15),
(13, 'PROD013', 'Backpack', 'Durable backpack for everyday use.', '40', 'Accessories', 50),
(14, 'PROD014', 'Wireless Mouse', 'Ergonomic wireless mouse for improved productivity.', '25', 'Electronics', 30),
(15, 'PROD015', 'Yoga Mat', 'Non-slip yoga mat for comfortable workouts.', '30', 'Fitness', 40),
(16, 'PROD016', 'Fiction Book', 'Engaging fiction book for avid readers.', '12', 'Books', 25),
(17, 'PROD017', 'Gaming Console', 'Enjoy gaming with this powerful gaming console.', '300', 'Electronics', 10),
(18, 'PROD018', 'Winter Jacket', 'Warm and stylish winter jacket.', '70', 'Clothing', 20),
(19, 'PROD019', 'Desk Lamp', 'Adjustable desk lamp for focused work.', '35', 'Home Office', 45),
(20, 'PROD020', 'Running Shorts', 'Comfortable shorts for your runs.', '20', 'Athletic Wear', 55),
(21, 'PROD021', 'Bluetooth Speaker', 'Portable speaker for great audio on the go.', '50', 'Electronics', 30),
(22, 'PROD022', 'Handbag', 'Fashionable handbag for any occasion.', '60', 'Fashion Accessories', 25),
(23, 'PROD023', 'Portable Charger', 'Charge your devices on the move.', '30', 'Electronics', 40),
(24, 'PROD024', 'Tennis Shoes', 'Durable tennis shoes for the court.', '75', 'Footwear', 15),
(25, 'PROD025', 'Cookware Set', 'Complete set of high-quality cookware.', '150', 'Kitchen', 10),
(26, 'PROD026', 'Sneakers', 'Casual sneakers for everyday wear.', '55', 'Footwear', 30),
(27, 'PROD027', 'Desk Organizer', 'Keep your desk tidy and organized.', '18', 'Office Supplies', 40),
(28, 'PROD028', 'Travel Mug', 'Insulated travel mug for hot beverages.', '15', 'Kitchen', 35),
(29, 'PROD029', 'Wireless Earbuds', 'Wireless earbuds for convenient listening.', '70', 'Electronics', 25),
(30, 'PROD030', 'Graphic T-shirt', 'Stylish graphic tee for a casual look.', '25', 'Clothing', 50),
(31, 'PROD031', 'Earrings', 'Elegant earrings for a touch of sophistication.', '40', 'Fashion Accessories', 20),
(32, 'PROD032', 'External Hard Drive', 'Store and backup your important data.', '80', 'Electronics', 15),
(33, 'PROD033', 'Yoga Block', 'Supportive yoga block for yoga enthusiasts.', '10', 'Fitness', 45),
(34, 'PROD034', 'Non-Stick Pan', 'Easy-to-clean non-stick frying pan.', '30', 'Kitchen', 30),
(35, 'PROD035', 'Running Jacket', 'Lightweight jacket for your runs.', '45', 'Athletic Wear', 20),
(36, 'PROD036', 'Smart Watch', 'Stay connected with this smart wearable.', '120', 'Electronics', 10),
(37, 'PROD037', 'Mug Set', 'Set of beautiful ceramic mugs for your beverages.', '25', 'Kitchen', 25),
(38, 'PROD038', 'Hair Dryer', 'Efficient hair dryer for quick styling.', '50', 'Beauty', 30),
(39, 'PROD039', 'Wall Clock', 'Stylish wall clock for your home.', '35', 'Home Decor', 25),
(40, 'PROD040', 'Resistance Bands', 'Versatile resistance bands for workouts.', '15', 'Fitness', 40),
(41, 'PROD041', 'Sweater', 'Warm and cozy sweater for chilly days.', '40', 'Clothing', 25),
(42, 'PROD042', 'Luggage Set', 'Durable luggage set for travel.', '100', 'Travel', 10),
(43, 'PROD043', 'Coffee Table', 'Modern coffee table for your living room.', '80', 'Furniture', 15),
(44, 'PROD044', 'Running Socks', 'Comfortable socks for your runs.', '8', 'Athletic Wear', 60),
(45, 'PROD045', 'Wireless Router', 'High-speed wireless router for seamless connectivity.', '70', 'Electronics', 15),
(46, 'PROD046', 'Tote Bag', 'Versatile tote bag for everyday use.', '30', 'Fashion Accessories', 35),
(47, 'PROD047', 'Stainless Steel Water Bottle', 'Durable water bottle for hydration on the go.', '20', 'Fitness', 40),
(48, 'PROD048', 'Cookbook', 'Explore new recipes with this cookbook.', '18', 'Books', 30),
(49, 'PROD049', 'Bluetooth Headset', 'Hands-free communication with this headset.', '35', 'Electronics', 20),
(50, 'PROD050', 'Pencil Set', 'Assortment of quality pencils for creative work.', '10', 'Office Supplies', 50);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`uniqueId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
