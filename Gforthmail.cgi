#! /usr/local/bin/gforth-arm

\ warnings off
:noname ; is bootmessage
variable holder
variable amount
here holder !
500 allot

: get-post-message ( -- nflag )
  holder @ 100 stdin read-file swap amount ! ;

: Show-post ( -- )
  ." char recieved:" amount @ . ." <br>" cr cr
  ." what i recieved: " holder @ amount @ type ." <br>" cr cr ;

: start-page ( -- )
  s\" Content-type: text/html; charset=utf-8\n\n" type
  s\" <title>A CHIP post reciever</title>\n\n" type ;

get-post-message
start-page
[if]  s" an error happened during get-post-message! <br>" cr cr [then]
Show-post
s\" this is a test<br>\n\n" type 
\ s\" Content-Type: text/plain;charset=us-ascii\n\n" type
\ s\" this is a test\n\n" type

bye
