# ------------------------------------------------------------
# Setup Environment
# This is the installable script to install on kali 2.0
# ------------------------------------------------------------

echo "setting permissions......"
chmod +x viper.py
chmod +x modules/handler/viperserver.py


echo "building cross compiler to compile exe files on linux for windows....."
sudo apt-get install wine winetricks
winetricks python

#cd ~/.wine/drive_c/Python26

#Note that python26 is installed, not including pip (is used to install pyinstaller). Fortunately, newer Python versions already include pip. 
#Choose the proper version from Download Python (for me, python-2.7.10.msi) and install it on wine by:

#get python 2.7.13 or which ever you choose
#https://www.python.org/downloads/
#We will fetch it for you

echo "fetching python msi 2.7.13 for cross compiling on linux for windows x86...."
wget https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi


echo "Installing python msi 2.7.13 for cross compiling on linux for windows x86...."
#navigate to the correct directory with the python.msi inside and run command

wine msiexec /i python-2.7.10.msi /L*v log.txt

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

# wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile HelloWorld.py
# wine pyinstaller --onefile --noconsole --nowindowed ViperClient.py
# wine  wine pyinstaller ViperClient.spec
# modify ViperClient.spec
# run python ViperClient.spec and change console=True to Console=False



