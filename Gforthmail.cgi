#! /usr/local/bin/gforth-arm

\ warnings off
:noname ; is bootmessage
variable holder
variable amount
here holder !
500 allot
variable preemail
variable email

: get-post-message ( -- nflag )
  holder @ 100 stdin read-file swap amount ! ;

: Show-post ( -- )
  ." char recieved:" amount @ . ." <br>"
  ." what i recieved: " holder @ amount @ type ." <br>" ;

: start-page ( -- )
  s\" Content-type: text/html; charset=utf-8\n\n" type
  s\" <title>A CHIP post reciever</title>" type ;

: strip-email ( -- )
  holder @ amount @ s" Eaddress=" search true =
  if 9 /string preemail $!
  preemail $@ type s\" < this is the email address before processing!<br>" type
  else s\" No Email address provided!<br>" type
  then
;
start-page
get-post-message dup [if] .  s" <: this error happened during get-post-message! <br>"  [then]
Show-post

bye
