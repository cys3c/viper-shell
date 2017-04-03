#!/bin/bash

### Background

echo "[*] - Starting the teamserver reactor"
echo "[*] - The reactor is running"
echo "[*] - Start your client and connect to teamserver"
echo "[*] - To connect to the chat room type viper> telnet localhost 8123"
echo "[*] - Press space bar to get back to viper console"
cd application
twistd -y teamserver.tac
cd ..
