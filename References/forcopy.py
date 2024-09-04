# This shows how to connect to the Tello drone to start sending commands

import threading 
import socket
import time
from djitellopy import Tello
import cv2

def connectDrone():
    host = ''
    port = 9000
    locaddr = (host,port) 


    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    tello_address = ('192.168.10.1', 8889)

    sock.bind(locaddr)

    def recv():
        count = 0
        while True: 
            try:
                data, server = sock.recvfrom(1518)
                print(data.decode(encoding="utf-8"))
            except Exception:
                print ('\nExit . . .\n')
                break

    # recvThread create
    recvThread = threading.Thread(target=recv)
    recvThread.start()
    while True: 
        try:
            tello = Tello()
            tello.connect()
            tello.streamon()

            if not msg:
                break

            if 'end' in msg:
                print ('...')
                sock.close()  
                break

            # Send data
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_address)
        except KeyboardInterrupt:
            print ('\n . . .\n')
            sock.close()  
            break

connectDrone()