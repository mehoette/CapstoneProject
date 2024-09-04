import cv2 as cv
import cvlib as cvlib
import threading
from cvlib.object_detection import draw_bbox
import time
import geocoder
from SurvivorScreen import *
from Survivor import *
import HomeScreen
from PhotosHelper import PhotosHelper

class Driver(object):
    def __init__(self, tello):
        self.tello = tello
        self.reload = False
        self.reload = False
        self.photos = PhotosHelper()
        self.state = 'start'
        self.check_state()

        
    def take_picture(self):
        """
        Takes picture for analyzing then analyzes it.

        :return: None
        """
        print(self.tello.streamon())
        # Capture a picture
        tello_camera = cv.VideoCapture("udp://@0.0.0.0:11111")
        ret, frame = tello_camera.read()
        time.sleep(1)

        # Write the picture to picture.png
        photo_name = self.photos.generate_name()
        cv.imwrite("./found_photos/" + photo_name + ".png", frame)
        if self.analyze_picture(photo_name):
            self.do_found(photo_name)
            self.photos.add_photo(photo_name)

    def analyze_picture(self, photo_name):
        """
        Analyzes picture to look for people. 

        :return: Either True if person is found, False otherwise.
        """
        # Read that picture and resize it
        img = cv.imread('./found_photos/' + photo_name + ".png")
        resize = cv.resize(img, (800, 600))

        bbox, label, conf = cvlib.detect_common_objects(resize)
        output_image = draw_bbox(resize, bbox, label, conf)
        cv.imwrite("./found_photos/" + photo_name + ".png" ,output_image)

        if 'person' in label:
            print('found')
            return True
        else:
            return False
        

    def check_state(self):
        while True:
            print(self.state)
            # Checks the state and does the appropriate function
            if self.state == 'start':
                self.do_start()
            elif self.state == 'scan':
                self.do_scan()
            elif self.state == 'stop':
                self.do_stop()
            elif self.state == 'found':
                self.do_found()
            elif self.state == 'move':
                self.do_move(5)
            else:
                break
            self.time_wait(1)
    
    def do_start(self):
        print(self.tello.takeoff())
        self.time_wait(6) # Tello needs 6 seconds to wait before sending more commands
        self.state = 'move'

    def do_scan(self):
        self.survivors = []
        print('do scan')
        # Scans the area for people. Takes a picture, then rotates 90 degrees, then repeats 3 times. 
        for i in range(3):
            self.take_picture()
            print(self.tello.rotate_cw(90))
            self.time_wait(3)
        self.state = 'stop'
        self.reload = True
        # homeScreen = HomeScreen()
        # homeScreen.showPage(self.survivors, True)


    def do_stop(self):
        print(self.tello.land())
        self.state = 'end'

    def do_found(self, photo_name):
        print("doing found")
        xLoc = (self.photos.count - 1) + 0.123456
        print(xLoc)
        print("./found_photos/" + photo_name + ".png")
        survivor = Survivor(xLoc, 0.987654, "./found_photos/" + photo_name + ".png")
        self.survivors.append(survivor)
        # location = geocoder.ip('me') # This line of code gets the current location given the wifi, however we use a UDP connection through wifi to connect to the drone... so we can't use it.
        # location = ['39.9307', '-91.3763'] # QU's location. 
        
    def set_done_flag(self):
        self.done_flag = True

    def time_wait(self, time): # waits a specified amount of time without completely killing the program
        print('waiting' + str(time))
        self.done_flag = False
        timer = threading.Timer(time, self.set_done_flag)
        timer.start()
        while self.done_flag == False:
            continue
        timer.cancel()
    
    def do_move(self, distance):
        # Moves forward x feet
        if distance is None:
            distance = 1
        print(self.tello.move('forward', distance))
        self.time_wait(4)
        self.state = 'scan'