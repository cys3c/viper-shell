#!/bin/bash

### Background

echo "[*] - Starting the teamserver reactor"
echo "[*] - The reactor is running"
cd application
twistd -y teamserver.tac
cd ..
