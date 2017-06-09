#!/bin/bash

echo "we will ping your network and find Live hosts"
for i in {1..254} ;do (ping 10.11.1.$i -c 1 -w 5  2>/dev/null && echo "10.11.1.$i" > Livehosts.txt ) ;done


echo "found Live hosts and created Livehosts.txt"
