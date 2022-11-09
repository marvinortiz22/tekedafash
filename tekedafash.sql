-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-11-2022 a las 19:25:17
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tekedafash`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_usuario`
--

CREATE TABLE `administrador_usuario` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `documento` varchar(9) NOT NULL,
  `nacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `administrador_usuario`
--

INSERT INTO `administrador_usuario` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `documento`, `nacimiento`) VALUES
(1, 'pbkdf2_sha256$320000$y6yKj0ypErikGyDQY0WsmV$BYbUHSW5sSyDbygwI33qqXH6Ab7kKG7AvieJCpnCDDU=', '2022-11-08 17:59:50.529919', 1, 'Kevin', 'Kevin', 'Agreda', 'kevin.ale24@gmail.com', 0, 1, '2022-11-08 16:52:30.442468', '012345678', '2000-11-07'),
(2, 'pbkdf2_sha256$320000$BRiXKQccNxgnie7ZG7rsEa$Apg5Hy/n/WOa+VtkRI0rBjsr+3fS7B3oWbpq1Ojs9sA=', NULL, 1, 'Gerardo', 'Gerardo', 'Navarro', 'prueba@gmail.com', 1, 1, '2022-11-08 18:24:02.605021', '012345679', '2001-11-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_usuario_groups`
--

CREATE TABLE `administrador_usuario_groups` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administrador_usuario_user_permissions`
--

CREATE TABLE `administrador_usuario_user_permissions` (
  `id` bigint(20) NOT NULL,
  `usuario_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add tipo prenda', 6, 'add_tipoprenda'),
(22, 'Can change tipo prenda', 6, 'change_tipoprenda'),
(23, 'Can delete tipo prenda', 6, 'delete_tipoprenda'),
(24, 'Can view tipo prenda', 6, 'view_tipoprenda'),
(25, 'Can add user', 7, 'add_usuario'),
(26, 'Can change user', 7, 'change_usuario'),
(27, 'Can delete user', 7, 'delete_usuario'),
(28, 'Can view user', 7, 'view_usuario'),
(29, 'Can add talla', 8, 'add_talla'),
(30, 'Can change talla', 8, 'change_talla'),
(31, 'Can delete talla', 8, 'delete_talla'),
(32, 'Can view talla', 8, 'view_talla'),
(33, 'Can add prenda', 9, 'add_prenda'),
(34, 'Can change prenda', 9, 'change_prenda'),
(35, 'Can delete prenda', 9, 'delete_prenda'),
(36, 'Can view prenda', 9, 'view_prenda'),
(37, 'Can add inventario', 10, 'add_inventario'),
(38, 'Can change inventario', 10, 'change_inventario'),
(39, 'Can delete inventario', 10, 'delete_inventario'),
(40, 'Can view inventario', 10, 'view_inventario'),
(41, 'Can add orden', 11, 'add_orden'),
(42, 'Can change orden', 11, 'change_orden'),
(43, 'Can delete orden', 11, 'delete_orden'),
(44, 'Can view orden', 11, 'view_orden'),
(45, 'Can add detalle de orden', 12, 'add_detalledeorden'),
(46, 'Can change detalle de orden', 12, 'change_detalledeorden'),
(47, 'Can delete detalle de orden', 12, 'delete_detalledeorden'),
(48, 'Can view detalle de orden', 12, 'view_detalledeorden');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleorden`
--

CREATE TABLE `detalleorden` (
  `id` bigint(20) NOT NULL,
  `costo` double NOT NULL,
  `precio` double NOT NULL,
  `cantidad` double NOT NULL,
  `inventario_id` bigint(20) NOT NULL,
  `orden_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `detalleorden`
--

