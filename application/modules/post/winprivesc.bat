@echo off
for /F "tokens=2" %%i in ('"sc query state= all | findstr SERVICE_NAME"') do @sc qc %%i | findstr BINARY_PATH_NAME | find /I /V "system32" >> usrsrvcs.txt
for /F "tokens=3" %%b in (usrsrvcs.txt) do @icacls %%b >> srvperms.txt
del usrsrvcs.txt