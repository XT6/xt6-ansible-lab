#!/bin/bash

# -- Creo usuario administrador y discovery inicial
#
/usr/bin/php7.2 /opt/observium/discovery.php -u
/usr/bin/php7.2 /opt/observium/discovery.php -h all
/usr/bin/php7.2 /opt/observium/adduser.php admin AdminLAC2019 10
/usr/bin/php7.2 /opt/observium/poller.php -h all

# -- Agrega los hosts a monitorear
/usr/bin/php7.2 /opt/observium/add_device.php /opt/observium/hosts.txt


