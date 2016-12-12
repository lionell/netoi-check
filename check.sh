#!/usr/bin/env bash

filename=$1
problem=$2
extension="${filename##*.}"


curl \
	-X POST \
	-F 'source=@'$filename'' \
	-F 'problem='$problem'' \
	-F 'planguage='$extension'' \
	-F 'language=ukr' \
	-F 'command=test' \
	-F 'code=pmg17' \
	http://www3.olymp.vinnica.ua/cgi-bin/v_olymp/i2004/members4.py > test.html

chrome test.html
