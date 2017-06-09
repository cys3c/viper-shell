#to Convert ViperClient.py to exe run commands below

echo "Generating ScsiAccessNewAdminaccount.exe"

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

echo "generating ScsiAccessNewAdminaccount.exe"

# wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile HelloWorld.py

wine pyinstaller --onefile --noconsole --nowindowed ScsiAccessNewAdminaccount.py
rm -rf build/
rm -rf dist/
sed -i 's/console=True/console=False/g' ScsiAccessNewAdminaccount.spec
wine pyinstaller ScsiAccessNewAdminaccount.spec
mv dist/ScsiAccessNewAdminaccount.exe .
rm -rf build/
rm -rf dist/
cd ../