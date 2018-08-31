#!/usr/bin/expect

spawn minicom usb0
send \n
send \r
expect "*sername: "
send rancid\r
expect "*assword: "
send \r
expect "*>"
send enable\r
expect "*assword: "
send "\n"
expect "*#"
send "write erase\n"
send \r
expect "*#"
send reload\r
send \r
expect "*confirm*"
send \r
