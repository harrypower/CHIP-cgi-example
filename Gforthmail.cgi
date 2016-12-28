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
  ." char recieved:" amount @ . ." <br>"
  ." what i recieved: " holder @ amount @ type ." <br>" ;

: start-page ( -- )
  s\" <!DOCTYPE html><html><title>A CHIP post reciever<\/title><body>" type ;

: close-page ( -- )
  s\" <\/body><\/html>" type ;

\ get-post-message
start-page
\ [if]  s\" an error happened during get-post-message! <br>" [then]
Show-post
close-page

bye
