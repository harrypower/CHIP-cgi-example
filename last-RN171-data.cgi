#! /usr/local/bin/gforth-arm

\ warnings off
:noname ; is bootmessage

: return-message ( -- )
  s\" Content-type: text/html; charset=utf-8\n\n" type ;

: last-message ( -- )
  s" /run/cgitest.tmp" slurp-file type ;

return-message
last-message
." End of message!" 
bye
