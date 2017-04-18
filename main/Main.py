import cv2
import sys


class Detector:

    def __init__(self):
        # Get specified cascade xml file
        self.faceCascade = cv2.CascadeClassifier(sys.argv[1])
        # Getting video capture object
        self.cap = cv2.VideoCapture(0)
        self.mode = None
        self.ret = False;
        self.mode_name = "color"
        # Opening the webcam, if it isn't already
        if not self.cap.isOpened():
            self.cap.open();
            print("Opened Web Cam")
        # Setting the face cascade

    def capture(self):
        running = True
        while running:
            # Getting single frame from camera
            self.ret, frame = self.cap.read()
            # Checking the return boolean
            if self.ret:
                # Getting colored with alpha version of image and grey for detection
                self.color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
                self.grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                detected_faces = self.faceCascade.detectMultiScale(self.grey, 1.3, 5)

                if self.mode_name == "color":
                    self.mode = self.color
                if self.mode_name == "grey":
                    self.mode = self.grey

                # Draw a rectangle around the faces
                for (x, y, w, h) in detected_faces:
                    cv2.rectangle(self.mode, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Displaying the image
                cv2.imshow("WebCam", self.mode)
                if cv2.waitKey(1) & 0xff == ord('e'):
                    running = False

                if cv2.waitKey(1) & 0xff == ord('c'):
                    print ("Changing image rendering mode ...")
                    if self.mode_name == "color":
                        self.mode_name = "grey"
                    elif self.mode_name == "grey":
                        self.mode_name = "color"

    def end(self):
        self.cap.release();
        cv2.destroyWindow("WebCam")
        print("Last webcam capture result " + str(int(self.ret)))
        exit(int(self.ret))

app = Detector()
app.capture()
app.end()
