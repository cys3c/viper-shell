#to Convert ViperClient.py to exe run commands below

echo "Generating ScsiAccess.exe"

echo ""
echo "read this first"
echo ""
echo "***Important please read before running this script. The payload will not work unless 
you change the following line.

blah blah blah"


echo "Once that line is changed then press any key to continue"
echo ""
echo ""

read -n 1 -s -p "Press any key to continue"

echo "generating ScsiAccess.exe"

# wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile HelloWorld.py

wine pyinstaller --onefile --noconsole --nowindowed ScsiAccess.py
rm -rf build/
rm -rf dist/
sed -i 's/console=True/console=False/g' ScsiAccess.spec
wine pyinstaller ScsiAccess.spec
mv dist/ScsiAccess.exe .
rm -rf build/
rm -rf dist/
cd ../