USE ajax;

DROP TRIGGER IF EXISTS check_if_id_is_unique;
DROP TRIGGER IF EXISTS check_if_update_can_be;
DROP TRIGGER IF EXISTS check_if_delete_can_be;
DROP PROCEDURE IF EXISTS add_country;
DROP PROCEDURE IF EXISTS add_ten_cities;
DROP FUNCTION IF EXISTS find_min_flors;
DROP PROCEDURE IF EXISTS add_new_db;
DROP TRIGGER IF EXISTS check_name_what_end_with_two_zero;
DROP TRIGGER IF EXISTS check_if_name_is_from_list;
DROP TRIGGER IF EXISTS log_city;

DELIMITER //

CREATE TRIGGER check_if_id_is_unique
	BEFORE INSERT
    ON systems
    FOR EACH ROW
BEGIN
	DECLARE isDone BOOLEAN DEFAULT FALSE;
    DECLARE s_name VARCHAR(45);
	DECLARE cursor_system CURSOR FOR SELECT system_name FROM systems;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET isDone = TRUE;
    OPEN cursor_system;
    curs_loop: LOOP
		FETCH cursor_system INTO s_name;
        IF isDone = TRUE THEN LEAVE curs_loop;
        END IF;
        IF new.System_name = s_name THEN
			SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "Name is allready exists";
		END IF;
        END LOOP;
	CLOSE cursor_system;
END//

CREATE TRIGGER check_if_update_can_be
	BEFORE UPDATE
    ON systems
    FOR EACH ROW
BEGIN
	DECLARE isDone BOOLEAN DEFAULT FALSE;
    DECLARE s_id INT;
	DECLARE cursor_notification CURSOR FOR SELECT system_id FROM notification;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET isDone = TRUE;
    OPEN cursor_notification;
    curs_loop: LOOP
		FETCH cursor_notification INTO s_id;
        IF isDone = TRUE THEN LEAVE curs_loop;
        END IF;
        IF old.System_id = s_id THEN
			SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "This system have dependecy";
		END IF;
        END LOOP;
	CLOSE cursor_notification;
END//

CREATE TRIGGER check_if_delete_can_be
	BEFORE DELETE
    ON systems
    FOR EACH ROW
BEGIN
	DECLARE isDone BOOLEAN DEFAULT FALSE;
    DECLARE s_id INT;
	DECLARE cursor_notification CURSOR FOR SELECT system_id FROM notification;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET isDone = TRUE;
    OPEN cursor_notification;
    curs_loop: LOOP
		FETCH cursor_notification INTO s_id;
        IF isDone = TRUE THEN LEAVE curs_loop;
        END IF;
        IF old.System_id = s_id THEN
			SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "This system have dependecy";
		END IF;
        END LOOP;
	CLOSE cursor_notification;
END//

CREATE PROCEDURE add_country (IN name VARCHAR(45))
BEGIN
	INSERT INTO country VALUES(name);
END//

CREATE PROCEDURE add_ten_cities (IN cityName VARCHAR(45))
BEGIN
	DECLARE count int;
    SET count = 1;
    addName: LOOP
		IF count > 10 THEN LEAVE addName;
        END IF;
		INSERT INTO city(name, country_name) VALUES(CONCAT(cityName, "-", count), "France");
        SET count = count + 1;
	END LOOP;
END//

CREATE FUNCTION find_min_flors() RETURNS FLOAT DETERMINISTIC
BEGIN
	RETURN(SELECT MIN(number_of_flors) FROM object);
END//

SELECT find_min_flors()//

CREATE PROCEDURE add_new_db()
BEGIN
	DECLARE isDone BOOLEAN DEFAULT FALSE;
    DECLARE s_name VARCHAR(45);
	DECLARE cursor_access_level_name CURSOR FOR SELECT access_level_name FROM access_level;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET isDone = TRUE;
    OPEN cursor_access_level_name;
    curs_loop: LOOP
		FETCH cursor_access_level_name INTO s_name;
        IF isDone = TRUE THEN LEAVE curs_loop;
        END IF;
        SET @commandDB = CONCAT("CREATE DATABASE ", s_name);
        PREPARE myquery FROM @commandDB;
        EXECUTE myquery;
        DEALLOCATE PREPARE myquery;
        END LOOP;
	CLOSE cursor_access_level_name;
END//

CREATE TRIGGER check_name_what_end_with_two_zero
	BEFORE INSERT
    ON country
    FOR EACH ROW
BEGIN
	IF (new.Country_name REGEXP("00$")) THEN
		SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "Name can not end with two 0";
	END IF;
END //

CREATE TRIGGER check_if_name_is_from_list
	BEFORE INSERT
    ON user
    FOR EACH ROW
BEGIN
	IF(new.Name NOT REGEXP("(Svitlana|Petro|Olha|Taras)")) THEN
		SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "Name is not from list";
	END IF;
END //

CREATE TRIGGER log_city
	AFTER INSERT
	ON city
    FOR EACH ROW
BEGIN
	INSERT INTO city_log (city_id, city_name, country_name, date) VALUES (new.City_id, new.City_name, new.Country_name, NOW());
END//
