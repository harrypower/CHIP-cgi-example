#! /usr/local/bin/gforth-arm

\ warnings off
:noname ; is bootmessage
variable holder
variable amount
here holder !
500 allot

: get-post-message ( -- )
  holder @ 500 stdin read-file throw cr cr amount !
;

: Show-post ( -- )
  ." char recieved:" amount @ . cr cr
  ." what i recieved: " holder @ amount @ type cr cr
;

: header ( -- )
  ." <!DOCTYPE html><html><title>A CHIP post reciever</title><body>" ;

get-web-message
header
Show-post

bye
