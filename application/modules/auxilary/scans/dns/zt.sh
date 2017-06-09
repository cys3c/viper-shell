#!/bin/bash
# You need to have dnsutils installed
DOMAIN="thinc.local"
dig NS $DOMAIN +short | sed -e "s/\.$//g" | while read nameserver; do echo "Testing $DOMAIN @ $nameserver"; dig AXFR $DOMAIN "@$nameserver"; done