#!/bin/bash

for name in $(cat list.txt);do
	host $name.acme.local 10.11.1.221 | grep "has address" | cut -d" " -f1,4

done