/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50067
Source Host           : localhost:3306
Source Database       : pythonjsgl

Target Server Type    : MYSQL
Target Server Version : 50067
File Encoding         : 65001

Date: 2024-03-26 15:35:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for app_gly
-- ----------------------------
DROP TABLE IF EXISTS `app_gly`;
CREATE TABLE `app_gly` (
  `id` int(11) NOT NULL auto_increment,
  `yhm` varchar(40) collate gb2312_bin NOT NULL,
  `mm` varchar(40) collate gb2312_bin NOT NULL,
  `xm` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_gly
-- ----------------------------
INSERT INTO `app_gly` VALUES ('1', 'admin', 'admin', 'admin');

-- ----------------------------
-- Table structure for app_jiaoshi
-- ----------------------------
DROP TABLE IF EXISTS `app_jiaoshi`;
CREATE TABLE `app_jiaoshi` (
  `id` int(11) NOT NULL auto_increment,
  `yhm` varchar(40) collate gb2312_bin NOT NULL,
  `mm` varchar(40) collate gb2312_bin NOT NULL,
  `xm` varchar(40) collate gb2312_bin NOT NULL,
  `lxdh` varchar(40) collate gb2312_bin NOT NULL,
  `zc` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_jiaoshi
-- ----------------------------
INSERT INTO `app_jiaoshi` VALUES ('1', 'js', 'js', 'js', '10230', '教授');
INSERT INTO `app_jiaoshi` VALUES ('2', 'js1', 'js1', 'js1', '2123123', '讲师');
INSERT INTO `app_jiaoshi` VALUES ('3', 'js2', 'js2', 'js2', '120301023', '教授');

-- ----------------------------
-- Table structure for app_jsjy
-- ----------------------------
DROP TABLE IF EXISTS `app_jsjy`;
CREATE TABLE `app_jsjy` (
  `id` int(11) NOT NULL auto_increment,
  `sqh` varchar(40) collate gb2312_bin NOT NULL,
  `bt` varchar(40) collate gb2312_bin NOT NULL,
  `nr` varchar(4000) collate gb2312_bin NOT NULL,
  `js` varchar(40) collate gb2312_bin NOT NULL,
  `sqrq` varchar(40) collate gb2312_bin NOT NULL,
  `sjd` varchar(40) collate gb2312_bin NOT NULL,
  `sqsj` varchar(40) collate gb2312_bin NOT NULL,
  `sqzt` varchar(40) collate gb2312_bin NOT NULL,
  `yh` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_jsjy
-- ----------------------------
INSERT INTO `app_jsjy` VALUES ('1', '20240325220125', '123', '123123123', '101', '2024-03-26', '8:00~10:00', '2024-03-25 22:01:25', '完成', '123');
INSERT INTO `app_jsjy` VALUES ('2', '20240326103645', '123', '123', '101', '2024-03-27', '8:00~10:00', '2024-03-26 10:36:45', '完成', '123');

-- ----------------------------
-- Table structure for app_jsxx
-- ----------------------------
DROP TABLE IF EXISTS `app_jsxx`;
CREATE TABLE `app_jsxx` (
  `id` int(11) NOT NULL auto_increment,
  `jsmc` varchar(40) collate gb2312_bin NOT NULL,
  `wz` varchar(40) collate gb2312_bin NOT NULL,
  `bz` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_jsxx
-- ----------------------------
INSERT INTO `app_jsxx` VALUES ('1', '101', '111', '111');
INSERT INTO `app_jsxx` VALUES ('2', '102', '102', '102');
INSERT INTO `app_jsxx` VALUES ('3', '103', '103', '103');

-- ----------------------------
-- Table structure for app_kecheng
-- ----------------------------
DROP TABLE IF EXISTS `app_kecheng`;
CREATE TABLE `app_kecheng` (
  `id` int(11) NOT NULL auto_increment,
  `kcmc` varchar(40) collate gb2312_bin NOT NULL,
  `rkjs` varchar(40) collate gb2312_bin NOT NULL,
  `sm` varchar(400) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_kecheng
-- ----------------------------
INSERT INTO `app_kecheng` VALUES ('1', '软件工程', 'js', '123');
INSERT INTO `app_kecheng` VALUES ('2', '计算机原理', 'js1', '123123');
INSERT INTO `app_kecheng` VALUES ('3', '图像科学', 'js2', '12');

-- ----------------------------
-- Table structure for app_qiandao
-- ----------------------------
DROP TABLE IF EXISTS `app_qiandao`;
CREATE TABLE `app_qiandao` (
  `id` int(11) NOT NULL auto_increment,
  `sksj` varchar(40) collate gb2312_bin NOT NULL,
  `xs` varchar(40) collate gb2312_bin NOT NULL,
  `zt` varchar(40) collate gb2312_bin NOT NULL,
  `rq` varchar(40) collate gb2312_bin NOT NULL,
  `qdsj` varchar(40) collate gb2312_bin NOT NULL,
  `qtsj` varchar(40) collate gb2312_bin NOT NULL,
  `kc` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_qiandao
-- ----------------------------
INSERT INTO `app_qiandao` VALUES ('1', '13:00~15:00', '123', '已完成', '2024-03-26', '2024-03-26 13:44:16', '2024-03-26 15:04:03', '计算机原理');

-- ----------------------------
-- Table structure for app_sjd
-- ----------------------------
DROP TABLE IF EXISTS `app_sjd`;
CREATE TABLE `app_sjd` (
  `id` int(11) NOT NULL auto_increment,
  `sjd` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_sjd
-- ----------------------------
INSERT INTO `app_sjd` VALUES ('1', '8:00~10:00');
INSERT INTO `app_sjd` VALUES ('2', '10:00~12:00');
INSERT INTO `app_sjd` VALUES ('3', '13:00~15:00');
INSERT INTO `app_sjd` VALUES ('4', '15:00~17:00');

-- ----------------------------
-- Table structure for app_sksj
-- ----------------------------
DROP TABLE IF EXISTS `app_sksj`;
CREATE TABLE `app_sksj` (
  `id` int(11) NOT NULL auto_increment,
  `lsh` varchar(40) collate gb2312_bin NOT NULL,
  `xq` varchar(40) collate gb2312_bin NOT NULL,
  `sjd` varchar(40) collate gb2312_bin NOT NULL,
  `kc` varchar(40) collate gb2312_bin NOT NULL,
  `js` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_sksj
-- ----------------------------
INSERT INTO `app_sksj` VALUES ('1', '20240325202539', '星期一', '13:00~15:00', '软件工程', '102');
INSERT INTO `app_sksj` VALUES ('2', '20240325202546', '星期一', '8:00~10:00', '软件工程', '101');
INSERT INTO `app_sksj` VALUES ('3', '20240325202558', '星期五', '13:00~15:00', '计算机原理', '102');
INSERT INTO `app_sksj` VALUES ('4', '20240326131900', '星期二', '13:00~15:00', '计算机原理', '102');

-- ----------------------------
-- Table structure for app_xingqi
-- ----------------------------
DROP TABLE IF EXISTS `app_xingqi`;
CREATE TABLE `app_xingqi` (
  `id` int(11) NOT NULL auto_increment,
  `xq` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_xingqi
-- ----------------------------
INSERT INTO `app_xingqi` VALUES ('1', '星期一');
INSERT INTO `app_xingqi` VALUES ('2', '星期二');
INSERT INTO `app_xingqi` VALUES ('3', '星期三');
INSERT INTO `app_xingqi` VALUES ('4', '星期四');
INSERT INTO `app_xingqi` VALUES ('5', '星期五');
INSERT INTO `app_xingqi` VALUES ('6', '星期六');
INSERT INTO `app_xingqi` VALUES ('7', '星期日');

-- ----------------------------
-- Table structure for app_xuesheng
-- ----------------------------
DROP TABLE IF EXISTS `app_xuesheng`;
CREATE TABLE `app_xuesheng` (
  `id` int(11) NOT NULL auto_increment,
  `yhm` varchar(40) collate gb2312_bin NOT NULL,
  `mm` varchar(40) collate gb2312_bin NOT NULL,
  `xm` varchar(40) collate gb2312_bin NOT NULL,
  `lxdh` varchar(40) collate gb2312_bin NOT NULL,
  `zy` varchar(40) collate gb2312_bin NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=gb2312 COLLATE=gb2312_bin;

-- ----------------------------
-- Records of app_xuesheng
-- ----------------------------
INSERT INTO `app_xuesheng` VALUES ('1', '123', '123', '123', '123', '计算机');
INSERT INTO `app_xuesheng` VALUES ('2', '333', '333', '333', '12313', '计算机');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add gly', '7', 'add_gly');
INSERT INTO `auth_permission` VALUES ('20', 'Can change gly', '7', 'change_gly');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete gly', '7', 'delete_gly');
INSERT INTO `auth_permission` VALUES ('22', 'Can add jiaoshi', '8', 'add_jiaoshi');
INSERT INTO `auth_permission` VALUES ('23', 'Can change jiaoshi', '8', 'change_jiaoshi');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete jiaoshi', '8', 'delete_jiaoshi');
INSERT INTO `auth_permission` VALUES ('25', 'Can add jsjy', '9', 'add_jsjy');
INSERT INTO `auth_permission` VALUES ('26', 'Can change jsjy', '9', 'change_jsjy');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete jsjy', '9', 'delete_jsjy');
INSERT INTO `auth_permission` VALUES ('28', 'Can add jsxx', '10', 'add_jsxx');
INSERT INTO `auth_permission` VALUES ('29', 'Can change jsxx', '10', 'change_jsxx');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete jsxx', '10', 'delete_jsxx');
INSERT INTO `auth_permission` VALUES ('31', 'Can add kecheng', '11', 'add_kecheng');
INSERT INTO `auth_permission` VALUES ('32', 'Can change kecheng', '11', 'change_kecheng');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete kecheng', '11', 'delete_kecheng');
INSERT INTO `auth_permission` VALUES ('34', 'Can add qiandao', '12', 'add_qiandao');
INSERT INTO `auth_permission` VALUES ('35', 'Can change qiandao', '12', 'change_qiandao');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete qiandao', '12', 'delete_qiandao');
INSERT INTO `auth_permission` VALUES ('37', 'Can add sjd', '13', 'add_sjd');
INSERT INTO `auth_permission` VALUES ('38', 'Can change sjd', '13', 'change_sjd');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete sjd', '13', 'delete_sjd');
INSERT INTO `auth_permission` VALUES ('40', 'Can add sksj', '14', 'add_sksj');
INSERT INTO `auth_permission` VALUES ('41', 'Can change sksj', '14', 'change_sksj');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete sksj', '14', 'delete_sksj');
INSERT INTO `auth_permission` VALUES ('43', 'Can add xingqi', '15', 'add_xingqi');
INSERT INTO `auth_permission` VALUES ('44', 'Can change xingqi', '15', 'change_xingqi');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete xingqi', '15', 'delete_xingqi');
INSERT INTO `auth_permission` VALUES ('46', 'Can add xuesheng', '16', 'add_xuesheng');
INSERT INTO `auth_permission` VALUES ('47', 'Can change xuesheng', '16', 'change_xuesheng');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete xuesheng', '16', 'delete_xuesheng');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `password` varchar(128) NOT NULL,
  `last_login` datetime default NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) default NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('7', 'app', 'gly');
INSERT INTO `django_content_type` VALUES ('8', 'app', 'jiaoshi');
INSERT INTO `django_content_type` VALUES ('9', 'app', 'jsjy');
INSERT INTO `django_content_type` VALUES ('10', 'app', 'jsxx');
INSERT INTO `django_content_type` VALUES ('11', 'app', 'kecheng');
INSERT INTO `django_content_type` VALUES ('12', 'app', 'qiandao');
INSERT INTO `django_content_type` VALUES ('13', 'app', 'sjd');
INSERT INTO `django_content_type` VALUES ('14', 'app', 'sksj');
INSERT INTO `django_content_type` VALUES ('15', 'app', 'xingqi');
INSERT INTO `django_content_type` VALUES ('16', 'app', 'xuesheng');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL auto_increment,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2024-03-25 06:05:56');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2024-03-25 06:05:58');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2024-03-25 06:05:59');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2024-03-25 06:05:59');
INSERT INTO `django_migrations` VALUES ('15', 'sessions', '0001_initial', '2024-03-25 06:05:59');
INSERT INTO `django_migrations` VALUES ('17', 'app', '0001_initial', '2024-03-25 08:19:50');
INSERT INTO `django_migrations` VALUES ('18', 'app', '0002_jiaoshi_jsjy_jsxx_kecheng_qiandao_sjd_sksj_xingqi_xuesheng', '2024-03-25 08:19:52');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of django_session
-- ----------------------------
