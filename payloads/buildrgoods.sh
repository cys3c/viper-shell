#rgoods.exe to exe run commands below

echo "we are going to build rgoods.exe"

echo "make sure to check the username and password"

echo ""
echo ""

read -n 1 -s -p "Press any key to continue"

echo "generating rgoods.exe"

# wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile HelloWorld.py

cd payloads/
wine pyinstaller --onefile --noconsole --nowindowed rgoods.py
rm -rf build/
rm -rf dist/
sed -i 's/console=True/console=False/g' rgoods.spec
wine pyinstaller rgoods.spec
mv dist/rgoods.exe .
rm -rf build/
rm -rf dist/
cd ../