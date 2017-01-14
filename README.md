# CHIP-cgi-example
Basic web page with some cgi code using Gforth as script.
Email example using sSMTP and mail command from command line.
RN171 Wifly test used in push mode to this web apache server.
Note at this time only the Gforthmail.cgi script will actually mail the email address that is received via a post message!

## Configure these examples
* Use my document [here](https://github.com/harrypower/CHIPdocs) to configure and set up the CHIP
  * Ensure you set up the Apache server and configure it for CGI as shown [here](https://github.com/harrypower/CHIPdocs/blob/master/my_chip_software.md).
  * Ensure you set up the sSMTP stuff for basic smtp mail sending and test it to ensure it works.  Can be found [here](https://github.com/harrypower/CHIPdocs/blob/master/my_chip_software.md).
  * Run the included setup.sh script to put the files in the correct place and start the ram files that are used by the cgi scripts.

## *index.html*
Basic html page allowing access to *Gforthmail.cgi* and *Gforthmailget.cgi* via form submit buttons.

## *Gforthmail.cgi*
Gforth code that will be executed as a cgi script.
This code shows how to receive the post information and will display other server information.

## *Gforthmailget.cgi*
Gforth code that will be executed as cgi script.
This code shows how to receive the get information and will display other server information.

## *setup.sh*
Bash script to remove the above files and copies the new files from repository to the correct Apache file locations for serving!
This script will also set permissions of the files copied so the cgi scripts will run correctly.  
Script needs to be set to execute with chmod -x and needs to be run as su or sudo!

## *RN171XV-sensor.md*
Documentation on set up information to make a RN171XV Wifly device send automatic sensor and GPIO information data to a web server!

## *README.md*
This document!

## *main.cpp*
This is the main.cpp code that can be used with an mbed LPC1768 device to connect to the RN171XV Wifly device for command mode programing!
This code is not use in the cgi or web page stuff on the chip at all but is here for completeness as it is referenced in the RN171XV-sensor.md document.
**Note** the mbed code does not define the uart settings at all because the default settings are used and they match the RN171XV uart needs.  

## *RN171-cgi-get.cgi*
This is a Gforth script that is to normally be executed via cgi.  setup.sh will place this file in the cgi-bin directory and make another file called
/run/cgitest.tmp for use by this script.  Basically when script is run it retrieves the get message from QUERY_STRING that is populated by apache.  
Also several other environment variables are retrieved and stored in /run/cgitest.tmp.  This information can be then looked at via another cgi script and the
RN171 Analog and GPIO data can be retrieved from the QUERY_STRING.  This works with the information in RN171XV-sensor.md document provided that the information
in that document is used to set up the RN171XV device and the device is set to point to this script!
**Note** the /run/cgitest.tmp file location is used because it is a tempfs mounted directory so it is in ram and not flash so no wearing issues!

## *last-RN171-data.cgi*
This is a Gforth script executed as cgi code.  It will return the last message received from the RN171 device that is pushing data to this server.
This script will be placed into cgi-bin directory by the setup.sh script.
