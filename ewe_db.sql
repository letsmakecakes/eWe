/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.20-log : Database - ewe
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`ewe` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ewe`;

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `Acid` int(11) NOT NULL AUTO_INCREMENT,
  `account_no` varchar(50) DEFAULT NULL,
  `debit_creditcardno` varchar(50) DEFAULT NULL,
  `cif_no` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `cvv` varchar(100) DEFAULT NULL,
  `balance` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Acid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

insert  into `bank`(`Acid`,`account_no`,`debit_creditcardno`,`cif_no`,`name`,`cvv`,`balance`) values (1,'12345678','1234567890123456','12345678','anvi','123','67609'),(2,'34567890','1234567890345678','98765431','admin','356','1031390');

/*Table structure for table `cart` */

DROP TABLE IF EXISTS `cart`;

CREATE TABLE `cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `order_status` varchar(30) DEFAULT NULL,
  `bill_no` int(11) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `cart` */

insert  into `cart`(`cart_id`,`product_id`,`customer_id`,`quantity`,`order_status`,`bill_no`,`date`) values (1,235,122,1,'booked',1,'2020-03-04 15:23:26'),(2,235,122,1,'cart',2,'2020-03-05 11:45:32'),(3,235,122,1,'cart',2,'2020-03-05 13:30:29'),(4,240,122,1,'cart',2,'2020-03-05 13:30:36');

/*Table structure for table `comments` */

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `commentid` int(11) NOT NULL AUTO_INCREMENT,
  `entrepreneur_id` int(11) NOT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`commentid`,`entrepreneur_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `comments` */

insert  into `comments`(`commentid`,`entrepreneur_id`,`comment`) values (1,349,'hshjdsdsjdsn'),(2,345,'gfcjgfj');

/*Table structure for table `conference` */

DROP TABLE IF EXISTS `conference`;

CREATE TABLE `conference` (
  `conferenceid` int(11) NOT NULL AUTO_INCREMENT,
  `conference_name` varchar(20) DEFAULT NULL,
  `conference_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`conferenceid`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `conference` */

insert  into `conference`(`conferenceid`,`conference_name`,`conference_description`) values (3,'jhgkj','kjhbk,mn ,');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(20) DEFAULT NULL,
  `emailid` varchar(30) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `phoneno` varchar(12) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `state` varchar(10) DEFAULT NULL,
  `district` varchar(10) DEFAULT NULL,
  `pin` varchar(10) DEFAULT NULL,
  `profile_image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=368 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`customer_name`,`emailid`,`date_of_birth`,`phoneno`,`place`,`state`,`district`,`pin`,`profile_image`) values (122,'Deepna PV','deepnapv@gmail.com','2020-02-20','678829197','hdfjsdsndsnd','Kerala','knr','670301','/static/Images/g1.jpg'),(367,'Deepna','deepnapv@gmail.com','2020-02-07','682682921','hjjskkaajsns','Kerala','knr','670301','/static/Images/g2.jpg');

/*Table structure for table `customer_feedback` */

DROP TABLE IF EXISTS `customer_feedback`;

CREATE TABLE `customer_feedback` (
  `cus_fid` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `review` varchar(453) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`cus_fid`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `customer_feedback` */

insert  into `customer_feedback`(`cus_fid`,`customer_id`,`product_id`,`review`,`date`) values (1,122,235,'hgdhg','2020-03-05'),(2,122,235,'very good material...comfortable one....','2020-03-06');

/*Table structure for table `entrepreneur` */

DROP TABLE IF EXISTS `entrepreneur`;

CREATE TABLE `entrepreneur` (
  `entrepreneur_id` int(11) NOT NULL,
  `entrepreneur_name` varchar(50) DEFAULT NULL,
  `emailid` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `phone_no` bigint(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `group` varchar(5) DEFAULT NULL,
  `profile_image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`entrepreneur_id`)
) ENGINE=MyISAM AUTO_INCREMENT=457 DEFAULT CHARSET=latin1;

/*Data for the table `entrepreneur` */

