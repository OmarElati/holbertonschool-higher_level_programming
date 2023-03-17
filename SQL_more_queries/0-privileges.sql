-- script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server.
CREATE USER 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
