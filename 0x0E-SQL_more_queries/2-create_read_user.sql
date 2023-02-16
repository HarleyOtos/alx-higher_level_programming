-- creates the database 'hbtn_0d_2' and the user 'user_0d_2'
-- 'user_0d_2' only SELECT privilege in 'hbtn_0d_2'
-- 'user_0d_2' password set to 'user_0d_2_pwd'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER IF 'user_0d_2'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
