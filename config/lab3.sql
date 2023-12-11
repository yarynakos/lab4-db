CREATE DATABASE IF NOT EXISTS ajax;
USE ajax;

DROP TABLE IF EXISTS notification;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS systems;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS sensor;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS zone;
DROP TABLE IF EXISTS access_level;
DROP TABLE IF EXISTS object;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

CREATE TABLE country (
 country_name VARCHAR(100) PRIMARY KEY
) ENGINE = InnoDB;

CREATE TABLE city (
city_id INT AUTO_INCREMENT PRIMARY KEY,
city_name VARCHAR(100) NOT NULL,
country_name VARCHAR(100) NOT NULL
)ENGINE = InnoDB;

ALTER TABLE city
ADD CONSTRAINT FK_country_name
FOREIGN KEY (country_name)
REFERENCES country(country_name);

CREATE TABLE object (
object_id INT AUTO_INCREMENT PRIMARY KEY,
type_of_object VARCHAR(45) NOT NULL,
number_of_flors INT NOT NULL,
city_id INT NOT NULL
)ENGINE = InnoDB;

ALTER TABLE object
ADD CONSTRAINT FK_city_id
FOREIGN KEY (city_id)
REFERENCES city(city_id);

CREATE TABLE access_level (
access_level_name VARCHAR(45) PRIMARY KEY
)ENGINE = InnoDB;

CREATE TABLE zone (
zone_id INT AUTO_INCREMENT PRIMARY KEY,
zone_name VARCHAR(45) NOT NULL,
access_level_name VARCHAR(45) NOT NULL,
object_id INT NOT NULL
)ENGINE = InnoDB;

ALTER TABLE zone
ADD CONSTRAINT FK_access_level_name_zone
FOREIGN KEY (access_level_name)
REFERENCES access_level(access_level_name),

ADD CONSTRAINT FK_object_id_zone
FOREIGN KEY (object_id)
REFERENCES object(object_id);

CREATE TABLE room (
room_id INT AUTO_INCREMENT PRIMARY KEY,
room_name VARCHAR(45) NOT NULL,
type_of_room VARCHAR(45) NOT NULL,
object_id INT NOT NULL,
zone_id INT NOT NULL
)ENGINE = InnoDB;

ALTER TABLE room
ADD CONSTRAINT FK_object_id_room
FOREIGN KEY (object_id)
REFERENCES object(object_id),

ADD CONSTRAINT FK_zone_id
FOREIGN KEY (zone_id)
REFERENCES zone(zone_id);

CREATE TABLE sensor (
sensor_id INT AUTO_INCREMENT PRIMARY KEY,
type_of_sensor VARCHAR(45) NOT NULL,
measurement_radius DOUBLE NOT NULL,
room_id INT NOT NULL
)ENGINE = InnoDB;

ALTER TABLE sensor
ADD CONSTRAINT FK_room_id
FOREIGN KEY (room_id)
REFERENCES room(room_id);

CREATE TABLE schedule (
schedule_id INT AUTO_INCREMENT PRIMARY KEY,
start_time TIME NOT NULL,
finish_time TIME NOT NULL,
break_time TIME NOT NULL,
sensor_id INT NOT NULL
)ENGINE = InnoDB;

ALTER TABLE schedule
ADD CONSTRAINT FK_sensor_id_schedule
FOREIGN KEY (sensor_id)
REFERENCES sensor(sensor_id);

CREATE TABLE user (
user_id INT AUTO_INCREMENT PRIMARY KEY,
surname VARCHAR(75) NOT NULL,
name VARCHAR(45) NOT NULL,
phone VARCHAR(13) NOT NULL,
email VARCHAR(45),
access_level_name VARCHAR(45) NOT NULL
)ENGINE = InnoDB;

ALTER TABLE user
ADD CONSTRAINT FK_access_level_name_user
FOREIGN KEY (access_level_name)
REFERENCES access_level(access_level_name);

CREATE TABLE systems (
    system_id INT PRIMARY KEY,
    system_name VARCHAR(45)
) ENGINE = InnoDB;

