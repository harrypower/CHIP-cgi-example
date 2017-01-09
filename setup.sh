#!/bin/bash

sudo rm /var/www/html/index.html
sudo rm /usr/lib/cgi-bin/Gforthmail.cgi
sudo rm /usr/lib/cgi-bin/Gforthmailget.cgi
sudo rm /usr/lib/cgi-bin/RN171-cgi-get.cgi

sudo cp index.html /var/www/html/index.html
sudo cp Gforthmail.cgi /usr/lib/cgi-bin/Gforthmail.cgi
sudo cp Gforthmailget.cgi /usr/lib/cgi-bin/Gforthmailget.cgi
sudo cp RN171-cgi-get.cgi /usr/lib/cgi-bin/RN171-cgi-get.cgi
sudo touch /run/cgitest.tmp

sudo chmod 755 /usr/lib/cgi-bin/Gforthmail.cgi
sudo chmod 755 /usr/lib/cgi-bin/Gforthmailget.cgi
suod chmod 755 /usr/lib/cgi-bin/RN171-cgi-get.cgi
