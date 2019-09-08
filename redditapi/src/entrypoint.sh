#!/bin/bash

set -x

# wait for mysql
until [ -n "$mysqlIsRunning" ]
do
	if [[ $(telnet $MYSQL_HOSTNAME 3306) == *"Connected to $MYSQL_HOSTNAME."* ]]
	then
		mysqlIsRunning="mysqlIsRunning"
	fi
	sleep 2
done

# run flask server
python3 app.py