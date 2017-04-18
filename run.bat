@echo off
echo This is a face detection program, written in python
echo Using opencv
echo The xml file provided with this application is vital for its face detection
echo Do not commit changes to it unless sure
echo On startup you might not see any response from the program, but wait for a little while and it should start
echo Starting program
start Main.exe haarcascade_frontalface_alt.xml
echo Program has Started !
echo To close the program press 'e' on the keyboard
echo To change rendering mode press 'c'
pause
@echo on
exit