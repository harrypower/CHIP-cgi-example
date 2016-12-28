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

: start-page ( -- )
  s\" <!DOCTYPE html><html><title>A CHIP post reciever<\/title><body>" type ;

: close-page ( -- )
  s\" <\/body><\/html>" type ;

get-web-message
start-page
Show-post
close-page

bye
