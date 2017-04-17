# FaceDetection
A small face detection program in python

This program uses the open cv library for python to detect faces from your WEBCAM.  
If you are on windows you don't need to install open cv or python to try out the program,  
in this case the application has been bundled into a single executable file with pyinstaller.  
Slowness at the start is completely normal as pyinstaller will unpack and load the requied libraries.

You must first unzip the downloaded zip file.  
If on windows, you can simply test the program by running the run.bat file.  
Also this application requires an extra haarcascade_frontalface_alt.xml file which is the cascade file for detecting faces.

The program opens up a window showing the RGBA image from your primary Webcam.
