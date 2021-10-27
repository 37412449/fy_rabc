/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50629
 Source Host           : localhost:3306
 Source Schema         : fy_rabc

 Target Server Type    : MySQL
 Target Server Version : 50629
 File Encoding         : 65001

 Date: 14/09/2021 15:54:43
*/

CREATE DATABASE IF NOT EXISTS fy_rabc DEFAULT CHARSET utf8mb4;

use fy_rabc;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 65 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add Token', 7, 'add_token');
INSERT INTO `auth_permission` VALUES (26, 'Can change Token', 7, 'change_token');
INSERT INTO `auth_permission` VALUES (27, 'Can delete Token', 7, 'delete_token');
INSERT INTO `auth_permission` VALUES (28, 'Can view Token', 7, 'view_token');
INSERT INTO `auth_permission` VALUES (29, 'Can add token', 8, 'add_tokenproxy');
INSERT INTO `auth_permission` VALUES (30, 'Can change token', 8, 'change_tokenproxy');
INSERT INTO `auth_permission` VALUES (31, 'Can delete token', 8, 'delete_tokenproxy');
INSERT INTO `auth_permission` VALUES (32, 'Can view token', 8, 'view_tokenproxy');
INSERT INTO `auth_permission` VALUES (33, 'Can add 公司信息管理', 9, 'add_companymodel');
INSERT INTO `auth_permission` VALUES (34, 'Can change 公司信息管理', 9, 'change_companymodel');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 公司信息管理', 9, 'delete_companymodel');
INSERT INTO `auth_permission` VALUES (36, 'Can view 公司信息管理', 9, 'view_companymodel');
INSERT INTO `auth_permission` VALUES (37, 'Can add 参数配置管理', 10, 'add_configmodel');
INSERT INTO `auth_permission` VALUES (38, 'Can change 参数配置管理', 10, 'change_configmodel');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 参数配置管理', 10, 'delete_configmodel');
INSERT INTO `auth_permission` VALUES (40, 'Can view 参数配置管理', 10, 'view_configmodel');
INSERT INTO `auth_permission` VALUES (41, 'Can add 组织架构管理', 11, 'add_orgmodel');
INSERT INTO `auth_permission` VALUES (42, 'Can change 组织架构管理', 11, 'change_orgmodel');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 组织架构管理', 11, 'delete_orgmodel');
INSERT INTO `auth_permission` VALUES (44, 'Can view 组织架构管理', 11, 'view_orgmodel');
INSERT INTO `auth_permission` VALUES (45, 'Can add 菜单资源管理', 12, 'add_resourcemodel');
INSERT INTO `auth_permission` VALUES (46, 'Can change 菜单资源管理', 12, 'change_resourcemodel');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 菜单资源管理', 12, 'delete_resourcemodel');
INSERT INTO `auth_permission` VALUES (48, 'Can view 菜单资源管理', 12, 'view_resourcemodel');
INSERT INTO `auth_permission` VALUES (49, 'Can add 角色信息管理', 13, 'add_rolemodel');
INSERT INTO `auth_permission` VALUES (50, 'Can change 角色信息管理', 13, 'change_rolemodel');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 角色信息管理', 13, 'delete_rolemodel');
INSERT INTO `auth_permission` VALUES (52, 'Can view 角色信息管理', 13, 'view_rolemodel');
INSERT INTO `auth_permission` VALUES (53, 'Can add 角色资源管理', 14, 'add_roleresmodel');
INSERT INTO `auth_permission` VALUES (54, 'Can change 角色资源管理', 14, 'change_roleresmodel');
INSERT INTO `auth_permission` VALUES (55, 'Can delete 角色资源管理', 14, 'delete_roleresmodel');
INSERT INTO `auth_permission` VALUES (56, 'Can view 角色资源管理', 14, 'view_roleresmodel');
INSERT INTO `auth_permission` VALUES (57, 'Can add 用户信息管理', 15, 'add_usermodel');
INSERT INTO `auth_permission` VALUES (58, 'Can change 用户信息管理', 15, 'change_usermodel');
INSERT INTO `auth_permission` VALUES (59, 'Can delete 用户信息管理', 15, 'delete_usermodel');
INSERT INTO `auth_permission` VALUES (60, 'Can view 用户信息管理', 15, 'view_usermodel');
INSERT INTO `auth_permission` VALUES (61, 'Can add 用户角色管理', 16, 'add_userrolemodel');
INSERT INTO `auth_permission` VALUES (62, 'Can change 用户角色管理', 16, 'change_userrolemodel');
INSERT INTO `auth_permission` VALUES (63, 'Can delete 用户角色管理', 16, 'delete_userrolemodel');
INSERT INTO `auth_permission` VALUES (64, 'Can view 用户角色管理', 16, 'view_userrolemodel');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$260000$yxHQdc9elq55hlniP0IiuD$Tyi0MHM+Yok47s852+XY8obQF0Zn9wAsr72cGRBE1gE=', '2021-09-29 10:06:23.109915', 0, 'admin', '', '', '123456@qq.com', 1, 1, '2021-09-14 14:48:39.822392');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for authtoken_token
-- ----------------------------
DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE `authtoken_token`  (
  `key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id`) USING BTREE,
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of authtoken_token
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 71 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2021-09-14 14:50:55.684583', '1', '系统管理', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (2, '2021-09-14 14:51:32.305906', '2', '基础设置', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (3, '2021-09-14 14:52:23.330193', '3', '组织架构管理', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (4, '2021-09-14 14:52:53.325491', '4', '系统资源管理', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (5, '2021-09-14 14:53:56.769242', '5', '角色信息管理', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (6, '2021-09-14 14:54:20.096800', '6', '用户信息管理', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (7, '2021-09-14 14:55:03.675216', '7', '角色用户设置', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (8, '2021-09-14 14:55:28.462896', '8', '角色资源设置', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (9, '2021-09-14 14:55:50.906600', '9', '系统参数管理', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (10, '2021-09-14 14:57:48.841103', '10', '查看', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (11, '2021-09-14 14:58:14.150412', '11', '查看', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (12, '2021-09-14 14:58:28.293296', '10', '查看', 2, '[{\"changed\": {\"fields\": [\"\\u8d44\\u6e90\\u7c7b\\u578b\"]}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (13, '2021-09-14 14:58:45.093780', '12', '查看', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (14, '2021-09-14 14:59:04.428504', '13', '查看', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (15, '2021-09-14 14:59:26.306548', '14', '查看', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (16, '2021-09-14 14:59:54.996092', '15', '查看', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (17, '2021-09-14 15:00:10.178052', '16', '查看', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (18, '2021-09-14 15:02:38.033844', '17', '新增', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (19, '2021-09-14 15:03:11.872008', '18', '新增', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (20, '2021-09-14 15:03:47.156996', '19', '新增', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (21, '2021-09-14 15:04:06.408941', '20', '新增', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (22, '2021-09-14 15:05:51.881078', '21', '修改', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (23, '2021-09-14 15:06:16.034599', '22', '修改', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (24, '2021-09-14 15:06:51.393635', '23', '修改', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (25, '2021-09-14 15:07:08.972688', '24', '修改', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (26, '2021-09-14 15:07:23.216538', '25', '修改', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (27, '2021-09-14 15:07:39.117278', '26', '修改', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (28, '2021-09-14 15:09:29.332360', '27', '修改', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (29, '2021-09-14 15:09:53.556682', '28', '新增', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (30, '2021-09-14 15:11:58.426176', '1', '管理员', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (31, '2021-09-14 15:14:30.078816', '1', 'OGD-6FF6-152B-11EC-AE7A-94C691099607', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (32, '2021-09-14 15:15:24.010468', '2', 'OGG-98FE-152B-11EC-8FE2-94C691099607', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (33, '2021-09-14 15:16:33.927766', '3', 'OGP-4886-152B-11EC-90DF-94C691099607', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (34, '2021-09-14 15:37:21.844578', '1', '联想中国', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (35, '2021-09-14 15:40:10.970450', '1', 'U-R-AF4C-152E-11EC-92BD-94C691099607', 1, '[{\"added\": {}}]', 16, 1);
INSERT INTO `django_admin_log` VALUES (36, '2021-09-14 15:40:52.083400', '1', '系统管理员', 2, '[{\"changed\": {\"fields\": [\"\\u89d2\\u8272\\u540d\\u79f0\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (37, '2021-09-14 15:42:36.899645', '1', '1', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (38, '2021-09-14 15:42:53.703019', '2', '2', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (39, '2021-09-14 15:43:03.186150', '3', '3', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (40, '2021-09-14 15:43:28.111628', '4', '4', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (41, '2021-09-14 15:43:39.834088', '5', '5', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (42, '2021-09-14 15:44:14.677465', '6', '6', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (43, '2021-09-14 15:44:28.409743', '7', '7', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (44, '2021-09-14 15:44:41.278589', '8', '8', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (45, '2021-09-14 15:44:51.778709', '9', '9', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (46, '2021-09-14 15:45:01.010391', '10', '10', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (47, '2021-09-14 15:45:16.833558', '11', '11', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (48, '2021-09-14 15:45:27.810123', '12', '12', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (49, '2021-09-14 15:45:39.926210', '13', '13', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (50, '2021-09-14 15:45:49.787524', '14', '14', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (51, '2021-09-14 15:46:01.192996', '15', '15', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (52, '2021-09-14 15:46:13.642387', '16', '16', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (53, '2021-09-14 15:46:24.717662', '17', '17', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (54, '2021-09-14 15:46:38.362985', '18', '18', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (55, '2021-09-14 15:46:48.509531', '19', '19', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (56, '2021-09-14 16:00:37.131725', '3', 'OGP-4886-152B-11EC-90DF-94C691099607', 2, '更新成功', 11, 1);
INSERT INTO `django_admin_log` VALUES (57, '2021-09-14 16:16:25.648099', '29', '公司信息管理', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (58, '2021-09-14 16:16:41.604598', '30', '查看', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (59, '2021-09-14 16:16:56.381641', '31', '新增', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (60, '2021-09-14 16:17:09.484839', '32', '修改', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (61, '2021-09-14 16:20:14.281258', '20', '20', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (62, '2021-09-14 16:20:24.047729', '21', '21', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (63, '2021-09-14 16:20:34.189122', '22', '22', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (64, '2021-09-27 16:43:26.997521', '33', '删除', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (65, '2021-09-27 16:43:36.995330', '34', '删除', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (66, '2021-09-27 16:43:48.569650', '35', '删除', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (67, '2021-09-27 16:44:29.742418', '36', '删除', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (68, '2021-09-27 16:45:03.031663', '37', '删除', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (69, '2021-09-29 10:05:41.584656', '38', '删除', 1, '新增成功', 12, 1);
INSERT INTO `django_admin_log` VALUES (70, '2021-09-29 10:06:09.717820', '57', '57', 1, '更新成功', 14, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (7, 'authtoken', 'token');
INSERT INTO `django_content_type` VALUES (8, 'authtoken', 'tokenproxy');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (9, 'fy_rabc_sys', 'companymodel');
INSERT INTO `django_content_type` VALUES (10, 'fy_rabc_sys', 'configmodel');
INSERT INTO `django_content_type` VALUES (11, 'fy_rabc_sys', 'orgmodel');
INSERT INTO `django_content_type` VALUES (12, 'fy_rabc_sys', 'resourcemodel');
INSERT INTO `django_content_type` VALUES (13, 'fy_rabc_sys', 'rolemodel');
INSERT INTO `django_content_type` VALUES (14, 'fy_rabc_sys', 'roleresmodel');
INSERT INTO `django_content_type` VALUES (15, 'fy_rabc_sys', 'usermodel');
INSERT INTO `django_content_type` VALUES (16, 'fy_rabc_sys', 'userrolemodel');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2021-09-14 14:35:48.671164');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2021-09-14 14:35:53.508698');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2021-09-14 14:35:54.544319');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2021-09-14 14:35:54.582500');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2021-09-14 14:35:54.607486');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2021-09-14 14:35:55.248902');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2021-09-14 14:35:55.723211');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2021-09-14 14:35:56.175426');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2021-09-14 14:35:56.199674');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2021-09-14 14:35:56.552690');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2021-09-14 14:35:56.581732');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2021-09-14 14:35:56.631350');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2021-09-14 14:35:57.056871');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2021-09-14 14:35:57.508738');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2021-09-14 14:35:57.940060');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2021-09-14 14:35:57.971365');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2021-09-14 14:35:58.441910');
INSERT INTO `django_migrations` VALUES (18, 'authtoken', '0001_initial', '2021-09-14 14:35:59.234689');
INSERT INTO `django_migrations` VALUES (19, 'authtoken', '0002_auto_20160226_1747', '2021-09-14 14:35:59.289228');
INSERT INTO `django_migrations` VALUES (20, 'authtoken', '0003_tokenproxy', '2021-09-14 14:35:59.312493');
INSERT INTO `django_migrations` VALUES (21, 'fy_rabc_sys', '0001_initial', '2021-09-14 14:35:59.346504');
INSERT INTO `django_migrations` VALUES (22, 'sessions', '0001_initial', '2021-09-14 14:35:59.705955');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('8ul49vwsyh0w65om7x79ifq68jur1vo1', '.eJy1mNlv4jgcx_-VUZ5p6_voW05ppR1pNXs9DBXKRcssR5XASFXF_75OYopDICZl8mJh5-CT32l_353XvFgtynKxWZez5aLcOo_f351F5jzCifMaF_l6O6tm691yOXGKvJylmyx3Hp1v4Z93AAD_DlIk7iAM_TuPh-GdJD6TEEjJAHeaJ7Zvr9UTX_V0Ha-q6XTH03mixjybqzGJoRoJYPqun_Fylzf_u580RKhFBDs4AXJDA0cGkTcEh_J5rBAEAdOdSJJc_Z6z_DIObuGgDo6AvmkdlxB_kHXylNQjn-4YT1g1CnLZUs5D-VY-bIpn5wBILIAsQKRlL9_9rPtERhQayyWwAaqFD0BqAUS-FAagQJwMARQyQ2pEXI1knisoBlhPrDkPcbZarB_mb7MiTtJZjbtZ5itFtPyAZhbogOC2VRkYZFX1pAJFmF8LXWHuyuIDkFsAMY9MQA-D4LNWNWEvpYx2--ZoQWEBdFUkmonDIvhZQDMuLYDoaEFpASQhYKaLPY9_NnEoThUmo7w3cbpxmW7W88VzOzKRjRshDyjuKj7rfKKuGFQgIUsr4rn4fD6lm9VrvH5rg0PQAsfdiAiFWxlcaoOTqK_RuKfgjOdUAXKQnAB-cz1_9s9v4b9HlHbbI2eKps9MFCSjsVDa_Y522y-iwkBxAzyaVdq9jnVrShSYDvJQb6-7CaXd1XgHRWIamigY4rFQ2v1LdGOFh6aDBAhHs0q7K8luV6JNVzqgRKKvld6Ewi3JHIXQjBXh8mFhSxNVK6mQp2W8RnGD4EgiLLlMJENmLrPe_cUtJNKSylhvXQ824eGwqnI1CQKWTI4Y9U2bBO6wmL2eBNoSmXh1nLiHbhX2baQ6JKpD5RUPludI_v4jcP8KjzDIksrQF8KEQVSOB4MtGcRls4PTMFLQvh3cjTDEkkQBbkL3ABOFbDwYaskjQkLTTZKLEWGYJZXU_ipsBbDo227dCMMtDQBgZsJ4EIyYTcICU3dCw03EHRTA1xcZ3C53qIsCg0AYe2IpRmuMGNpYBJS-yeK6g3w0wCzIhiIFRAaKx9GghjQoXLCt3klKVKREVQDXiYS9vgNhB4YipOwiGSPnYILw99CEsdU7n-IaJjoc_tQeYjQYW71DVYE7wrgM0PFgbHvMUFBkwHiq4I0Hw20RHGIJDBoRsUGt4Dqap4kzi3fbl9muzIuaxIFOay2J0__ydXUh-xGvnzf36uS-LRbJfXXLvb5a3n-tDsSevrf1gpe4fFFPJ2kGCAYig7GcA5mkIkYQ0iQTGLAccshFTlLMEvVtBGJJcU45TGJ1Pc04rErCbJWvd6V61_f3qVN96NR5_DJ1plqR0JKEPs83B_qpM1F3LBSzvree16f3slrpvKkWUbWKqiWXRnMZ_KZa_9QCqFZAtQR6BeGuWDbTgyjaLMfpdvEzb_5veizRzcVDlTRmTaEyFhq_T52naiVfZNWbVCfF-8mXfpvWQpRWogbzFxXymPzkDH8to2kdTes9WvAZxN8jqY77TfScTyq9UguWN3yTVlxv4z_BZVYXtOGtqXUSQpurzX0BkFsB2zE-FBBdbc8LgMKahLXYqtXWG4PY0F-HYl-IiwthLM98VS3EaiX2l6amqc6Omp0Q7OuFpMjjLC12q-RCE7i-MZ2z0_XNaH9idnS6APdPzv5_FXV38g:1mUmWQ:ee2N7IUd2DoXeuIcFhXCaOej86T8I3zAmK4C-z4qzMc', '2021-10-11 17:02:02.962388');
INSERT INTO `django_session` VALUES ('h1hnw8cdu7a4g54drdkebbk6ztq1rhea', '.eJy1mFlv6jgUx7_KVZ6h9RYvfcuGNA9XGt3ZHi4VymJaZliqhFypqvju4ySmOARiAuXFwo4Tfv77HB-f8-G8yXy1KIrFZl3Mloti6zz9_HAWmfMER85bnMv1dlb11uVyOXJyWczSTSadJ-dH9McYABCMoYv4GMIoGPssisaCBFRAIAQFzGne2L6_VW981911vKq605Kl80S1MpurNomhagmgetaveFnK5n93o4YItYhgBydEXmTgiHDiD8Fx2TxWCJyAacmTRKrfcyrP4-AWDurgcBiY6niEBIPUkSmpWzYtKUto1XJyXinnsXgvHjf5i7MHJBZAGiLS0ivwrt0-nhGFRqUANkA18AnoWgBRILgByBEjQwC5yJBqEVMtmUsFRQHtsTXnMc5Wi_Xj_H2Wx0k6q3E3S7lSRMtPaGqBDgluq0rBIFXVmwoUYXYpdIVZFvknILMAYjYxAX0MwmtVNWHPuYze9s1BQW4B9JQlmo5DJ_BaQNMuLYDooKCwAJIIUHOLfZ9d6zguThUmdVmv43TtMt2s54uXtmUiGzdCPlDclX3W_uR6fNABCWlaEc_59f6UblZv8fq9DQ5BCxx3LSLiXiW40IKTSV-g8Y7BKZOuAmQgOQL84fnB7O_fon8OKO2wR04cmgE1UZCY3AulHe_cbvhFLjdQvBDfTZV2rKPdM2USmhvko95YdxNKO6qxDorAbmSiYIjvhdKOX7xrKywyN4iD6G6qtKOS6EYlt4lKe5QJ7wulN6EwizNPImjaCvfYMLN1E3VWulwcH-M1iheGBxJu8WUiKDJ9mfbeL24hERZXxvrquteERcNOlYtJELB48oS6galJ6A2z2ctJoM2RiV_bibePVlHfRapDoiKUrHiwOEXy1--h92d0gEEWV4YB5yYMcsX9YLDFg5hobnAaRnC37wZ3IwyxOFGIG9Pdw0wiej8Y1-JHhETmNgnG7whDLa6k7ldRy4B533XrRhhmCQAAUxPGh-CO3sQtMHUkNLaJeIMM-PJDBrePO9RFgWHIjTux4HcLjBjaWDgUgcnieYP2aIAsyIYiOEQGis_QoIB0mbk8j5xZXG5fZ2Uh85rEgU5rLInT_-S6epD9G69fNg8q79nmi-ShmvKgnxYP36t0wtdzWx94jYtX9XaSZoBgwDMYizkQScpjBKGbZBwDKiGDjEuSYpqotRGIhYuly2ASq-dpxmAl6Gwl12WhvvXzY-pUC506T9-mzlTnczqh09lQkw5NnZGasVDMem7dr3OfohrpfKkuQekalE5Ym4x18Jfq6pEuH-n6kS4gXUBY5sumuy8pNcNxul38ks3_TQ8G3jzc25jRa7Z56jxXI3KRVS-qYwfvRt_6Jayzdp22D8bNK8IvxCUncOsSg64x6FxYJ8ODcHvKTV-6BPeU4lXpRtdubliCLj59KS61Kt6Gt_rJkYFsLlb3DCCzArYteCgguljPM4Dc6mJ13UkXnm60WaMUNRS7bRdHixAnFlGXoHQN6ksdz6xLfaUxQ7CrB5Jcxlmal6vkzHl9eQw5JcvlcWN3pDI6HoC7Z2f3P_2Fm60:1mQ3jb:Au1Lt6A8ta_ZHxGLZJRu3PkbXxF1G4upkcy-oIWyxaY', '2021-09-28 16:24:07.147022');
INSERT INTO `django_session` VALUES ('jb33zs18slm6zgghu8ozwapa65jsi58e', '.eJy1mNlu4zYUhl9loGs74b7kTitQoAMU03Z6MQ4MbU7cegkke4Ag8LuXsuiYsh3RjEc3hEUt_nTOfw7F_817KavlvK7n61U9Xczrjffw482bF94DHHkvaVWuNtPmaLVdLEZeVdbTfF2U3oP3Lf5zDAAIx5AiMYYwDscBj-OxJCGTEEjJAPfaOzavL80dX_XhKl02h5Mtz2eZGstipsYshWokgOmrfqaLbdn-727UEqEOETzDiZAfGzgySgIXHMpnqUIQBEy2IstK9XvGyo9xcAcHneEgFACFg0mLI6gvnHAgy9WIZ2KyJbNSRYcB1hMp7z4tlvPV_ex1WqVZPq1f6_t8vXxJV69LBbXwDtzEwi1gaGbVJyR0ymqZk_3IFTHPWDMK0sfdkK6rp3dAagFkESKdPIf-Z2UnCqLQWCmBDVBNvAMyW-ZDKQxAgThxARSyQGpEHH0-89V6UXbTzi3QEcHdqDLgFFV1pwJFmF8L3WBu6-odUFgAMU9MwACD6LNRNWE_KnWd9vUxgtIC6CslmoXDEvhZQFOXFkB0jCAEFkISA2bmOAj4ZyuH4lxxMsp7K-dSS1rN5k9daeIuNz7jhlEkjFYqhegrKP-Um_GSKj4OshO-b34QTr__Fv9zRIEWFAFlaKL4fl-ZnKPQTAWMCnmazD2KH0VHEmQhkQIigyTgKHEhUUVaNjxYXiL5-4_I_ys-wnALTIylWuwSluiWlzDmAkMRUmGRjJFLMFH8e2zAwG6OyHkhxsJvZC51jkjS911yi1ygsKAkMTRRhM_dUK6WCyIWEi7b9ukfaoj2tc8b5YItMJISv5FLrMOCg75WeaNcuoVEL3xPhMyUC5JOheQiF2lBIZIhE4X1fjncIhdqIYlw-zF9kEsSOxW0m1yIBSak2De6iwxUlAaTS1e77HzXg6gwcuRHeKjugoAFBesdz6G78NhNudfLhVlICImFKRcuBpQLtcCg5t-PcvEZoMPJpatdfp6jJDJXgAD1bqdukgu0oCSMhmZ3iXw3lOvlwi0kajNsdhdBRd_e-Ea5CFuGwjgeIxAewkLjvv3kjXLpalecr4yYmiUdYIiHkguyoZDA7yQpdvrUdUoS7DYYeb5I89jsugLEg5URtqDAUJi9TiAqh4tLt5KaHd7pQk3bffshMMlgeyMkbCwAM7OsAwiGUwySNpq9Row1ifhOX7wOWzVmQ4kFRcaKFKiG9-tbzOPIm6bbzfN0W5fVnsSDXmcuS_P_ylVzovg3XT2t79RufFPNs7vmkjt9tr772uzOA31t5wHPaf2s7s7yAhAMRAFTOQMyy0WKIKRZITBgJeSQi5LkmGXq3QjEkuKScpil6nxecNgEdLosV9taPevH28RrXnTiPXyZeBPtMmibQXsLrbkw8Ubqirli1tfuj_dWQt3MnD1p7-hqS1f7KK2R4v6kxozVbqz2t7TBdQXhtlq0hxaHtr06zTfzn2WLMTlWYXvyID3jqC0LY6KVw8R7bGbKedE8SRUi3o2-nIW68Wq1WavdWm3XOr2WNnCH5SeX-DtS2Ztm2jVz5q8a5CH56QX-veWnPb9fKqt3-3fYd2KXctJ4q9pcveGdtDs8LD-35qT7NtYWcqKp9dXxPxCfAAorYFf0roDo6gB_ACitVbk3irVTfHOzfPeOXbE_EMplXUCw209kVZkWebVdZpdXBYeV6kKYHFan3UnU0ekE3D16u_8BonGj5A:1mVOzH:p5i64gjJskCRSyVVGMFfQK6n2ZYsqcH858ciHHxo0p0', '2021-10-13 10:06:23.224320');

-- ----------------------------
-- Table structure for t_sys_company
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_company`;
CREATE TABLE `t_sys_company`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `company_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '公司代码',
  `short_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '公司简称',
  `full_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '公司全称',
  `address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '公司地址',
  `tel` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '公司电话',
  `logo_url` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'logo地址',
  `core_value` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '核心价值观',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '公司信息表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_company
-- ----------------------------
INSERT INTO `t_sys_company` VALUES (1, 'CP-546E4-152E-11EC-B7DD-94C691099607', '谷歌中国', '谷歌信息技术（中国）有限公司', NULL, NULL, NULL, NULL, 1, 'admin', '2021-09-14 15:37:22', NULL, '2021-09-14 15:37:22', NULL);

-- ----------------------------
-- Table structure for t_sys_config
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_config`;
CREATE TABLE `t_sys_config`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `main_type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '参数主类型',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '名称',
  `value_type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'str' COMMENT '值类型（‘str’,\'dic\',\'arr\'）',
  `value` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '值',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '参数配置表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_config
-- ----------------------------
INSERT INTO `t_sys_config` VALUES (1, '性别', '男', 'str', '1', 1, 'admin', '2021-10-26 15:31:57', NULL, '2021-10-26 15:31:57', NULL);
INSERT INTO `t_sys_config` VALUES (2, '性别', '女', 'str', '0', 1, 'admin', '2021-10-26 15:32:11', NULL, '2021-10-26 15:32:11', NULL);

-- ----------------------------
-- Table structure for t_sys_org
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_org`;
CREATE TABLE `t_sys_org`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `parent_id` int(11) NULL DEFAULT NULL COMMENT '父节点ID',
  `org_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '组织架构代码',
  `org_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '组织架构名称',
  `org_type` varchar(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '组织架构类型（‘C’：公司；‘D’：部门；‘P’：岗位；）',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_sys_org_code`(`org_code`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '组织架构表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_org
-- ----------------------------
INSERT INTO `t_sys_org` VALUES (1, NULL, 'OGD-6FF6-152B-11EC-AE7A-94C691099607', 'IT部', 'D', 1, 'admin', '2021-09-14 15:14:30', NULL, '2021-09-14 15:14:30', NULL);
INSERT INTO `t_sys_org` VALUES (2, 1, 'OGG-98FE-152B-11EC-8FE2-94C691099607', '运维组', 'G', 1, 'admin', '2021-09-14 15:15:24', NULL, '2021-09-14 15:15:24', NULL);
INSERT INTO `t_sys_org` VALUES (3, 2, 'OGP-4886-152B-11EC-90DF-94C691099607', '系统管理员', 'P', 1, 'admin', '2021-09-14 15:16:34', 'admin', '2021-09-14 16:00:37', '');

-- ----------------------------
-- Table structure for t_sys_resource
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_resource`;
CREATE TABLE `t_sys_resource`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `parent_id` int(11) NULL DEFAULT NULL COMMENT '父ID',
  `res_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '资源代码',
  `res_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '资源类型（‘M’：菜单；‘A’：操作）',
  `res_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '资源名称',
  `res_value` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '资源值（如果是菜单，则为菜单路径，中间菜单可以是空；如果是操作，则为操作代码）',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_sys_resource_code`(`res_code`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 39 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '资源信息表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_resource
-- ----------------------------
INSERT INTO `t_sys_resource` VALUES (1, NULL, 'RES-000C-1528-11EC-B7EE-94C691099607', 'M', '系统管理', NULL, 1, 'admin', '2021-09-14 14:50:56', NULL, '2021-09-14 14:50:56', NULL);
INSERT INTO `t_sys_resource` VALUES (2, 1, 'RES-D2AE-1528-11EC-9DFB-94C691099607', 'M', '基础设置', NULL, 1, 'admin', '2021-09-14 14:51:32', NULL, '2021-09-14 14:51:32', NULL);
INSERT INTO `t_sys_resource` VALUES (3, 2, 'RES-22B0-1534-11EC-85A8-94C691099607', 'M', '公司信息管理', '/admin/fy_rabc_sys/companymodel', 1, 'admin', '2021-09-14 14:51:59', NULL, '2021-09-14 14:51:59', '');
INSERT INTO `t_sys_resource` VALUES (4, 2, 'RES-81CC-1528-11EC-A44C-94C691099607', 'M', '组织架构管理', '/sys/org', 1, 'admin', '2021-09-14 14:52:23', NULL, '2021-09-29 09:50:57', NULL);
INSERT INTO `t_sys_resource` VALUES (5, 2, 'RES-6D24-1528-11EC-9DCA-94C691099607', 'M', '系统资源管理', '/sys/res', 1, 'admin', '2021-09-14 14:52:53', NULL, '2021-09-29 09:50:53', NULL);
INSERT INTO `t_sys_resource` VALUES (6, 2, 'RES-2C98-1528-11EC-8274-94C691099607', 'M', '角色信息管理', '/admin/fy_rabc_sys/rolemodel', 1, 'admin', '2021-09-14 14:53:57', NULL, '2021-09-29 09:50:49', NULL);
INSERT INTO `t_sys_resource` VALUES (7, 2, 'RES-D434-1528-11EC-9D60-94C691099607', 'M', '用户信息管理', '/sys/usr', 1, 'admin', '2021-09-14 14:54:20', NULL, '2021-09-29 09:50:44', NULL);
INSERT INTO `t_sys_resource` VALUES (8, 2, 'RES-37F4-1528-11EC-B30D-94C691099607', 'M', '角色用户设置', '/sys/rol', 1, 'admin', '2021-09-14 14:55:04', NULL, '2021-09-29 09:50:40', NULL);
INSERT INTO `t_sys_resource` VALUES (9, 2, 'RES-A9DC-1528-11EC-A6F1-94C691099607', 'M', '角色资源设置', '/sys/r2r', 1, 'admin', '2021-09-14 14:55:28', NULL, '2021-09-29 09:50:38', NULL);
INSERT INTO `t_sys_resource` VALUES (10, 2, 'RES-4E06-1528-11EC-9BB7-94C691099607', 'M', '系统参数管理', '/admin/fy_rabc_sys/configmodel', 1, 'admin', '2021-09-14 14:55:51', NULL, '2021-09-29 09:50:35', NULL);
INSERT INTO `t_sys_resource` VALUES (11, 4, 'RES-AE8A-1529-11EC-94FE-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 14:57:49', 'admin', '2021-09-29 09:51:33', NULL);
INSERT INTO `t_sys_resource` VALUES (12, 5, 'RES-6DC6-1529-11EC-929F-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 14:58:14', NULL, '2021-09-29 09:51:37', NULL);
INSERT INTO `t_sys_resource` VALUES (13, 6, 'RES-0258-1529-11EC-AD3E-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 14:58:45', NULL, '2021-09-29 09:51:43', NULL);
INSERT INTO `t_sys_resource` VALUES (14, 7, 'RES-3FDA-1529-11EC-B24C-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 14:59:04', NULL, '2021-09-29 09:51:48', NULL);
INSERT INTO `t_sys_resource` VALUES (15, 8, 'RES-935E-1529-11EC-B313-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 14:59:26', NULL, '2021-09-29 09:51:51', NULL);
INSERT INTO `t_sys_resource` VALUES (16, 9, 'RES-67E8-1529-11EC-80EC-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 14:59:55', NULL, '2021-09-29 09:51:55', NULL);
INSERT INTO `t_sys_resource` VALUES (17, 10, 'RES-D534-1529-11EC-8F84-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 15:00:10', NULL, '2021-09-29 09:52:00', NULL);
INSERT INTO `t_sys_resource` VALUES (18, 4, 'RES-FE1A-1529-11EC-8A7E-94C691099607', 'A', '新增', 'RABC_ADD', 1, 'admin', '2021-09-14 15:02:38', NULL, '2021-09-29 09:52:03', NULL);
INSERT INTO `t_sys_resource` VALUES (19, 5, 'RES-4962-1529-11EC-9674-94C691099607', 'A', '新增', 'RABC_ADD', 1, 'admin', '2021-09-14 15:03:12', NULL, '2021-09-29 09:52:06', NULL);
INSERT INTO `t_sys_resource` VALUES (20, 6, 'RES-32AE-1529-11EC-87EF-94C691099607', 'A', '新增', 'RABC_ADD', 1, 'admin', '2021-09-14 15:03:47', NULL, '2021-09-29 09:52:10', NULL);
INSERT INTO `t_sys_resource` VALUES (21, 7, 'RES-F65C-1529-11EC-9DAC-94C691099607', 'A', '新增', 'RABC_ADD', 1, 'admin', '2021-09-14 15:04:06', NULL, '2021-09-29 09:52:13', NULL);
INSERT INTO `t_sys_resource` VALUES (22, 8, 'RES-94BA-152A-11EC-85E0-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 15:05:52', NULL, '2021-09-29 09:52:16', NULL);
INSERT INTO `t_sys_resource` VALUES (23, 9, 'RES-1C88-152A-11EC-8259-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 15:06:16', NULL, '2021-09-29 09:52:19', NULL);
INSERT INTO `t_sys_resource` VALUES (24, 4, 'RES-79F4-152A-11EC-985D-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 15:06:51', NULL, '2021-09-29 09:52:23', NULL);
INSERT INTO `t_sys_resource` VALUES (25, 5, 'RES-D3AE-152A-11EC-9FE6-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 15:07:09', NULL, '2021-09-29 09:52:26', NULL);
INSERT INTO `t_sys_resource` VALUES (26, 6, 'RES-44E8-152A-11EC-9786-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 15:07:23', NULL, '2021-09-29 09:52:29', NULL);
INSERT INTO `t_sys_resource` VALUES (27, 7, 'RES-85AE-152A-11EC-8588-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 15:07:39', NULL, '2021-09-29 09:52:31', NULL);
INSERT INTO `t_sys_resource` VALUES (28, 10, 'RES-036E-152A-11EC-B100-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 15:09:29', NULL, '2021-09-29 09:52:44', NULL);
INSERT INTO `t_sys_resource` VALUES (29, 10, 'RES-80EC-152A-11EC-94AD-94C691099607', 'A', '新增', 'RABC_ADD', 1, 'admin', '2021-09-14 15:09:54', NULL, '2021-09-29 09:52:50', NULL);
INSERT INTO `t_sys_resource` VALUES (30, 3, 'RES-1DD8-1534-11EC-9884-94C691099607', 'A', '查看', 'RABC_VIEW', 1, 'admin', '2021-09-14 16:16:42', NULL, '2021-09-29 09:52:56', '');
INSERT INTO `t_sys_resource` VALUES (31, 3, 'RES-819C-1534-11EC-9AA0-94C691099607', 'A', '新增', 'RABC_ADD', 1, 'admin', '2021-09-14 16:16:56', NULL, '2021-09-29 09:52:59', '');
INSERT INTO `t_sys_resource` VALUES (32, 3, 'RES-9812-1534-11EC-B72F-94C691099607', 'A', '修改', 'RABC_UPDATE', 1, 'admin', '2021-09-14 16:17:09', NULL, '2021-09-29 09:53:02', '');
INSERT INTO `t_sys_resource` VALUES (33, 4, 'RES-954A-1F6E-11EC-83B1-94C691099607', 'A', '删除', 'RABC_DELETE', 1, 'admin', '2021-09-27 16:43:27', NULL, '2021-09-29 09:53:05', '');
INSERT INTO `t_sys_resource` VALUES (34, 5, 'RES-C53A-1F6F-11EC-9B62-94C691099607', 'A', '删除', 'RABC_DELETE', 1, 'admin', '2021-09-27 16:43:37', NULL, '2021-09-29 09:53:09', '');
INSERT INTO `t_sys_resource` VALUES (35, 6, 'RES-2786-1F6F-11EC-A605-94C691099607', 'A', '删除', 'RABC_DELETE', 1, 'admin', '2021-09-27 16:43:49', NULL, '2021-09-29 09:53:11', '');
INSERT INTO `t_sys_resource` VALUES (36, 10, 'RES-E852-1F6F-11EC-B858-94C691099607', 'A', '删除', 'RABC_DELETE', 1, 'admin', '2021-09-27 16:44:30', NULL, '2021-09-29 09:53:18', '');
INSERT INTO `t_sys_resource` VALUES (37, 3, 'RES-E390-1F6F-11EC-8F66-94C691099607', 'A', '删除', 'RABC_DELETE', 1, 'admin', '2021-09-27 16:45:03', NULL, '2021-09-29 09:57:59', '');
INSERT INTO `t_sys_resource` VALUES (38, 7, 'RES-3CEE-20C9-11EC-95EA-94C691099607', 'A', '删除', 'RABC_DELETE', 1, 'admin', '2021-09-29 10:05:42', NULL, '2021-09-29 10:05:42', '');

-- ----------------------------
-- Table structure for t_sys_role
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_role`;
CREATE TABLE `t_sys_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `role_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色代码',
  `role_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色名称',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_sys_role_code`(`role_code`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '角色表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_role
-- ----------------------------
INSERT INTO `t_sys_role` VALUES (1, 'ROL-138C-152B-11EC-8F18-94C691099607', '系统管理员', 1, 'admin', '2021-09-14 15:11:58', 'admin', '2021-09-14 15:11:58', NULL);

-- ----------------------------
-- Table structure for t_sys_role_res
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_role_res`;
CREATE TABLE `t_sys_role_res`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `role_res_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色资源代码',
  `role_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色代码',
  `res_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '资源代码',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_rol_res_code`(`role_res_code`) USING BTREE,
  INDEX `FK_re_roleres_res`(`res_code`) USING BTREE,
  INDEX `FK_re_roleres_role`(`role_code`) USING BTREE,
  CONSTRAINT `FK_re_roleres_res` FOREIGN KEY (`res_code`) REFERENCES `t_sys_resource` (`res_code`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_re_roleres_role` FOREIGN KEY (`role_code`) REFERENCES `t_sys_role` (`role_code`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 58 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '角色资源表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_role_res
-- ----------------------------
INSERT INTO `t_sys_role_res` VALUES (30, 'RO-RE-F0-20C9-11EC-8160-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-1DD8-1534-11EC-9884-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (31, 'RO-RE-CC-20C9-11EC-A01B-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-819C-1534-11EC-9AA0-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (32, 'RO-RE-A8-20C9-11EC-97EB-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-9812-1534-11EC-B72F-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (33, 'RO-RE-E6-20C9-11EC-97B1-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-E390-1F6F-11EC-8F66-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (34, 'RO-RE-A2-20C9-11EC-A2E5-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-AE8A-1529-11EC-94FE-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (35, 'RO-RE-68-20C9-11EC-943D-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-FE1A-1529-11EC-8A7E-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (36, 'RO-RE-8C-20C9-11EC-B850-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-79F4-152A-11EC-985D-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (37, 'RO-RE-54-20C9-11EC-A55D-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-954A-1F6E-11EC-83B1-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (38, 'RO-RE-02-20C9-11EC-A979-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-6DC6-1529-11EC-929F-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (39, 'RO-RE-A8-20C9-11EC-A175-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-4962-1529-11EC-9674-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (40, 'RO-RE-F6-20C9-11EC-BA43-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-D3AE-152A-11EC-9FE6-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (41, 'RO-RE-E8-20C9-11EC-9177-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-C53A-1F6F-11EC-9B62-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (42, 'RO-RE-E2-20C9-11EC-AD8B-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-0258-1529-11EC-AD3E-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (43, 'RO-RE-D4-20C9-11EC-B7EB-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-32AE-1529-11EC-87EF-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (44, 'RO-RE-DA-20C9-11EC-BFB9-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-44E8-152A-11EC-9786-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (45, 'RO-RE-9C-20C9-11EC-B2F3-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-2786-1F6F-11EC-A605-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (46, 'RO-RE-90-20C9-11EC-878E-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-3FDA-1529-11EC-B24C-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (47, 'RO-RE-AC-20C9-11EC-96F9-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-F65C-1529-11EC-9DAC-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (48, 'RO-RE-86-20C9-11EC-A5A1-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-85AE-152A-11EC-8588-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (49, 'RO-RE-9C-20C9-11EC-AE56-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-3CEE-20C9-11EC-95EA-94C691099607', 1, 'admin', '2021-09-29 10:06:09', NULL, '2021-09-29 10:06:09', NULL);
INSERT INTO `t_sys_role_res` VALUES (50, 'RO-RE-7A-20C9-11EC-90EE-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-935E-1529-11EC-B313-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);
INSERT INTO `t_sys_role_res` VALUES (51, 'RO-RE-14-20C9-11EC-966B-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-94BA-152A-11EC-85E0-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);
INSERT INTO `t_sys_role_res` VALUES (52, 'RO-RE-F0-20C9-11EC-8875-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-67E8-1529-11EC-80EC-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);
INSERT INTO `t_sys_role_res` VALUES (53, 'RO-RE-B4-20C9-11EC-AA61-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-1C88-152A-11EC-8259-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);
INSERT INTO `t_sys_role_res` VALUES (54, 'RO-RE-8C-20C9-11EC-8074-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-D534-1529-11EC-8F84-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);
INSERT INTO `t_sys_role_res` VALUES (55, 'RO-RE-18-20C9-11EC-AC05-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-036E-152A-11EC-B100-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);
INSERT INTO `t_sys_role_res` VALUES (56, 'RO-RE-E8-20C9-11EC-AA71-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-80EC-152A-11EC-94AD-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);
INSERT INTO `t_sys_role_res` VALUES (57, 'RO-RE-9A-20C9-11EC-AE69-94C691099607', 'ROL-138C-152B-11EC-8F18-94C691099607', 'RES-E852-1F6F-11EC-B858-94C691099607', 1, 'admin', '2021-09-29 10:06:10', NULL, '2021-09-29 10:06:10', NULL);

-- ----------------------------
-- Table structure for t_sys_user
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_user`;
CREATE TABLE `t_sys_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `org_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '组织架构代码',
  `user_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户代码',
  `user_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户姓名',
  `nick_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户昵称',
  `ico_img` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '头像图片地址',
  `gender` int(11) NULL DEFAULT NULL COMMENT '性别',
  `id_num` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '身份证号码',
  `tel` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '手机号',
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'E-Mail地址',
  `login_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '登录名',
  `pwd` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '登录密码',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_sys_user_code`(`user_code`) USING BTREE,
  UNIQUE INDEX `idx_sys_user_logname`(`login_name`) USING BTREE,
  INDEX `FK_re_orguser_org`(`org_code`) USING BTREE,
  CONSTRAINT `FK_re_orguser_org` FOREIGN KEY (`org_code`) REFERENCES `t_sys_org` (`org_code`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '用户表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_user
-- ----------------------------
INSERT INTO `t_sys_user` VALUES (1, 'OGP-4886-152B-11EC-90DF-94C691099607', '100001', '管理员', '管理员', NULL, 1, NULL, NULL, NULL, 'admin', 'admin', 1, 'admin', '2021-09-14 15:39:25', NULL, '2021-09-14 15:48:22', NULL);

-- ----------------------------
-- Table structure for t_sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `t_sys_user_role`;
CREATE TABLE `t_sys_user_role`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `user_role_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户角色代码',
  `user_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '用户代码',
  `role_code` varchar(36) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '角色代码',
  `status` int(11) NOT NULL DEFAULT 1 COMMENT '记录状态（1有效；0无效）',
  `creator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `createdate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建日期',
  `updator` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `updatedate` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新日期',
  `remark` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `idx_sys_user_role_code`(`user_role_code`) USING BTREE,
  INDEX `FK_rf_roleuser_role`(`role_code`) USING BTREE,
  INDEX `FK_rf_roleuser_user`(`user_code`) USING BTREE,
  CONSTRAINT `FK_rf_roleuser_role` FOREIGN KEY (`role_code`) REFERENCES `t_sys_role` (`role_code`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_rf_roleuser_user` FOREIGN KEY (`user_code`) REFERENCES `t_sys_user` (`user_code`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '用户角色表' ROW_FORMAT = COMPACT;

-- ----------------------------
-- Records of t_sys_user_role
-- ----------------------------
INSERT INTO `t_sys_user_role` VALUES (1, 'U-R-AF4C-152E-11EC-92BD-94C691099607', '100001', 'ROL-138C-152B-11EC-8F18-94C691099607', 1, 'admin', '2021-09-14 15:40:11', NULL, '2021-09-14 15:40:11', NULL);

SET FOREIGN_KEY_CHECKS = 1;