/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - weed detection
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`weed detection` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `weed detection`;

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `ch_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`ch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`ch_id`,`from_id`,`to_id`,`message`,`date`,`time`) values 
(1,8,3,'hlo','2023-05-02','15:08:49'),
(2,8,3,'hloo','2023-05-02','15:21:35'),
(3,8,3,'hi\r\n','2023-05-02','15:21:51'),
(4,2,7,'hlo','2023-05-02','15:53:39'),
(5,2,7,'hh','2023-05-02','16:02:11'),
(6,2,7,'hi\r\n','2023-05-02','16:02:54'),
(7,2,7,'hlooo','2023-05-02','16:06:48'),
(8,2,9,'hlo\r\n','2023-05-02','16:22:44'),
(9,2,9,'hlioo','2023-05-02','16:22:52'),
(10,3,8,'hlo\r\n','2023-05-02','16:26:38');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `complaints` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`cid`,`lid`,`complaints`,`reply`,`date`) values 
(1,3,'not good','take','0000-00-00'),
(2,8,'aa','ok','2023-04-01'),
(3,8,'aa','pending','2023-04-01'),
(4,8,'difficult','pending','2023-04-27'),
(5,8,'hlo','pending','2023-04-27'),
(6,8,'hlo','pending','2023-04-27'),
(7,8,'hisana nasreen','pending','2023-04-27'),
(8,8,'bad','pending','2023-05-03'),
(9,8,'oh','pending','2023-05-03');

/*Table structure for table `crop` */

DROP TABLE IF EXISTS `crop`;

CREATE TABLE `crop` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `crops` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `crop` */

insert  into `crop`(`cid`,`crops`,`details`,`date`) values 
(2,'pepper','mmm','2023-03-15'),
(3,'aaa','abc','2023-03-15'),
(4,'xyz','aabbcc','2023-03-15');

/*Table structure for table `expert` */

DROP TABLE IF EXISTS `expert`;

CREATE TABLE `expert` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `expert` */

insert  into `expert`(`eid`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,2,'hisana','nasreen','tnr','abc',676302,8541,'hisa@gmail.com'),
(2,4,'fasii','la','mlprm','tanur',676302,2443096,'fasila@gmail.com'),
(3,5,'anju','k','kochi','aluva',678909,9847474523,'anju@gmail.com');

/*Table structure for table `farming_method` */

DROP TABLE IF EXISTS `farming_method`;

CREATE TABLE `farming_method` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fmethod` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `farming_method` */

insert  into `farming_method`(`fid`,`lid`,`fmethod`,`details`,`date`) values 
(7,2,'cultivations','good','2023-04-01');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`uid`,`feedback`,`date`) values 
(1,8,'hello','2023-04-27'),
(2,8,'hello','2023-04-27'),
(3,8,'hlo','2023-04-27'),
(4,8,'hlo','2023-04-27'),
(5,8,'gdmng','2023-04-27'),
(6,8,'hloooo','2023-04-27'),
(7,8,'hloooo','2023-04-27');

/*Table structure for table `fertilization` */

DROP TABLE IF EXISTS `fertilization`;

CREATE TABLE `fertilization` (
  `fid` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `fertilization` */

insert  into `fertilization`(`fid`,`name`,`details`) values 
(7,'admin','dfgh');

/*Table structure for table `gov_policy` */

DROP TABLE IF EXISTS `gov_policy`;

CREATE TABLE `gov_policy` (
  `g_id` int(11) NOT NULL AUTO_INCREMENT,
  `policy` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`g_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `gov_policy` */

insert  into `gov_policy`(`g_id`,`policy`,`details`,`date`) values 
(2,'frmng','kerala','2023-03-15'),
(3,'abc','bloooo','2023-03-19');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'soorya','soorya','Expert'),
(3,'123','123','Expert'),
(4,'fasila','fasila','Expert'),
(5,'anju','Anju12345','Expert'),
(6,'soorya','soorya','user'),
(7,'','shamli','user'),
(8,'shamli','shamli','user'),
(9,'shamli','shamli','user'),
(10,'far','Asdf@23456','user'),
(11,'far','Asdf@23456','user'),
(12,'far','Asdf@23456','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`id`,`notification`,`date`) values 
(1,'helloo all','0000-00-00'),
(3,'haiiiiiiiiiiiiiiiiiiiii','2023-03-16');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int(100) NOT NULL,
  `phone` bigint(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`email`) values 
(0,0,'','','','',0,0,''),
(2,7,'safna','shamli','tirur','tirur',676302,2443098,'shamli@gmail.com'),
(3,8,'safna','shamli','tirur','tirur',676302,2443098,'shamli@gmail.com'),
(4,9,'safna','shamli','tirur','tirur',676302,2443098,'shamli@gmail.com'),
(5,10,'farhana','apg','pattambi','pattanbi',999999,9090908989,'df@gmm.bnm'),
(6,11,'farhana','apg','pattambi','pattanbi',999999,9090908989,'df@gmm.bnm'),
(7,12,'farhana','apg','pattambi','pattanbi',999999,9090908989,'df@gmm.bnm');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
