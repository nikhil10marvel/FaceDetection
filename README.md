# FaceDetection
A small face detection program in python

This program uses the open cv library for python to detect faces from your WEBCAM.  
If you are on windows you don't need to install open cv or python to try out the program,  
in this case the application has been bundled into a single executable file with pyinstaller.  
Slowness at the start is completely normal as pyinstaller will unpack and load the requied libraries.

You must first unzip the downloaded zip file.  
If on windows, you can simply test the program by running the run.bat file.  
Also this application requires an extra `haarcascade_frontalface_alt.xml` file which is the cascade file for detecting faces.

The program opens up a window showing the RGBA image from your primary Webcam.  
The program will open the webcam, if it is not already.

The source code of the program can be found in the 'main' directory.
If you are not on windows, you can always try by installing opencv and python and running the source code.
The program requires an arguement, i.e, the cascade file, which should be `haarcascade_frontalface_alt.xml`.

Controls ( Once window is open ):   
    Press e : to exit ( THE WINDOW KEEPS REOPENING EVEN WHEN YOU 'X'OUT or CLOSE IT )  
    Press c : to change rendering mode ( From RGBA to GREYSCALE )  
    
The program draws a rectangle around detected faces.  
Note: OPENCV uses machine learning algorithms inorder to find and detect faces. It is not guaranteed that it will detect all faces and is 100% accurate.
