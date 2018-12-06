CREATE DATABASE final;

USE final;

CREATE TABLE datos(
    id int(10) NOT NULL PRIMARY KEY,
    nombre varchar(32) NOT NULL
    precio int(10) NOT NULL
    existencia int(10) NOT NULL

)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO datos (id, nombre,precio,existencia)
VALUES ('898','llaves','34',"14"),('14','chapa','44','55');

SHOW TABLES;

SELECT * FROM datos;

DESCRIBE datos;

SELECT "Creando un usuario y asignandolo a la base de datos" as "Mensaje";
CREATE USER 'unid2'@'localhost' IDENTIFIED BY 'unid.2018';
-- CREATE USER 'kuorra'@'localhost' IDENTIFIED BY 'kuorra.2018';
GRANT ALL PRIVILEGES ON final.* TO 'unid2'@'localhost';
-- GRANT ALL PRIVILEGES ON base_demo.* TO kuorra@'%' IDENTIFIED BY 'kuorra.remote';

FLUSH PRIVILEGES;