insert  into `entrepreneur`(`entrepreneur_id`,`entrepreneur_name`,`emailid`,`date_of_birth`,`phone_no`,`place`,`pin`,`district`,`group`,`profile_image`) values (368,'Adwaith Rajeev','adwaithrajeev@gmail.com','2020-02-13',9061081745,'hkjhkj',670301,'knr','Yes','/static/Images/b1.jpg'),(345,'Deepna K','ddepna@gmail.com','2010-02-09',9061081740,'tly',789876,'kannur','Yes','/static/Images/g1.jpg'),(369,'Haritha P','h@gmail.com','1997-07-24',9876543212,'haritha Nivas',678765,'Kannur','No','/static/Images/g2.jpg');

/*Table structure for table `help` */

DROP TABLE IF EXISTS `help`;

CREATE TABLE `help` (
  `helpid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `emailid` varchar(20) DEFAULT NULL,
  `contactno` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`helpid`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `help` */

insert  into `help`(`helpid`,`name`,`emailid`,`contactno`) values (1,'Hariharan TP','hariharan123@gmail.c',8796543217),(3,'Midhun K','midhunk987@gmail.com',8796543299);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=370 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`type`) values (134,'admin','admin','admin'),(345,'ent','ent','ent'),(122,'user','user','user'),(366,'adwaithrajeev@gmail.com','Adwaith','ent'),(368,'adwaithrajeev@gmail.com','Adwaith','ent'),(367,'deepnapv@gmail.com','Deepna','user'),(369,'h@gmail.com','123456','ent');

/*Table structure for table `material` */

DROP TABLE IF EXISTS `material`;

CREATE TABLE `material` (
  `materialid` int(11) NOT NULL AUTO_INCREMENT,
  `material` varchar(20) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `pic` varchar(800) DEFAULT NULL,
  `stock` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`materialid`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `material` */

insert  into `material`(`materialid`,`material`,`description`,`pic`,`stock`) values (1,'oils','for soap manufacturing','/static/Images/oil.jpg',10),(2,'machine','for tailoring','/static/Images/pr_ta2.jpg',4),(3,'glycerine','glycerine is needed for soap manufacturing','/static/Images/glycerine.png',5),(4,'tailoring kit','super kit for faster tailoring','/static/Images/pr_ta1.jpg',2),(5,'soapkit','superkit for soap manufacturing','/static/Images/soap1.jpg',3),(6,'yarn','16 yarns in one packet','/static/Images/yarn.jpg',4);

/*Table structure for table `material_request` */

DROP TABLE IF EXISTS `material_request`;

CREATE TABLE `material_request` (
  `material_req` int(11) NOT NULL AUTO_INCREMENT,
  `entrepreneur_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `quantity` bigint(20) DEFAULT NULL,
  `status` varchar(90) DEFAULT NULL,
  `material_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`material_req`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `material_request` */

insert  into `material_request`(`material_req`,`entrepreneur_id`,`date`,`quantity`,`status`,`material_id`) values (1,345,'2020-03-06',1,'accept',3),(2,345,'2020-03-06',2,'pending',3);

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification_name` varchar(700) DEFAULT NULL,
  `notification_description` varchar(900) DEFAULT NULL,
  `notification_date` date DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=681 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification_name`,`notification_description`,`notification_date`) values (679,'gdhgf','bmnbmn','2020-03-10'),(680,'new materials are added','materials according to your feedback was launched soon','2020-03-03');

/*Table structure for table `otp` */

DROP TABLE IF EXISTS `otp`;

CREATE TABLE `otp` (
  `otp_id` int(11) NOT NULL AUTO_INCREMENT,
  `otpvalue` varchar(40) DEFAULT NULL,
  `upiid` int(11) DEFAULT NULL,
  PRIMARY KEY (`otp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

/*Data for the table `otp` */

insert  into `otp`(`otp_id`,`otpvalue`,`upiid`) values (1,'7169',0),(2,'6576',0),(3,'5770',1),(4,'6175',1),(5,'7753',1),(6,'770',1),(7,'8171',1),(8,'8636',1),(9,'2810',1),(10,'5085',1),(11,'7160',1),(12,'8404',1),(13,'852',1),(14,'6334',1),(15,'5579',1),(16,'3859',1),(17,'6099',1),(18,'2396',1),(19,'2601',1),(20,'7500',1),(21,'1428',1),(22,'2572',1),(23,'3141',1),(24,'5891',1),(25,'5630',1),(26,'748',1),(27,'8567',1),(28,'5700',1),(29,'5126',1),(30,'2576',1),(31,'7907',1),(32,'5221',1);

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `paymentid` int(11) NOT NULL AUTO_INCREMENT,
  `date_of_payment` date DEFAULT NULL,
  `order_id` int(11) NOT NULL,
  `account_number` bigint(20) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  PRIMARY KEY (`paymentid`,`order_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(20) DEFAULT NULL,
  `product_prize` float DEFAULT NULL,
  `product_size` char(1) DEFAULT NULL,
  `product_description` varchar(100) DEFAULT NULL,
  `product_stock` varchar(10) DEFAULT NULL,
  `entrepreneur_id` int(11) DEFAULT NULL,
  `product_image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=245 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`product_name`,`product_prize`,`product_size`,`product_description`,`product_stock`,`entrepreneur_id`,`product_image`) values (235,'Saree',1200,'L','agajsansbasgagsashaj','5',345,'/static/Images/s1.jpg'),(240,'Dress',999,'L','hssaajanan','2',345,'/static/Images/s2.jpg'),(241,'saree',1500,'X','cotton mix rayon material','2',345,'/static/Images/sare.jpg'),(242,'saree',1100,'X','simple saree with thick border','3',345,'/static/Images/s4.jpg'),(243,'saree',1100,'X','simple saree with thick border','3',345,'/static/Images/s3.jpg'),(244,'saree',1100,'X','simple saree with thick border','3',345,'/static/Images/s5.jpg');

/*Table structure for table `training` */

DROP TABLE IF EXISTS `training`;

CREATE TABLE `training` (
  `session_no` int(11) NOT NULL AUTO_INCREMENT,
  `session_name` varchar(20) DEFAULT NULL,
  `session_details` varchar(100) DEFAULT NULL,
  `trainee` varchar(10) DEFAULT NULL,
  `trainee_description` varchar(100) DEFAULT NULL,
  `file` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`session_no`)
) ENGINE=MyISAM AUTO_INCREMENT=348 DEFAULT CHARSET=latin1;

