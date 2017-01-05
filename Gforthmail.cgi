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
  then ;

: get-get-message ( -- )
  s" QUERY_STRING" getenv ." QUERY_STRING is :" type ." <br>"
  s" REMOTE_ADDR" getenv ." REMOTE_ADDR is :" type ." <br>"
  s" REQUEST_METHOD" getenv ." REQUEST_METHOD is :" type ." <br>"
  s" HTTP_REFERER" getenv ." HTTP_REFERER is:" type ." <br>"
  s" HTTP_HOST" getenv ." HTTP_HOST is:" type ." <br>"
  s" SERVER_SOFTWARE" getenv ." SERVER_SOFTWARE is:" type ." <br>"
;

start-page
get-post-message dup [if] .  s" <: this error happened during get-post-message! <br>"  [then]
Show-post
strip-email
get-get-message

bye
