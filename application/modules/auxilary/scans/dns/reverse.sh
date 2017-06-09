#!/bin/bash

#loop in seq from ip 220 to 230
for ip in $(seq 229);do
	host 10.11.1.$ip | grep "local" | cut -d" " -f1,5

done