/*Data for the table `training` */

insert  into `training`(`session_no`,`session_name`,`session_details`,`trainee`,`trainee_description`,`file`) values (346,'Tailoring','sghssjjs','Conan','dhjsjsks','/static/Videos/20200217-143146.mp4'),(347,'Soap Manufacturing','soapkjbjkb','jaine','fyufyfgvh','/static/Videos/20200217-143146.mp4');

/*Table structure for table `training_feedback` */

DROP TABLE IF EXISTS `training_feedback`;

CREATE TABLE `training_feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `entrepreneur_id` int(11) DEFAULT NULL,
  `session_no` bigint(20) DEFAULT NULL,
  `review` varchar(50) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `training_feedback` */

insert  into `training_feedback`(`feedback_id`,`entrepreneur_id`,`session_no`,`review`,`rating`,`date`) values (1,349,346,'hsajadhsjs',7,'2020-02-20'),(2,345,346,'very good',5,'2020-02-20'),(7,345,346,'jhvfjhf',7,'2020-03-05'),(8,345,346,'Your guidance is very beneficiable',4,'2020-03-06');

/*Table structure for table `upiids` */

DROP TABLE IF EXISTS `upiids`;

CREATE TABLE `upiids` (
  `upi_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) DEFAULT NULL,
  `upiid` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`upi_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `upiids` */

insert  into `upiids`(`upi_id`,`account_id`,`upiid`) values (1,1,'hello');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
