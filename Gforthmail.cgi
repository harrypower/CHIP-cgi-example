#! /usr/local/bin/gforth-arm

\ warnings off
:noname ; is bootmessage
variable holder
variable amount
here holder !
500 allot
variable preemail
variable email
variable email-message
0 value fid

: get-post-message ( -- nflag )
  holder @ 100 stdin read-file swap amount ! ;

: Show-post ( -- )
  ." char recieved:" amount @ . ." <br>"
  ." what i recieved: " holder @ amount @ type ." <br>" ;

: start-page ( -- )
  s\" Content-type: text/html; charset=utf-8\n\n" type
  s\" <title>A CHIP post reciever</title>" type ;

: parse-email ( -- )
  preemail $@ s" %40" search true =
  if dup preemail $@ rot - email $! s" @" email $+! 3 /string email $+!
  else 2drop
  then ;

: sendmail ( -- )
  s\" subject: Hello from the chip\n" email-message $!
  s\" from: " email-message $+!
  email $@ email-message $+!
  s\" \n" email-message $+!
  s\" A automated message from the CHIP!\n" email-message $+!
  s\" /run/cgimail.tmp" w/o open-file swap to fid
  false = if
    email-message $@ fid write-file drop
    fid flush-file drop
    fid close-file drop
  then
;

: strip-email ( -- )
  holder @ amount @ s" Eaddress=" search true =
  if 9 /string preemail $!
  preemail $@ type s\" < this is the email address before processing!<br>" type
  parse-email
  email $@ type s\" < this is the processed email address !<br>" type
  sendmail
  else s\" No Email address provided!<br>" type
  then ;

: get-get-message ( -- )
  s" QUERY_STRING" getenv ." QUERY_STRING is :" type ." <br>"
  s" REMOTE_ADDR" getenv ." REMOTE_ADDR is :" type ." <br>"
  s" REQUEST_METHOD" getenv ." REQUEST_METHOD is :" type ." <br>"
  s" HTTP_REFERER" getenv ." HTTP_REFERER is:" type ." <br>"
  s" HTTP_HOST" getenv ." HTTP_HOST is:" type ." <br>"
  s" SERVER_SOFTWARE" getenv ." SERVER_SOFTWARE is:" type ." <br>"
  s" date" system ." <br>"
;

start-page
get-post-message dup [if] .  s" <: this error happened during get-post-message! <br>"  [then]
Show-post
strip-email
get-get-message

bye