INSERT INTO `detalleorden` (`id`, `costo`, `precio`, `cantidad`, `inventario_id`, `orden_id`) VALUES
(1, 10, 12, 2, 1, 1),
(2, 10, 12, 1, 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'Administrador', 'inventario'),
(9, 'Administrador', 'prenda'),
(8, 'Administrador', 'talla'),
(6, 'Administrador', 'tipoprenda'),
(7, 'Administrador', 'usuario'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(12, 'Cliente', 'detalledeorden'),
(11, 'Cliente', 'orden'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-11-08 16:48:42.846999'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-11-08 16:48:43.676114'),
(3, 'auth', '0001_initial', '2022-11-08 16:48:48.526469'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-11-08 16:48:49.701264'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-11-08 16:48:49.942209'),
(6, 'auth', '0004_alter_user_username_opts', '2022-11-08 16:48:50.281616'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-11-08 16:48:50.385548'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-11-08 16:48:50.473490'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-11-08 16:48:50.585415'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-11-08 16:48:50.665360'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-11-08 16:48:50.761480'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-11-08 16:48:50.980799'),
(13, 'auth', '0011_update_proxy_permissions', '2022-11-08 16:48:51.067429'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-11-08 16:48:51.162417'),
(15, 'Administrador', '0001_initial', '2022-11-08 16:49:02.621062'),
(16, 'Administrador', '0002_alter_inventario_cantidad', '2022-11-08 16:49:02.906342'),
(17, 'Administrador', '0003_alter_inventario_cantidad', '2022-11-08 16:49:03.138242'),
(18, 'Cliente', '0001_initial', '2022-11-08 16:49:07.560482'),
(19, 'admin', '0001_initial', '2022-11-08 16:49:09.473744'),
(20, 'admin', '0002_logentry_remove_auto_add', '2022-11-08 16:49:09.580270'),
(21, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-08 16:49:09.652272'),
(22, 'sessions', '0001_initial', '2022-11-08 16:49:10.121210');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('9zzs3qff94e5gt55z6i9oa04uz0e39ct', 'eyJfcGFzc3dvcmRfcmVzZXRfdG9rZW4iOiJiZWtrZDYtMDEzZGFkMGM1NDAyYTUxYjdkMzE1MTczZWE0ZTY5YzEiLCJjYXJyaXRvIjpbXX0:1osTA8:IjcSwrcDeF_Jths6ryUvPjcIqTo50TkHph5P7e39Rko', '2022-11-22 18:17:28.678567');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `prenda_id` bigint(20) NOT NULL,
  `talla_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`id`, `cantidad`, `prenda_id`, `talla_id`) VALUES
(1, 10, 1, 2),
(2, 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `orden`
--

CREATE TABLE `orden` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `cliente_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `orden`
--

INSERT INTO `orden` (`id`, `fecha`, `cliente_id`) VALUES
(1, '2022-11-02 15:53:47.000000', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prenda`
--

CREATE TABLE `prenda` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `descripcion` varchar(120) NOT NULL,
  `costo` double NOT NULL,
  `precioVenta` double NOT NULL,
  `visibilidad` int(11) NOT NULL,
  `urlFoto` varchar(400) NOT NULL,
  `tipoPrenda_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `prenda`
--

INSERT INTO `prenda` (`id`, `nombre`, `descripcion`, `costo`, `precioVenta`, `visibilidad`, `urlFoto`, `tipoPrenda_id`) VALUES
(1, 'Blusa roja', 'Blusa de color rojo', 10, 12, 1, 'https://http2.mlstatic.com/D_NQ_NP_925651-MLM45142790080_032021-W.jpg', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `talla`
--

CREATE TABLE `talla` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `tipoPrenda_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `talla`
--

INSERT INTO `talla` (`id`, `nombre`, `tipoPrenda_id`) VALUES
(2, 'M', 1),
(1, 'S', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoprenda`
--

CREATE TABLE `tipoprenda` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipoprenda`
--

INSERT INTO `tipoprenda` (`id`, `nombre`) VALUES
(1, 'Blusas'),
(2, 'Pantalones');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administrador_usuario`
--
ALTER TABLE `administrador_usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `documento` (`documento`);

--
-- Indices de la tabla `administrador_usuario_groups`
--
ALTER TABLE `administrador_usuario_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Administrador_usuario_groups_usuario_id_group_id_4252ebd4_uniq` (`usuario_id`,`group_id`),
  ADD KEY `Administrador_usuario_groups_group_id_94c2b7a0_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `administrador_usuario_user_permissions`
--
ALTER TABLE `administrador_usuario_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Administrador_usuario_us_usuario_id_permission_id_b4ec5708_uniq` (`usuario_id`,`permission_id`),
  ADD KEY `Administrador_usuari_permission_id_e3281db5_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `detalleorden`
--
ALTER TABLE `detalleorden`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `detalleOrden_orden_id_inventario_id_8b7e623a_uniq` (`orden_id`,`inventario_id`),
  ADD KEY `detalleOrden_inventario_id_ceffad8f_fk_inventario_id` (`inventario_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_Administrador_usuario_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `inventario_prenda_id_talla_id_5882c873_uniq` (`prenda_id`,`talla_id`),
  ADD KEY `inventario_talla_id_e34b1f5d_fk_talla_id` (`talla_id`);

--
-- Indices de la tabla `orden`
--
ALTER TABLE `orden`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orden_cliente_id_c5b16822_fk_Administrador_usuario_id` (`cliente_id`);

--
-- Indices de la tabla `prenda`
--
ALTER TABLE `prenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `prenda_nombre_descripcion_urlFoto_tipoPrenda_id_8d8bc9cb_uniq` (`nombre`,`descripcion`,`urlFoto`,`tipoPrenda_id`),
  ADD KEY `prenda_tipoPrenda_id_c8894c7e_fk_tipoPrenda_id` (`tipoPrenda_id`);

--
-- Indices de la tabla `talla`
--
ALTER TABLE `talla`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `talla_nombre_tipoPrenda_id_07b7c6b0_uniq` (`nombre`,`tipoPrenda_id`),
  ADD KEY `talla_tipoPrenda_id_b936355e_fk_tipoPrenda_id` (`tipoPrenda_id`);

--
-- Indices de la tabla `tipoprenda`
--
ALTER TABLE `tipoprenda`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administrador_usuario`
--
ALTER TABLE `administrador_usuario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `administrador_usuario_groups`
--
ALTER TABLE `administrador_usuario_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `administrador_usuario_user_permissions`
--
ALTER TABLE `administrador_usuario_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `detalleorden`
--
ALTER TABLE `detalleorden`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `orden`
--
ALTER TABLE `orden`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `prenda`
--
ALTER TABLE `prenda`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `talla`
--
ALTER TABLE `talla`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipoprenda`
--
ALTER TABLE `tipoprenda`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `administrador_usuario_groups`
--
ALTER TABLE `administrador_usuario_groups`
  ADD CONSTRAINT `Administrador_usuari_usuario_id_a0651ad2_fk_Administr` FOREIGN KEY (`usuario_id`) REFERENCES `administrador_usuario` (`id`),
  ADD CONSTRAINT `Administrador_usuario_groups_group_id_94c2b7a0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `administrador_usuario_user_permissions`
--
ALTER TABLE `administrador_usuario_user_permissions`
  ADD CONSTRAINT `Administrador_usuari_permission_id_e3281db5_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `Administrador_usuari_usuario_id_eb4065df_fk_Administr` FOREIGN KEY (`usuario_id`) REFERENCES `administrador_usuario` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `detalleorden`
--
ALTER TABLE `detalleorden`
  ADD CONSTRAINT `detalleOrden_inventario_id_ceffad8f_fk_inventario_id` FOREIGN KEY (`inventario_id`) REFERENCES `inventario` (`id`),
  ADD CONSTRAINT `detalleOrden_orden_id_8ac68d4a_fk_orden_id` FOREIGN KEY (`orden_id`) REFERENCES `orden` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Administrador_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `administrador_usuario` (`id`);

--
-- Filtros para la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD CONSTRAINT `inventario_prenda_id_6720efb3_fk_prenda_id` FOREIGN KEY (`prenda_id`) REFERENCES `prenda` (`id`),
  ADD CONSTRAINT `inventario_talla_id_e34b1f5d_fk_talla_id` FOREIGN KEY (`talla_id`) REFERENCES `talla` (`id`);

--
-- Filtros para la tabla `orden`
--
ALTER TABLE `orden`
  ADD CONSTRAINT `orden_cliente_id_c5b16822_fk_Administrador_usuario_id` FOREIGN KEY (`cliente_id`) REFERENCES `administrador_usuario` (`id`);

--
-- Filtros para la tabla `prenda`
--
ALTER TABLE `prenda`
  ADD CONSTRAINT `prenda_tipoPrenda_id_c8894c7e_fk_tipoPrenda_id` FOREIGN KEY (`tipoPrenda_id`) REFERENCES `tipoprenda` (`id`);

--
-- Filtros para la tabla `talla`
--
ALTER TABLE `talla`
  ADD CONSTRAINT `talla_tipoPrenda_id_b936355e_fk_tipoPrenda_id` FOREIGN KEY (`tipoPrenda_id`) REFERENCES `tipoprenda` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
