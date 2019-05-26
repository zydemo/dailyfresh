/*
Navicat MySQL Data Transfer

Source Server         : first
Source Server Version : 50722
Source Host           : localhost:3306
Source Database       : dailyfresh

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-05-26 18:07:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add user info', '7', 'add_userinfo');
INSERT INTO `auth_permission` VALUES ('26', 'Can change user info', '7', 'change_userinfo');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete user info', '7', 'delete_userinfo');
INSERT INTO `auth_permission` VALUES ('28', 'Can view user info', '7', 'view_userinfo');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 商品信息', '8', 'add_goodsinfo');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 商品信息', '8', 'change_goodsinfo');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 商品信息', '8', 'delete_goodsinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 商品信息', '8', 'view_goodsinfo');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 分类信息', '9', 'add_typeinfo');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 分类信息', '9', 'change_typeinfo');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 分类信息', '9', 'delete_typeinfo');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 分类信息', '9', 'view_typeinfo');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$120000$QU55PtHNepan$RbaijUnGoYc4uMyj9Sd9Oc578VWRNtZRHRvh+L21/nE=', '2019-05-26 04:06:06.378675', '1', 'admin', '', '', '123@163.com', '1', '1', '2019-05-26 03:17:35.888724');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `df_goods_goodsinfo`
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_goodsinfo`;
CREATE TABLE `df_goods_goodsinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gtitle` varchar(35) NOT NULL,
  `gprice` decimal(7,2) NOT NULL,
  `gunit` varchar(20) NOT NULL,
  `gclick` int(11) NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  `gjianjie` varchar(200) NOT NULL,
  `gkucun` int(11) NOT NULL,
  `gpic` varchar(100) DEFAULT NULL,
  `gcontent` longtext NOT NULL,
  `gtype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `df_goods_goodsinfo_gtype_id_63a02cef_fk_df_goods_typeinfo_id` (`gtype_id`),
  CONSTRAINT `df_goods_goodsinfo_gtype_id_63a02cef_fk_df_goods_typeinfo_id` FOREIGN KEY (`gtype_id`) REFERENCES `df_goods_typeinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_goodsinfo
-- ----------------------------
INSERT INTO `df_goods_goodsinfo` VALUES ('1', '展卉 海南千禧圣女果', '21.80', '500g', '1', '0', '圣女果，北方常被称为小西红柿，正式名称为小番茄果，是一年生草本植物，属茄科番茄属。植株最高时能长到2米。具有生津止渴、健胃消食、清热解毒、凉血平肝，补血养血和增进食欲的功效。', '100', 'article_img/201905/20190526174010_31.jpg', '<p>&nbsp;&nbsp;&nbsp;&nbsp;它根系发达，再生能力强，侧根发生多，大部份分布于土表30厘米的土层内。植株生长强健，有茎蔓自封顶的，品种较少；有无限生长的，株高2米以上。叶为奇数羽状复叶，小叶多而细。</p><p style=\"text-align: center;\"><img src=\"/static/media/upimg/圣女果_20190526155214_711.jpg\" title=\"\" alt=\"圣女果.jpg\"/></p><p>&nbsp;&nbsp;&nbsp;&nbsp;果实鲜艳，有红、黄、绿等果色，单果重一般为10～30克，果实以圆球型为主；种子比普通番茄小，心形。密被茸毛，百粒重1.2～1.5克。果实直径约1～3厘米，鲜红色。</p>', '1');
INSERT INTO `df_goods_goodsinfo` VALUES ('2', '渔鼎鲜 挪威冰鲜三文鱼（大西洋鲑）去皮纯肉400g 日料刺身', '89.50', '400g', '2', '0', '渔鼎鲜 挪威冰鲜三文鱼（大西洋鲑）去皮纯肉 日料刺身', '200', 'article_img/201905/20190526173903_19.jpg', '<p><img src=\"/static/media/upimg/58fd7e13N26b6af41_20190526173813_788.jpg\" title=\"\" alt=\"58fd7e13N26b6af41.jpg\"/></p>', '2');
INSERT INTO `df_goods_goodsinfo` VALUES ('3', '东来顺羔羊后腿切片400g 内蒙新鲜羔羊后腿肉片清真羊肉卷 涮火锅食材', '62.80', '400g', '3', '0', '东来顺羔羊后腿切片，内蒙新鲜羔羊后腿肉片清真羊肉卷 涮火锅食材', '300', 'article_img/201905/20190526175110_45.jpg', '<p><img src=\"/static/media/upimg/1c629c5a8b5776c4_20190526175048_241.jpg\" style=\"\"/></p><p><img src=\"/static/media/upimg/3b0d93fe198d4260_20190526175048_483.jpg\" style=\"\"/></p><p><br/></p>', '3');
INSERT INTO `df_goods_goodsinfo` VALUES ('4', '麻酱鸡蛋农家秘制红泥腌制五香流油咸鸡蛋20枚', '38.00', '20枚', '5', '0', '麻酱鸡蛋农家秘制红泥腌制五香流油咸鸡蛋20枚', '200', 'article_img/201905/20190526175452_1.jpg', '<p><img src=\"/static/media/upimg/5ce21e6cN88e0b37c_20190526175438_777.jpg\" style=\"\"/></p><p><img src=\"/static/media/upimg/5ce21e6dNdbf3ff7c_20190526175438_929.jpg\" style=\"\"/></p><p><br/></p>', '4');
INSERT INTO `df_goods_goodsinfo` VALUES ('5', '西红柿 番茄 粉茄 约1.25kg 新鲜蔬菜', '22.80', '1.25kg', '10', '0', '西红柿 番茄 粉茄 约1.25kg 新鲜蔬菜', '100', 'article_img/201905/20190526175712_10.jpg', '<p><img src=\"/static/media/upimg/05d0d391e61dd0e8_20190526175702_826.jpg\" title=\"\" alt=\"05d0d391e61dd0e8.jpg\"/></p>', '5');
INSERT INTO `df_goods_goodsinfo` VALUES ('6', '五芳斋 儿童面点 老母鸡汤小馄饨 1.85kg 5袋装 速冻食品小云吞', '89.90', '1.85kg*5袋', '15', '0', '五芳斋 儿童面点 老母鸡汤小馄饨 1.85kg 5袋装 速冻食品小云吞', '100', 'article_img/201905/20190526175906_31.jpg', '<p><img src=\"/static/media/upimg/5aa73055N0a1a922c_20190526175900_611.jpg\" title=\"\" alt=\"5aa73055N0a1a922c.jpg\"/></p>', '6');

-- ----------------------------
-- Table structure for `df_goods_typeinfo`
-- ----------------------------
DROP TABLE IF EXISTS `df_goods_typeinfo`;
CREATE TABLE `df_goods_typeinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ttitle` varchar(20) NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_goods_typeinfo
-- ----------------------------
INSERT INTO `df_goods_typeinfo` VALUES ('1', '新鲜水果', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('2', '海鲜水产', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('3', '猪牛羊肉', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('4', '禽类蛋品', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('5', '新鲜蔬菜', '0');
INSERT INTO `df_goods_typeinfo` VALUES ('6', '速冻食品', '0');

-- ----------------------------
-- Table structure for `df_user_userinfo`
-- ----------------------------
DROP TABLE IF EXISTS `df_user_userinfo`;
CREATE TABLE `df_user_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) NOT NULL,
  `upwd` varchar(40) NOT NULL,
  `uemail` varchar(30) NOT NULL,
  `ushou` varchar(20) NOT NULL,
  `uaddress` varchar(200) NOT NULL,
  `uyoubian` varchar(6) NOT NULL,
  `uphone` varchar(11) NOT NULL,
  `isDelete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of df_user_userinfo
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-05-26 07:16:23.828715', '1', '新鲜水果', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-05-26 07:16:44.381239', '2', '海鲜水产', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-05-26 07:16:56.651307', '3', '猪牛羊肉', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-05-26 07:42:03.331328', '4', '禽类蛋品', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-05-26 07:42:11.075899', '5', '新鲜蔬菜', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-05-26 07:42:16.701669', '6', '新鲜蔬菜', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-05-26 07:42:46.568023', '6', '速冻食品', '2', '[{\"changed\": {\"fields\": [\"ttitle\"]}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-05-26 07:56:36.745700', '1', 'GoodsInfo object (1)', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2019-05-26 09:39:04.297252', '2', '渔鼎鲜 挪威冰鲜三文鱼（大西洋鲑）去皮纯肉400g 日料刺身', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2019-05-26 09:39:50.213878', '1', '展卉 海南千禧圣女果', '2', '[{\"changed\": {\"fields\": [\"gpic\"]}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2019-05-26 09:40:10.506039', '1', '展卉 海南千禧圣女果', '2', '[{\"changed\": {\"fields\": [\"gpic\"]}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2019-05-26 09:51:10.090114', '3', '东来顺羔羊后腿切片400g 内蒙新鲜羔羊后腿肉片清真羊肉卷 涮火锅食材', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2019-05-26 09:54:52.574757', '4', '麻酱鸡蛋农家秘制红泥腌制五香流油咸鸡蛋20枚', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2019-05-26 09:56:34.809574', '5', '西红柿 番茄 粉茄 约1.25kg 新鲜蔬菜', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2019-05-26 09:57:12.637737', '5', '西红柿 番茄 粉茄 约1.25kg 新鲜蔬菜', '2', '[{\"changed\": {\"fields\": [\"gpic\", \"gcontent\"]}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2019-05-26 09:59:06.118943', '6', '五芳斋 儿童面点 老母鸡汤小馄饨 1.85kg 5袋装 速冻食品小云吞', '1', '[{\"added\": {}}]', '8', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('8', 'df_goods', 'goodsinfo');
INSERT INTO `django_content_type` VALUES ('9', 'df_goods', 'typeinfo');
INSERT INTO `django_content_type` VALUES ('7', 'df_user', 'userinfo');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-05-26 02:40:59.167404');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-05-26 02:41:12.053141');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-05-26 02:41:16.219379');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-05-26 02:41:16.250381');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2019-05-26 02:41:16.282382');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2019-05-26 02:41:17.356444');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2019-05-26 02:41:18.338500');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2019-05-26 02:41:19.359558');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2019-05-26 02:41:19.454564');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2019-05-26 02:41:20.122602');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2019-05-26 02:41:20.159604');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2019-05-26 02:41:20.211607');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2019-05-26 02:41:21.172662');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2019-05-26 02:41:21.834700');
INSERT INTO `django_migrations` VALUES ('15', 'df_goods', '0001_initial', '2019-05-26 02:41:24.485852');
INSERT INTO `django_migrations` VALUES ('16', 'df_user', '0001_initial', '2019-05-26 02:41:24.835872');
INSERT INTO `django_migrations` VALUES ('17', 'df_user', '0002_auto_20190526_1040', '2019-05-26 02:41:24.889875');
INSERT INTO `django_migrations` VALUES ('18', 'sessions', '0001_initial', '2019-05-26 02:41:25.642918');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('rgw9zokzd7lg44y6g3tacj5lpckp1ljv', 'OGNmMzdkNjFjZGFmOTU4OWY1NDA5MjA1N2M3Y2VjM2JjZGQwMjVlZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMzZiZGU3NTJlYTRkNmIwY2FmZWU2YTVmNzA5OWZjN2JhYWQ4YjliIn0=', '2019-06-09 04:06:06.501682');
