
#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018
# This is one way to connect to the drone with Python. See basicUsage.py for commands and an easier way to connect

import cv2
import time
from djitellopy import Tello
import cvlib as cvlib
from cvlib.object_detection import draw_bbox

tello = Tello()
tello.connect()
tello.takeoff()

tello.streamoff()
tello.streamon()
frame_read = tello.get_frame_read()
tello.streamoff()
tello.land()
while True:
    img = frame_read.frame

    if img is not None:
        # height , width , layers =  img.shape
        # new_h=int(height/scale)
        # new_w=int(width/scale)
        # resize = cv2.resize(img, (new_w, new_h))
        resize = cv2.resize(img, (800, 600))
        bbox, label, conf = cvlib.detect_common_objects(resize)
        output_image = draw_bbox(resize, bbox, label, conf)

        #cv2.imshow("Object Detection", output_image)
        cv2.imwrite("test1.png",output_image)
        break
    #recvThread create
    # recvThread = threading.Thread(target=recv)
    # # recvThread.start()
    # while True: 
    #     try:
    #         #print('taking picture')
    #         #msg = takePicture()
    #         print('picture start')
    #         tello = Tello()
    #         tello.connect()
    #         tello.streamon()
    #         #takePicture()
    #         while True:
    #             frame_read = tello.get_frame_read()
    #             time.sleep(1)
    #             cv2.imwrite("picture.png", frame_read.frame)
    #             print('---------taking picture---------')
    #             results = VideoOutput.videoOutput("picture.png")
    #             print(results)
    #             time.sleep(1)

            # if not msg:
            #     break  

            # if 'end' in msg:
            #     print ('...')
            #     sock.close()  
            #     break
            # if 'picture' in msg:
            #     takePicture()
            #     continue

            # Send data
            # msg = msg.encode(encoding="utf-8") 
            # sent = sock.sendto(msg, tello_address)
        # except KeyboardInterrupt:
        #     print ('\n . . .\n')
        #     sock.close()  
        #     break
# print ('\r\n\r\nTello Python3 Demo.\r\n')

# print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

# print ('end -- quit demo.\r\n')

def takePicture():
    import VideoOutput
    import time
    from djitellopy import Tello
    import cv2

    telloVideo = cv2.VideoCapture("udp://@192.168.10.1:8889")
    time.sleep(1)

    ret = False

    scale = 3

    while(True):
        time.sleep(1)
        # Capture frame-by-framestreamon
        ret, frame = telloVideo.read()
        if(ret):
        # Our operations on the frame come here
            height , width , layers =  frame.shape
            new_h=int(height/scale)
            new_w=int(width/scale)
            resize = cv2.resize(frame, (new_w, new_h)) # <- resize for improved performance
            # Display the resulting frame
            cv2.imshow('Tello',resize)
            
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("test.jpg",resize) # writes image test.bmp to disk
            print("Take Picture")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    telloVideo.release()
    cv2.destroyAllWindows()





    
    





    




