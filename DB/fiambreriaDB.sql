-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.18-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para fiambreria_db
CREATE DATABASE IF NOT EXISTS `fiambreria_db` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `fiambreria_db`;

-- Volcando estructura para tabla fiambreria_db.barrio
CREATE TABLE IF NOT EXISTS `barrio` (
  `id_barrio` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `id_ciudad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_barrio`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.barrio: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `barrio` DISABLE KEYS */;
INSERT INTO `barrio` (`id_barrio`, `nombre`, `id_ciudad`) VALUES
	(1, 'Nuñez', 1),
	(2, 'Urquiza', 1),
	(3, 'Martinez', 2);
/*!40000 ALTER TABLE `barrio` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.categoria
CREATE TABLE IF NOT EXISTS `categoria` (
  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) DEFAULT NULL,
  `UM` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.categoria: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `categoria` DISABLE KEYS */;
INSERT INTO `categoria` (`id_categoria`, `nombre`, `UM`) VALUES
	(1, 'Almacen', 'unidades'),
	(2, 'Quesos', 'grs'),
	(3, 'Fiambre/embutido', 'grs'),
	(4, 'Sandwich', 'unidades'),
	(5, 'Panificado', 'unidades'),
	(6, 'Dulce cajon', 'grs'),
	(7, 'Oferta combinada', 'unidades');
/*!40000 ALTER TABLE `categoria` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.ciudad
CREATE TABLE IF NOT EXISTS `ciudad` (
  `id_ciudad` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `id_provincia` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_ciudad`),
  KEY `id_provincia` (`id_provincia`),
  CONSTRAINT `ciudad_ibfk_1` FOREIGN KEY (`id_provincia`) REFERENCES `provincia` (`id_provincia`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.ciudad: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` (`id_ciudad`, `nombre`, `id_provincia`) VALUES
	(1, 'CABA', 1),
	(2, 'GBA', 1);
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.controlstock
CREATE TABLE IF NOT EXISTS `controlstock` (
  `id_ControlStock` int(11) NOT NULL AUTO_INCREMENT,
  `id_Producto` int(11) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `UM` varchar(10) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `id_local` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_ControlStock`),
  KEY `id_Producto` (`id_Producto`),
  KEY `id_categoria` (`id_categoria`),
  KEY `id_local` (`id_local`),
  CONSTRAINT `controlstock_ibfk_1` FOREIGN KEY (`id_Producto`) REFERENCES `productos` (`id_producto`),
  CONSTRAINT `controlstock_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`),
  CONSTRAINT `controlstock_ibfk_3` FOREIGN KEY (`id_local`) REFERENCES `locales` (`id_local`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.controlstock: ~28 rows (aproximadamente)
/*!40000 ALTER TABLE `controlstock` DISABLE KEYS */;
INSERT INTO `controlstock` (`id_ControlStock`, `id_Producto`, `nombre`, `id_categoria`, `UM`, `cantidad`, `id_local`) VALUES
	(1, 2, 'stock_Urquiza', 3, 'Horma', 6, 1),
	(2, 3, 'stock_Urquiza', 3, 'Horma', 2, 1),
	(3, 4, 'stock_Urquiza', 2, 'Horma', 8, 1),
	(4, 5, 'stock_Urquiza', 2, 'Horma', 3, 1),
	(5, 6, 'stock_Urquiza', 2, 'Horma', 6, 1),
	(6, 7, 'stock_Urquiza', 3, 'Horma', 5, 1),
	(7, 8, 'stock_Urquiza', 3, 'Horma', 2, 1),
	(8, 9, 'stock_Urquiza', 1, 'unidades', 60, 1),
	(9, 10, 'stock_Urquiza', 1, 'unidades', 2, 1),
	(10, 22, 'stock_Nuñez', 1, 'unidades', 6, 2),
	(11, 21, 'stock_Nuñez', 1, 'unidades', 6, 2),
	(12, 20, 'stock_Nuñez', 3, 'Horma', 0, 2),
	(13, 1, 'stock_Martinez', 3, 'Horma', 2, 3),
	(14, 2, 'stock_Martinez', 3, 'Horma', 3, 3),
	(15, 3, 'stock_Martinez', 3, 'Horma', 2, 3),
	(16, 4, 'stock_Martinez', 2, 'Horma', 8, 3),
	(17, 5, 'stock_Martinez', 2, 'Horma', 3, 3),
	(18, 6, 'stock_Martinez', 2, 'Horma', 6, 3),
	(19, 7, 'stock_Martinez', 3, 'Horma', 5, 3),
	(20, 8, 'stock_Martinez', 3, 'Horma', 2, 3),
	(21, 9, 'stock_Martinez', 1, 'unidades', 60, 3),
	(22, 10, 'stock_Martinez', 1, 'unidades', 2, 3),
	(23, 11, 'stock_Martinez', 3, 'Horma', 5, 3),
	(24, 12, 'stock_Martinez', 3, 'Horma', 2, 3),
	(25, 13, 'stock_Martinez', 1, 'Horma', 3, 3),
	(26, 14, 'stock_Martinez', 1, 'Horma', 2, 1),
	(27, 15, 'stock_Martinez', 1, 'unidades', 4, 3),
	(28, 16, 'stock_Martinez', 1, 'unidades', 4, 3);
/*!40000 ALTER TABLE `controlstock` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.factura
CREATE TABLE IF NOT EXISTS `factura` (
  `id_factura` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `medioDePago` varchar(20) DEFAULT NULL,
  `id_local` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `id_local` (`id_local`),
  CONSTRAINT `factura_ibfk_1` FOREIGN KEY (`id_local`) REFERENCES `locales` (`id_local`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.factura: ~64 rows (aproximadamente)
/*!40000 ALTER TABLE `factura` DISABLE KEYS */;
INSERT INTO `factura` (`id_factura`, `fecha`, `medioDePago`, `id_local`) VALUES
	(108, '2021-07-04 10:02:15', 'Mercado_Pago', 1),
	(109, '2021-07-04 10:02:15', 'Debito', 1),
	(110, '2021-07-04 11:09:15', 'Debito', 2),
	(111, '2021-07-04 12:44:15', 'Mercado_Pago', 2),
	(112, '2021-07-04 13:45:15', 'Efectivo', 2),
	(113, '2021-07-04 14:42:15', 'Mercado_Pago', 1),
	(114, '2021-07-04 15:41:15', 'Debito', 2),
	(115, '2021-07-04 17:10:15', 'Efectivo', 1),
	(116, '2021-07-04 10:09:15', 'Mercado_Pago', 1),
	(117, '2021-07-05 16:02:15', 'Debito', 3),
	(118, '2021-07-05 15:14:15', 'Efectivo', 1),
	(119, '2021-07-05 13:02:15', 'Mercado_Pago', 2),
	(120, '2021-07-05 10:35:15', 'Debito', 2),
	(121, '2021-07-05 11:40:15', 'Debito', 3),
	(122, '2021-07-05 11:24:15', 'Mercado_Pago', 1),
	(123, '2021-07-05 12:02:15', 'Efectivo', 2),
	(124, '2021-07-05 14:32:15', 'Mercado_Pago', 3),
	(125, '2021-07-05 13:41:15', 'Debito', 3),
	(126, '2021-07-05 15:22:15', 'Efectivo', 1),
	(127, '2021-07-06 19:33:15', 'Mercado_Pago', 1),
	(128, '2021-07-06 12:30:15', 'Debito', 3),
	(129, '2021-07-06 13:19:15', 'Efectivo', 1),
	(130, '2021-07-06 15:41:15', 'Debito', 2),
	(131, '2021-07-06 17:10:15', 'Efectivo', 1),
	(132, '2021-07-06 10:09:15', 'Mercado_Pago', 1),
	(133, '2021-07-07 16:02:15', 'Debito', 3),
	(134, '2021-07-07 15:14:15', 'Efectivo', 1),
	(135, '2021-07-07 13:02:15', 'Mercado_Pago', 2),
	(136, '2021-07-07 17:10:15', 'Efectivo', 1),
	(137, '2021-07-07 10:09:15', 'Mercado_Pago', 1),
	(138, '2021-07-07 16:02:15', 'Debito', 3),
	(139, '2021-07-07 15:14:15', 'Efectivo', 1),
	(140, '2021-07-07 13:02:15', 'Mercado_Pago', 2),
	(141, '2021-07-07 16:02:15', 'Debito', 3),
	(142, '2021-04-23 10:02:15', 'Mercado_Pago', 1),
	(143, '2021-04-23 10:02:15', 'Debito', 2),
	(144, '2021-04-23 11:09:15', 'Debito', 3),
	(145, '2021-04-23 12:44:15', 'Mercado_Pago', 1),
	(146, '2021-04-23 13:45:15', 'Efectivo', 1),
	(147, '2021-04-23 14:42:15', 'Mercado_Pago', 1),
	(148, '2021-04-23 15:41:15', 'Debito', 2),
	(149, '2021-04-24 17:10:15', 'Efectivo', 3),
	(150, '2021-04-24 10:09:15', 'Mercado_Pago', 3),
	(151, '2021-04-24 16:02:15', 'Debito', 3),
	(152, '2021-04-24 15:14:15', 'Efectivo', 1),
	(153, '2021-04-24 13:02:15', 'Mercado_Pago', 1),
	(154, '2021-04-25 10:35:15', 'Debito', 2),
	(155, '2021-04-25 11:40:15', 'Debito', 3),
	(156, '2021-04-25 11:24:15', 'Mercado_Pago', 1),
	(157, '2021-04-25 12:02:15', 'Efectivo', 1),
	(158, '2021-04-26 14:32:15', 'Mercado_Pago', 1),
	(159, '2021-04-26 13:41:15', 'Debito', 2),
	(160, '2021-04-27 15:22:15', 'Efectivo', 3),
	(161, '2021-04-27 19:33:15', 'Mercado_Pago', 3),
	(162, '2021-04-27 12:30:15', 'Debito', 3),
	(163, '2021-04-27 13:19:15', 'Efectivo', 1),
	(164, '2021-12-03 15:07:02', 'Efectivo', 3),
	(165, '2021-12-03 15:17:05', 'Efectivo', 3),
	(166, '2021-12-03 15:20:24', 'Efectivo', 3),
	(167, '2021-12-03 15:22:53', 'Efectivo', 2),
	(168, '2021-12-03 15:38:16', 'Efectivo', 2),
	(169, '2021-12-03 15:39:54', 'Mercado_Pago', 1),
	(170, '2021-12-03 15:58:03', 'Debito', 1),
	(171, '2021-12-03 16:16:26', 'Credito', 1),
	(172, '2021-12-03 16:17:47', 'Mercado_Pago', 2),
	(173, '2021-12-03 16:23:43', 'Debito', 1),
	(174, '2021-12-03 16:27:45', 'Efectivo', 1),
	(175, '2021-12-03 16:29:46', 'Mercado_Pago', 2),
	(176, '2021-12-03 16:32:44', 'Efectivo', 2),
	(177, '2021-12-03 16:34:35', 'Credito', 1),
	(178, '2021-12-03 16:39:49', 'Efectivo', 1),
	(179, '2021-12-03 16:40:51', 'Credito', 1),
	(180, '2021-12-06 16:27:59', 'Credito', 3);
/*!40000 ALTER TABLE `factura` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.facturadetalle
CREATE TABLE IF NOT EXISTS `facturadetalle` (
  `id_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `id_producto` int(11) DEFAULT NULL,
  `cantidad` float DEFAULT NULL,
  `id_factura` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `id_producto` (`id_producto`),
  KEY `id_factura` (`id_factura`),
  CONSTRAINT `facturadetalle_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`),
  CONSTRAINT `facturadetalle_ibfk_2` FOREIGN KEY (`id_factura`) REFERENCES `factura` (`id_factura`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.facturadetalle: ~98 rows (aproximadamente)
/*!40000 ALTER TABLE `facturadetalle` DISABLE KEYS */;
INSERT INTO `facturadetalle` (`id_detalle`, `id_producto`, `cantidad`, `id_factura`) VALUES
	(1, 1, 0.2, 108),
	(2, 6, 0.15, 108),
	(3, 2, 0.25, 108),
	(4, 4, 0.3, 108),
	(5, 12, 0.38, 108),
	(6, 15, 1, 109),
	(7, 2, 0.25, 109),
	(8, 4, 0.3, 109),
	(9, 15, 1, 110),
	(10, 7, 0.2, 110),
	(11, 14, 0.2, 110),
	(12, 6, 0.15, 111),
	(13, 2, 0.25, 111),
	(14, 4, 0.3, 112),
	(15, 12, 0.38, 113),
	(16, 15, 1, 113),
	(17, 2, 0.25, 113),
	(18, 4, 0.3, 114),
	(19, 15, 1, 114),
	(20, 7, 0.2, 114),
	(21, 14, 0.2, 115),
	(22, 6, 0.15, 115),
	(23, 1, 0.25, 115),
	(24, 5, 0.3, 115),
	(25, 3, 0.25, 116),
	(26, 7, 0.3, 116),
	(27, 11, 0.38, 117),
	(28, 10, 1, 117),
	(29, 2, 0.25, 117),
	(30, 4, 0.3, 118),
	(31, 9, 1, 118),
	(32, 7, 0.2, 119),
	(33, 8, 0.2, 119),
	(34, 6, 0.15, 120),
	(35, 1, 0.25, 121),
	(36, 5, 0.3, 122),
	(37, 2, 0.25, 122),
	(38, 4, 0.3, 123),
	(39, 12, 0.38, 123),
	(40, 15, 1, 124),
	(41, 2, 0.25, 125),
	(42, 4, 0.3, 125),
	(43, 6, 0.15, 126),
	(44, 1, 0.25, 126),
	(45, 5, 0.3, 127),
	(46, 2, 0.25, 127),
	(47, 4, 0.3, 128),
	(48, 12, 0.38, 129),
	(49, 15, 1, 130),
	(50, 2, 0.25, 131),
	(51, 4, 0.3, 132),
	(52, 1, 0.2, 132),
	(53, 6, 0.15, 133),
	(54, 2, 0.25, 133),
	(55, 4, 0.3, 134),
	(56, 12, 0.38, 135),
	(57, 15, 1, 136),
	(58, 2, 0.25, 136),
	(59, 15, 1, 137),
	(60, 7, 0.2, 138),
	(61, 14, 0.2, 138),
	(62, 6, 0.15, 139),
	(63, 2, 0.25, 139),
	(64, 4, 0.3, 140),
	(65, 12, 0.38, 140),
	(66, 15, 1, 141),
	(67, 2, 0.25, 141),
	(68, 4, 0.3, 141),
	(69, 7, 0.2, 138),
	(70, 14, 0.2, 139),
	(71, 6, 0.15, 140),
	(72, 2, 0.25, 140),
	(73, 4, 0.3, 141),
	(74, 12, 0.38, 141),
	(75, 15, 1, 141),
	(76, 2, 0.25, 141),
	(77, 4, 0.3, 141),
	(78, 13, 1.5, 167),
	(79, 2, 0.8, 167),
	(80, 5, 0.75, 168),
	(81, 3, 1.5, 168),
	(82, 13, 1.25, 168),
	(83, 16, 1, 168),
	(84, 3, 0.75, 169),
	(85, 5, 1, 169),
	(86, 13, 1.75, 169),
	(87, 1, 1.5, 170),
	(88, 14, 0.5, 170),
	(89, 20, 0.75, 170),
	(90, 25, 1, 170),
	(91, 1, 1.5, 171),
	(92, 16, 1, 172),
	(93, 21, 1, 172),
	(94, 22, 1, 172),
	(95, 25, 1, 172),
	(96, 23, 1, 172),
	(97, 25, 1, 173),
	(98, 24, 1, 173),
	(99, 7, 0.5, 174),
	(100, 15, 1, 175),
	(101, 25, 1, 176),
	(102, 40, 1.5, 177),
	(103, 8, 1, 178),
	(104, 15, 1, 179),
	(105, 14, 0.75, 179),
	(106, 18, 1, 179),
	(107, 20, 0.5, 179),
	(108, 21, 1, 179),
	(109, 14, 1, 180);
/*!40000 ALTER TABLE `facturadetalle` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.locales
CREATE TABLE IF NOT EXISTS `locales` (
  `id_local` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `numEmpleados` int(11) DEFAULT NULL,
  `nombreEncargado` varchar(50) DEFAULT NULL,
  `id_Barrio` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_local`),
  KEY `id_Barrio` (`id_Barrio`),
  CONSTRAINT `locales_ibfk_1` FOREIGN KEY (`id_Barrio`) REFERENCES `barrio` (`id_barrio`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.locales: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `locales` DISABLE KEYS */;
INSERT INTO `locales` (`id_local`, `nombre`, `numEmpleados`, `nombreEncargado`, `id_Barrio`) VALUES
	(1, 'local_Urquiza', 3, 'Gabriela Rivera', 2),
	(2, 'local_Nuñez', 2, 'Michelle Di Lello', 1),
	(3, 'local_Martinez', 5, 'Gabriela Gomez', 3);
/*!40000 ALTER TABLE `locales` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.pais
CREATE TABLE IF NOT EXISTS `pais` (
  `id_pais` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.pais: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `pais` DISABLE KEYS */;
INSERT INTO `pais` (`id_pais`, `nombre`) VALUES
	(1, 'Argentina');
/*!40000 ALTER TABLE `pais` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id_producto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `marca` varchar(30) DEFAULT NULL,
  `precio` float DEFAULT NULL,
  `PrecioVenta` float DEFAULT NULL,
  `id_categoria` int(11) DEFAULT NULL,
  `num_codigo` varchar(20) DEFAULT NULL,
  `id_Proveedor` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `id_categoria` (`id_categoria`),
  KEY `id_Proveedor` (`id_Proveedor`),
  CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`),
  CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`id_Proveedor`) REFERENCES `proveedores` (`id_Proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.productos: ~26 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id_producto`, `nombre`, `marca`, `precio`, `PrecioVenta`, `id_categoria`, `num_codigo`, `id_Proveedor`) VALUES
	(1, 'Jamon cocido', 'Luvianka', 350, 760, 3, '3022', 6),
	(2, 'Jamon cocido', 'Bocatti', 740, 1650, 3, '1701', 1),
	(3, 'Jamon cocido', 'Atahualpa', 640, 1390, 3, '2396', NULL),
	(4, 'Barra Dambo', 'La paulina', 490, 1060, 2, '1713', 6),
	(5, 'Barra Tybo', 'Barraza', 500, 1080, 2, NULL, NULL),
	(6, 'Barra Regio', 'La paulina', 520, 1130, 2, '3190', 6),
	(7, 'Jamon crudo', 'Atahualpa', 800, 1740, 3, NULL, NULL),
	(8, 'Jamon crudo', 'El artesano', 800, 1740, 3, '976', NULL),
	(9, 'Mayonesa 237g', 'Hellmans', 25, 54, 1, NULL, NULL),
	(10, 'Mayonesa con ajo 340g', 'Arytza', 160, 350, 1, NULL, NULL),
	(11, 'Sardo Semi estacionado', 'La paulina', 790, 1720, 2, NULL, 6),
	(12, 'Reggianito semi estacionado', 'Melincue', 850, 2000, 2, '1652', 4),
	(13, 'Reggianito estacionado', 'Marisol', 1120, 2430, 2, '50', 4),
	(14, 'Spianatta', 'El nahuelito', 800, 1740, 3, NULL, NULL),
	(15, 'Salsa Barbacoa', 'Kansas', 150, 326, 1, NULL, NULL),
	(16, 'Salsa Caesar', 'Kansas', 150, 326, 1, NULL, NULL),
	(17, 'Sardo Semi estacionado Seleccion', 'La Serenisima', 790, 1720, 2, NULL, 7),
	(18, 'Pategras', 'La Serenisima', 850, 1850, 2, NULL, 7),
	(19, 'Pategras', 'La Paulina', 1120, 2430, 2, '4121', 6),
	(20, 'Lomo horneado', 'Bocatti', 800, 1740, 3, '2033', 1),
	(21, 'Papas fritas clasicas 110grs', 'Krachitos', 150, 326, 1, NULL, 1),
	(22, 'Nachos', 'Macritas', 150, 326, 1, NULL, 4),
	(23, 'OFERTA B1', 'OFERTAS/COMBINADA', 335, 335, 7, '9100', NULL),
	(24, 'OFERTA B2', 'OFERTAS/COMBINADA', 240, 240, 7, '9102', NULL),
	(25, 'OFERTA B3', 'OFERTAS/COMBINADA', 360, 360, 7, '9103', NULL),
	(36, 'Jamon cocido natural', 'Emezeta Nativo', 0, 1300, 3, '1647', NULL),
	(37, 'Jamon Crudo', 'Sello de Oro', 230.4, 230.4, 3, NULL, NULL),
	(38, 'Jamon Crudo S/TACC', 'Sello de Oro', 990.4, 230.5, 3, '1990', 4),
	(39, 'Cheddar x100gs', 'Milkout', 4355.5, 155, 2, '3434', 3),
	(40, 'Cheddar x100gs', 'La Serenisima', 3435, 120, 2, '3435', 7),
	(41, 'Azul x100g', 'San Gotardo', 1306.4, 155, 2, '5657', 1);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.proveedores
CREATE TABLE IF NOT EXISTS `proveedores` (
  `id_Proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_Proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.proveedores: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` (`id_Proveedor`, `nombre`) VALUES
	(1, 'La Ibero'),
	(2, 'Norte distribución'),
	(3, 'Milkout'),
	(4, 'La franquicia'),
	(5, 'La preferida'),
	(6, 'La Paulina'),
	(7, 'La serenisima');
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;

-- Volcando estructura para tabla fiambreria_db.provincia
CREATE TABLE IF NOT EXISTS `provincia` (
  `id_provincia` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `id_pais` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_provincia`),
  KEY `id_pais` (`id_pais`),
  CONSTRAINT `provincia_ibfk_1` FOREIGN KEY (`id_pais`) REFERENCES `pais` (`id_pais`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.provincia: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `provincia` DISABLE KEYS */;
INSERT INTO `provincia` (`id_provincia`, `nombre`, `id_pais`) VALUES
	(1, 'Buenos Aires', 1),
	(2, 'Santa Fe', 1),
	(3, 'Misiones', 1),
	(4, 'Chubut', 1);
/*!40000 ALTER TABLE `provincia` ENABLE KEYS */;

-- Volcando estructura para procedimiento fiambreria_db.TotalVentas
DELIMITER //
CREATE PROCEDURE `TotalVentas`(IN seleccionLocal VARCHAR(50))
BEGIN
SELECT date_format(fecha,'%Y-%M-%d') AS 'dia', SUM(monto) AS 'Facturacion', COUNT(id_factura) AS 'numFacturas',
case 
when SUM(monto) > 2500 then 'Bien'
when SUM(monto) < 1000 then 'Bajo'
ELSE 'Regular'
END AS 'Observacion'
from vista_ventas_locales 
WHERE vista_ventas_locales.local_nombre = seleccionLocal
GROUP BY dia,local_nombre;

END//
DELIMITER ;

-- Volcando estructura para tabla fiambreria_db.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) DEFAULT NULL,
  `mail` varchar(30) DEFAULT NULL,
  `clave` binary(64) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla fiambreria_db.usuarios: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id_usuario`, `nombre`, `mail`, `clave`) VALUES
	(1, 'Romina', 'fiambreria@gmail.com', _binary 0x49303531626D56364D54497A4E44553D000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000),
	(2, 'Gabriela', 'urquiza@gmail.com', _binary 0x4931567963585670656D45784D6A4D304E513D3D0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000),
	(3, 'Laura', 'laura@gmail.com', _binary 0x49314A7662576C75595445794D7A5131000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

-- Volcando estructura para vista fiambreria_db.vista_controlstock
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `vista_controlstock` (
	`nombre` VARCHAR(50) NULL COLLATE 'latin1_swedish_ci',
	`producto` VARCHAR(81) NULL COLLATE 'latin1_swedish_ci',
	`categoria` VARCHAR(20) NULL COLLATE 'latin1_swedish_ci',
	`UM` VARCHAR(10) NULL COLLATE 'latin1_swedish_ci',
	`cantidad` INT(11) NULL
) ENGINE=MyISAM;

-- Volcando estructura para vista fiambreria_db.vista_productos
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `vista_productos` (
	`id_producto` INT(11) NOT NULL,
	`producto` VARCHAR(81) NULL COLLATE 'latin1_swedish_ci',
	`PrecioVenta` FLOAT NULL,
	`Venta por` VARCHAR(10) NULL COLLATE 'latin1_swedish_ci',
	`categoria` VARCHAR(20) NULL COLLATE 'latin1_swedish_ci',
	`Proveedor` VARCHAR(50) NULL COLLATE 'latin1_swedish_ci'
) ENGINE=MyISAM;

-- Volcando estructura para vista fiambreria_db.vista_ventas_locales
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `vista_ventas_locales` (
	`fecha` DATETIME NULL,
	`medioDePago` VARCHAR(20) NULL COLLATE 'latin1_swedish_ci',
	`id_factura` INT(11) NOT NULL,
	`Monto` DOUBLE(19,2) NULL,
	`local_nombre` VARCHAR(50) NULL COLLATE 'latin1_swedish_ci'
) ENGINE=MyISAM;

-- Volcando estructura para vista fiambreria_db.vista_controlstock
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `vista_controlstock`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vista_controlstock` AS SELECT locales.nombre,CONCAT( productos.nombre,SPACE(1), productos.marca) AS 'producto',categoria.nombre AS 'categoria',controlstock.UM,controlstock.cantidad
FROM locales
INNER JOIN controlstock ON locales.id_local = controlstock.id_local
INNER JOIN productos ON controlstock.id_Producto = productos.id_producto
INNER JOIN categoria ON controlstock.id_categoria = categoria.id_categoria ;

-- Volcando estructura para vista fiambreria_db.vista_productos
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `vista_productos`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vista_productos` AS SELECT id_producto, CONCAT( productos.nombre,SPACE(1), productos.marca) AS producto, PrecioVenta,categoria.UM AS 'Venta por', categoria.nombre AS 'categoria',proveedores.nombre AS 'Proveedor'
FROM productos
left JOIN proveedores ON productos.id_proveedor = proveedores.id_Proveedor
LEFT JOIN categoria ON productos.id_categoria = categoria.id_categoria ;

-- Volcando estructura para vista fiambreria_db.vista_ventas_locales
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `vista_ventas_locales`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vista_ventas_locales` AS SELECT fecha, medioDePago,factura.id_factura, SUM(round(productos.PrecioVenta*cantidad , 2)) AS 'Monto',locales.nombre AS 'local_nombre'
FROM factura
INNER JOIN locales ON factura.id_local = locales.id_local
INNER JOIN facturadetalle ON factura.id_factura = facturadetalle.id_factura
INNER JOIN productos ON facturadetalle.id_producto = productos.id_producto
GROUP BY id_factura ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