CREATE TABLE notification (
notification_id INT AUTO_INCREMENT PRIMARY KEY,
type_of_notification VARCHAR(45),
time_of_notification TIME NOT NULL,
text_of_notification VARCHAR(100),
user_id INT NOT NULL,
object_id INT NOT NULL,
sensor_id INT NOT NULL,
system_id INT NOT NULL
)ENGINE = InnoDB;

ALTER TABLE notification
ADD CONSTRAINT FK_user_id
FOREIGN KEY (user_id)
REFERENCES user(user_id),

ADD CONSTRAINT object_id_notification
FOREIGN KEY (object_id)
REFERENCES object(object_id),

ADD CONSTRAINT sensor_id_notification
FOREIGN KEY (sensor_id)
REFERENCES sensor(sensor_id),

ADD CONSTRAINT systems
FOREIGN KEY (system_id)
REFERENCES systems(system_id);

INSERT INTO country (country_name)
VALUE ('Ukraine'),
('Poland'),
('USA'),
( 'France'),
('Italy'),
('Romania'),
('Canada'),
('UK'),
('Turkey'),
('Moldova');
INSERT INTO city (city_id, city_name, country_name)
VALUES (1, 'Lviv', 'Ukraine'),
(2, 'Warshaw', 'Poland'),
(3, 'Boston', 'USA'),
(4, 'Paris', 'France'),
(5, 'Rome', 'Italy'),
(6, 'Bucharest', 'Romania'),
(7, 'Ottawa', 'Canada'),
(8, 'London', 'UK'),
(9, 'Ankara', 'Turkey'),
(10, 'Chisinau', 'Moldova');
INSERT INTO object (object_id, type_of_object, number_of_flors, city_id)
VALUES (11, 'house', 3, 1),
(12, 'storage', 2, 2),
(13, 'shopping center', 5, 3),
(14, 'school', 4, 4),
(15, 'university', 9, 5),
(16, 'parking', 7, 6),
(17, 'bank', 3, 7),
(18, 'museum', 1, 8),
(19, 'school', 2, 9),
(20, 'jewelry store', 1, 10);
INSERT INTO access_level (access_level_name)
VALUE ('NORMAL'),
( 'OWNER'),
('GUEST'),
('LOW1'),
('LOW2'),
('LOW3'),
('LOW4'),
('LOW5'),
('LOW6'),
('HIGHT');
INSERT INTO zone (zone_id, zone_name, access_level_name, object_id )
VALUES (21, 'zone 1', 'NORMAL',11),
( 22, 'zone 2', 'OWNER', 12),
( 23, 'zone 3', 'GUEST', 13),
(24, 'zone 4', 'LOW1',15),
(25, 'zone 5', 'LOW2',16),
(26, 'zone 6', 'LOW3',17),
(27, 'zone 7', 'LOW4',18),
(28, 'zone 8', 'LOW5',19),
(29, 'zone 9', 'LOW6',14),
(30, 'zone 10', 'HIGHT',20);
INSERT INTO room (room_id, room_name, object_id, zone_id, type_of_room)
VALUES (31, 'living room', 11, 21, 'living room'),
(32, 'corridor', 12, 22, 'corridor'),
(33, 'store', 13, 23, 'store'),
(34, 'classroom', 14, 24, 'classroom'),
(35, 'corridor', 15, 25, 'corridor'),
(36, 'living room', 16, 26, 'living room'),
(37, 'corridor', 17, 27, 'corridor'),
(38, 'living room', 18, 28, 'living room'),
(39, 'corridor', 19, 29, 'corridor'),
(40, 'safe', 20, 30, 'safe');
INSERT INTO sensor (sensor_id, type_of_sensor, measurement_radius, room_id)
Values (41, 'light', 10.0, 31),
(42, 'smoke', 5.0, 32),
(43, 'water', 2.5, 33),
(44, 'movement', 10.0, 34),
(45, 'light', 11.0, 35),
(46, 'smoke', 5.0, 36),
(47, 'water', 2.5, 37),
(48, 'movement', 10.0, 38),
(49, 'smoke', 3,  39),
(50, 'blow', 3.7,  40);
INSERT INTO schedule (schedule_id, start_time, finish_time, break_time, sensor_id)
VALUES(51, '12:00', '13:00', '5:00', 41),
(52, '13:00', '14:00', '7:00', 42),
(53, '18:00', '17:00', '2:00', 43),
(54, '12:00', '13:00', '5:00', 44),
(55, '13:00', '14:00', '7:00', 45),
(56, '18:00', '17:00', '2:00', 46),
(57, '17:00', '18:00', '4:00', 47),
(58, '10:00', '11:00', '3:00', 48),
(59, '17:00', '18:00', '4:00', 49),
(60, '10:00', '11:00', '3:00', 50);
INSERT INTO user (user_id, surname, name, phone, email, access_level_name)
VALUES (61, 'Kos', 'Yaryna', '0987654321', 'yarynaaa@gmail.com', 'OWNER'),
(62, 'Vilkov', 'Igor', '0123456789', 'igoooor@gmail.com', 'HIGHT'),
(63, 'Shvets', 'Yulia', '0987789987', 'yuliaaaa@gmail.com', 'GUEST'),
(64, 'Kuhar', 'Taras', '0987612345', 'tarassss@gmail.com', 'NORMAL'),
(65, 'Hrabovska', 'Yaryna', '0123456789', 'hryaaa@gmail.com', 'LOW1'),
(66, 'Shvets', 'Taras', '0123496765', 'tarik@gmail.com', 'LOW2'),
(67, 'Kuhar', 'Natalia', '0123497765', 'natalya@gmail.com', 'LOW3'),
(68, 'Kos', 'Igor', '0123495765', 'kosss@gmail.com', 'LOW4'),
(69, 'Vilkov', 'Yaryna', '0123494765', 'yara@gmail.com', 'LOW5'),
(70, 'Vilkov', 'Taras', '0123493765', 'vt@gmail.com', 'LOW6');
INSERT INTO systems(system_id, system_name)
VALUES(81, 'SystemLabel'),
 (82, 'CoreSystem'),
 (83, 'PlatformName'),
 (84, 'NetworkAlias'),
 (85, 'MainframeID'),
 (86, 'CentralHub'),
 (87, 'MasterControl'),
 (88, 'CoreProcessor'),
 (89, 'SystemIdentity'),
 (90, 'UnifiedSystem');
