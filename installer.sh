# ------------------------------------------------------------
# Setup Environment
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

wget https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi

#navigate to the correct directory with the python.msi inside and run command
wine msiexec /i python-2.7.10.msi /L*v log.txt

#Install PyInstaller on wine

cd ~/.wine/drive_c/Python27

wine python.exe Scripts/pip.exe install pyinstaller


echo "Everything has been taken care of you can now use viper"
echo "usage $> python viper.py"
echo "usage $> python viper.py"

# wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile HelloWorld.py
# wine pyinstaller --onefile --noconsole --nowindowed ViperClient.py
# wine  wine pyinstaller ViperClient.spec
# modify ViperClient.spec
# run python ViperClient.spec and change console=True to Console=False



