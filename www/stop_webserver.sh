#!/bin/bash

### Background
echo "[*] - Stopping the webserver reactor"
echo "[*] - The webserver shutting down"
echo "[*] - The reactor is stopping"
kill `cat twistd.pid`