INSERT INTO notification (notification_id, type_of_notification, time_of_notification, text_of_notification, object_id, sensor_id, user_id, system_id)
VALUES (71, 'SMS', '15:00', 'alarm', 11, 41, 61, 81),
(72, 'SMS', '15:00', 'alarm',12, 42, 62, 82),
(73, 'SMS', '15:00', 'alarm',13, 43, 63, 83),
(74, 'SMS', '15:00', 'alarm', 14, 44, 64, 84),
(75, 'SMS', '15:00', 'alarm',15, 45, 65, 85),
(76, 'SMS', '15:00', 'alarm',16, 46, 66, 86),
(77, 'SMS', '15:00', 'alarm',17, 47, 67, 87),
(78, 'SMS', '15:00', 'alarm',18, 48, 68, 88),
(79, 'SMS', '15:00', 'alarm',19, 49, 69, 89),
(80, 'SMS', '15:00', 'alarm',20, 50, 70, 90);

CREATE INDEX index_city_name ON city(city_name);
CREATE INDEX index_type_of_object ON object(type_of_object);
CREATE INDEX index_number_of_flors ON object(number_of_flors);
CREATE INDEX index_zone_name ON zone(zone_name);
CREATE INDEX index_room_name ON room(room_name);
CREATE INDEX index_type_of_room ON room(type_of_room);
CREATE INDEX index_start_time ON schedule(start_time);
CREATE INDEX index_finish_time ON schedule(finish_time);
CREATE INDEX index_surname ON user(surname);
CREATE INDEX index_name ON user(name);
CREATE INDEX index_type_of_notification ON notification(type_of_notification);
CREATE INDEX index_text_of_notification ON notification(text_of_notification);
