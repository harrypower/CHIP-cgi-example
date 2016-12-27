#! /usr/local/bin/gforth-arm

\ warnings off
:noname ; is bootmessage
variable holder
variable amount
here holder !
500 allot

: get-display ( -- )
  holder @ 10 accept amount !

  ." char recieved:" amount @ . cr cr

  ." what i recieved: " holder @ amount @ type cr cr
;

: get-web-message ( -- )
  holder @ 500 stdin read-file throw cr cr amount !
  ." char recieved:" amount @ . cr cr
  ." what i recieved: " holder @ amount @ type cr cr
;
s\" Content-Type: text/plain;charset=us-ascii\n\n" type
s\" This is working!\n\n" type
\ get-display
get-web-message
bye
