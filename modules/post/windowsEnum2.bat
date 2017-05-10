CODE
cd \
mkdir WMIC-PC-INFO
cd WMIC-PC-INFO
wmic BIOS list full /format:htable > BIOS.html
wmic CSPRODUCT list full /format:htable > SM-BIOS.html
wmic CPU list full /format:htable > CPU-INFO.html
wmic COMPUTERSYSTEM list full /format:htable > COMPUTERSYSTEM.html
wmic BOOTCONFIG list full /format:htable > BOOTCONFIG.html
wmic BASEBOARD list full /format:htable > MOBO.html
wmic DISKDRIVE list /format:htable > DISK-DRIVES.html
wmic ENVIRONMENT list /format:htable > SYSTEM-ENV.html
wmic GROUP list /format:htable > GROUPS-SID.html
wmic USERACCOUNT list /format:htable > USERS-SID-STATUS.html
wmic SYSACCOUNT list full /format:htable > SYSACCOUNT-SECURITY-LIST.html
wmic SYSDRIVER list full /format:htable > SYSDRIVER-LIST.html
wmic STARTUP list full /format:htable > BASIC-STARTUP-LIST.html
wmic SHARE list full /format:htable > SHARES.html
wmic SERVICE list full /format:htable > SERVICES.html
wmic SERVER list full /format:htable > SERVER.html
wmic NIC list full /format:htable > NETWORK-ADAPTERS.html
wmic NICCONFIG list full /format:htable > NETWORK-ADAPTERS-DETAILED-INFO.html
wmic NETLOGIN list full /format:htable > NETLOGINS-INFO.html
wmic LOGICALDISK list full /format:htable > LOGICALDISK-INFO.html