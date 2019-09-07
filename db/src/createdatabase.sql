
CREATE USER backend IDENTIFIED WITH mysql_native_password BY 'pass';
GRANT ALL PRIVILEGES ON redditeye.* TO 'backend'@'%' WITH GRANT OPTION;

CREATE USER phpmyadmin IDENTIFIED WITH mysql_native_password BY 'pass';
GRANT ALL PRIVILEGES ON redditeye.* TO 'phpmyadmin'@'%' WITH GRANT OPTION;
