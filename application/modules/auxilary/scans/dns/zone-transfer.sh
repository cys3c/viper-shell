#!/bin/bash
 
domains="$1"
data="";
 
for dnsserver in $(host -t ns "$domains" | cut -d " " -f 4);
do
        # VARIABLES
        str_len=$(echo "$dnsserver" | tr -d " " | wc -c)
        str_len=$(echo "$str_len-2"| bc )
        dns_server=$(echo "$dnsserver" | cut -b "-$str_len")
        zone_data=$(dig axfr "$1" "@$dns_server")
 
        # CHECKING ZONE TRANSFER
        check=$(echo "$zone_data" | grep "Transfer failed" | wc -l)
 
        if [[ $check -ne 0 ]];
        then
                echo -e " Transfer \033[31mFAILURE\033[00m at $dns_server"
        else
                echo -e " Transfer \033[32mSUCCESS\033[00m at $dns_server"
 
                # REMEMBER LAST SUCCESSFUL
                data="$zone_data";
                server="$dns_server"
        fi
 
done
 
echo ""
echo " Use command: dig axfr $1 @$server"
 
# UNCOMMENT THIS IF YOU WANT ZONE DATA OUTPUT
# echo "$data"