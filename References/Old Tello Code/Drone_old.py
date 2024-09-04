# The typically state loop we want to see from this would be roam -> move -> scanArea...picture -> either found or roam again. When error or user intervention, end flight


#from djitellopy import Tello
import tello
import threading 
import socket
import Command
import time
import cv2 as cv
import cvlib as cvlib
from cvlib.object_detection import draw_bbox
#TODO: CREATE GLOABALS FOR STUFF
class Drone:
  

  def __init__(self) -> None:
    print('Setting up drone...')
    self.state = 'start'
    self.found = False
    self.analyzingPicture = False
    self.commands = ['start'] # should be 'start'. Make 'test' to use the test command, found in Command.py
    self.oldState = ''
    self.connect()
    print('Done!')
# Establishes connection with drone
  def connect(self): 
    print('Connecting...')
    def recv():
      print('Starting thread...')
      # Continuously check for messages (commands) being sent to the drone
      while True: 
        print('enter while')
        try:
          data, server = self.sock.recvfrom(1518)
          print('enter try')
          print(data.decode(encoding="utf-8"))
        except Exception as e:
          print('e is about to be printed')
          print(e)
          if(e == 'out of range'):
            print('e is out of range')
            continue
          print ('\nExit . . .\n')
          self.addCommand('end')
          break
        
             
    host = ''
    port = 9000
    locaddr = (host,port)
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.bind(locaddr)
    self.tello_address = ('192.168.10.1', 8889)
    self.tello = Tello()
    recvThread = threading.Thread(target=recv)
    recvThread.start()
    while True: # Continuously check the state of the drone. If the old state is the new state, continue checking. This ensures that a state function isn't ran 
      #  more than one time in a row. 
      if self.getState() == self.getOldState():
        continue
      if self.getState() == 'roam':
        print('its roam')
        self.roamState()
      elif self.getState() == 'found':
        print('its found')
        self.foundState()
      elif self.getState() == 'start':
        print('its start')
        self.startState()
      elif self.getState() == 'move':
        print('its move')
        self.moveState()
      elif self.getState() == 'scan':
        print('its scan')
        self.scanAreaState()
      elif self.getState() == 'end':
        print('its end')
        self.endState()
        self.sock.close()

      continue

  # Input is an array of commands in order. 
  def sendCommands(self, msgs, time_wait = 0): # Example input could be ['start']
    print('Sending commands...')
    for msg in msgs:
      print('next command: ' + msg)
      splitmsg = msg.split(' ')
      if len(splitmsg) > 1:
        commands = Command.interpret(splitmsg[0], splitmsg[1]) # msg = 'up 2', command would be equal to a queue containing 'up 2'. 
      else:
        commands = Command.interpret(msg) # msg = 'start', command would be equal to a queue containing 'command' and 'takeoff'. 
      for command in commands:
        #print('Command interpretted, attempting to send...')
        print(command)
        try:
          #tello.connect()
          #tello.streamon()

          if not command:
            return

          if 'picture' in command:
            self.takePicture()
            return

          if 'end' in command or 'quit' in command:
            self.setState('end')
            self.stateHasChanged = True
            return

          # Send data
          msg = command.encode(encoding="utf-8") 
          sent = self.sock.sendto(msg, self.tello_address)
          print('waiting ' + str(time_wait) + 'seconds...')
          time.sleep(time_wait)
          print("val of sent")
          print(sent)
        except KeyboardInterrupt:
          print ('\n . . .\n')
          self.sock.close()  
          return

  def takePicture(self):
    #self.tello.connect()
    self.tello.streamon()
    frame_read = self.tello.get_frame_read()
    time.sleep(1)

    # Write the picture to picture.png
    cv.imwrite("./found_photos/picture.png", frame_read.frame)

    # Read that picture and resize it
    img = cv.imread('./found_photos/picture.png')
    resize = cv.resize(img, (800, 600))

    bbox, label, conf = cvlib.detect_common_objects(resize)

    self.analyzingPicture == False
    if 'person' in label:
      self.setState('found')
      self.found = True
      return
  def getState(self):
    return self.state
  
  def setState(self, state):
    self.state = state

  def getOldState(self):
    return self.oldState
  
  def setOldState(self, state):
    self.oldState = state
    
  def startState(self):
    self.setOldState(self.getState())
    print('starting state function')
    self.sendCommands(self.commands) # start command is always already in commands (in init)
    self.clearCommands()
    self.setState('roam')

  def roamState(self):
    # add loop for roaming state here
    print('Roaming state function')
    self.setOldState(self.getState())
    self.setState('move')
    print("old state: " + self.getOldState())
    print("new state: " + self.getState())

  def foundState(self):
    print("found state! someone was found!")
    self.setOldState(self.getState())
    self.found = False
    # TODO grab location, send to frontend and get confirmation, then set state to roam
    self.setState('roam')

  def endState(self):
    self.setOldState(self.getState())
    self.clearCommands()
    self.addCommand('end')
    print('exit state function')

  def addCommand(self, command):
    self.commands.append(command)

  def clearCommands(self):
    self.commands.clear

  def moveState(self, direction = 'forward', distance = '50'):
    print('move state function')
    self.setOldState(self.getState())
    self.tello.forward(50)
    # time_wait = int(distance) / 10
    # action = [direction + ' ' + distance]
    # self.sendCommands(action, time_wait)
    self.setState('scan')

  def scanAreaState(self):
    print('scan area state function')
    self.setOldState(self.getState())
    for i in range(4):
      self.analyzingPicture = True
      self.sendCommands(['picture'])
      while(self.analyzingPicture == True):
        continue
      if(self.getState() == 'found'):
        break
      self.sendCommands(['clock 90'], time_wait = 2)
    self.setState('roam')
    

  # test that moving is good
  # test that rotating is good (do same thing that you did with move function)
  # Have drone move forward, then take picture, then turn, then take picture, repeat until 360 degrees or so, then move in a direction x amount of cm, then repeat until person is found in photo. 

