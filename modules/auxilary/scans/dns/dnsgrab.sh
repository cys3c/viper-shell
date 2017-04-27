#!/bin/bash
echo -e "\nThis script will allow you to look for publically available hosts"
echo "You can perform a query either by selecting a target domain or /24 network"
echo "Would you like to [domain] scan or [subnet] enumerate?"
read answer
if [ $answer = "domain" ]; then
        echo "What domain would you like to scan?:"
        echo "example 'domain.com'"
        read domain
        echo -e "\n"
        for name in $(cat /usr/share/dnsenum/dns.txt);do
        host $name.$domain | grep "has address"
        done
elif [ $answer = "subnet" ]; then
        echo "Please enter Class C Subnet which you'd like to enumerate:"
        echo -e "example 192.168.20\n"
        read subnet
        for octet in `seq 1 254`;do
        host $subnet.$octet | grep "name pointer" | cut -d" " -f1,5
        done
else
        echo -e "\nExpected 'domain' or 'subnet' as input, script exiting..."
fi
