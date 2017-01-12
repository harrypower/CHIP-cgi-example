#!/bin/bash

sudo rm /var/www/html/index.html
sudo rm /usr/lib/cgi-bin/Gforthmail.cgi
sudo rm /usr/lib/cgi-bin/Gforthmailget.cgi
sudo rm /usr/lib/cgi-bin/RN171-cgi-get.cgi
sudo rm /usr/lib/cgi-bin/last-RN171-data.cgi
sudo rm /run/cgitest.tmp
sudo rm /run/cgimail.tmp

sudo cp index.html /var/www/html/index.html
sudo cp Gforthmail.cgi /usr/lib/cgi-bin/Gforthmail.cgi
sudo cp Gforthmailget.cgi /usr/lib/cgi-bin/Gforthmailget.cgi
sudo cp RN171-cgi-get.cgi /usr/lib/cgi-bin/RN171-cgi-get.cgi
sudo cp last-RN171-data.cgi /usr/lib/cgi-bin/last-RN171-data.cgi
sudo touch /run/cgitest.tmp
sudo touch /run/cgimail.tmp

sudo chmod 755 /usr/lib/cgi-bin/Gforthmail.cgi
sudo chmod 755 /usr/lib/cgi-bin/Gforthmailget.cgi
sudo chmod 755 /usr/lib/cgi-bin/RN171-cgi-get.cgi
sudo chmod 755 /usr/lib/cgi-bin/last-RN171-data.cgi
sudo chmod 666 /run/cgitest.tmp
sudo chmod 666 /run/cgimail.tmp
