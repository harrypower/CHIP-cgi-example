#!/bin/bash

sudo rm /var/www/html/index.html
sudo rm /usr/lib/cgi-bin/Gforthmail.cgi
sudo rm /usr/lib/cgi-bin/Gforthmailget.cgi

sudo cp index.html /var/www/html/index.html
sudo cp Gforthmail.cgi /usr/lib/cgi-bin/Gforthmail.cgi
sudo cp Gforthmailget.cgi /usr/lib/cgi-bin/Gforthmailget.cgi

sudo chmod 755 /usr/lib/cgi-bin/Gforthmail.cgi
sudo chmod 755 /usr/lib/cgi-bin/Gforthmailget.cgi

