# CHIP-cgi-example
Simple web pages with some cgi code using some ssmtp email stuff

## *index.html*
Basic html page allowing access to *Gforthmail.cgi* and *Gforthmailget.cgi* via form submit buttons

## *Gforthmail.cgi*
Gforth code that will be executed as a cgi script.
This code shows how to recieve the post information and will display other server information.

## *Gforthmailget.cgi*
Gforth code that will be executed as cgi script.
This code shows how to recieve the get information ans will display other server information.

## *setup.sh*
Bash script to remove the above files and copies the new files from repository to the correct Apache file locations for serving!
This script will also set permisions of the files copied so the cgi scripts will run correctly.  
Script needs to be set to execute with chmod -x and needs to be run as su or sudo!
