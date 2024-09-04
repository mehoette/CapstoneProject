# This is a function that can be used for sending commands to the Drone in a simpler manner.
# The purpose of making this is to have simplified commands, as well as well-defined functions
# for giving commands to the drone. The drone typically takes in commands via command line input, 
# but this allows us to use these functions that return the commands that will be read by the 
# drone input buffer. This also allows for the creation of "custom" drone commands. Some 
# examples of this would be the 'start' commands, which consists of the drone starting up
# (command) and the drone taking off (takeoff). The way this is handled is that commands
# are appended to a queue depending on the commands that was entered. The function returns the
# actual code command that the drone needs to recieve in order to properly execute the command. 

import time

def interpretCommand(command, val = 0):
  val = str(val)
  x = command.lower()
  q = []
  if x == 'start': # start of drone
    q.append('command')
    q.append('takeoff')
    return q
  elif x == 'land': # lands drone
    q.append('land')
    return q
  elif x == 'sos': # Emergency shutoff
    q.append('emergency')
    return q
  elif "up" in command: # Sends drone up x cm
    q.append('up ' + val)
    return q
  elif "down" in command: # Sends drone down x cm
    q.append('down ' + val)
    return q
  elif "left" in command: # Sends drone left x cm
    q.append('left +' + val)
    return q
  elif "right" in command: # Sends drone right x cm
    q.append('right ' + val)
    return q
  elif "forward" in command: # Sends drone forward x cm
    q.append('forward ' + val)
    return q
  elif "back" in command: # Sends drone back x cm
    q.append('back ' + val)
    return q
  elif "clock" in command: # Rotate x degree clockwise (1-3600)
    q.append('cw ' + val)
    return q
  elif "counter" in command: # Rotate x degree counter clockwise (1-3600)
    q.append('ccw ' + val)
    return q
  elif "picture" in command: # Takes a picture
    q.append('picture')
    return q
  elif "wait" in command: # Waits
    print('Waiting ' + val + ' seconds')
    time.sleep(int(val))
    return q
  elif 'quit' in command or 'end' in command: # ends the program
    q.append('end')
    return q
  
# These is an example usage of a command. The stage here is that the drone has detected a person forward and to the right. 
# Ideally, these wouldn't be boolean, but instead screen coordinates that can tell the drone where in the image the person
# is detected so that it can know how much and in what direction to go towards toget a better picture.

# The print statements here act as the command being sent to the drone.
PERSON_DETECTED_FORWARD = True
PERSON_DETECTED_RIGHT = True
PERSON_DETECTED_UP = False
commandQueue = []
print(interpretCommand('start'))
print(interpretCommand('wait', 5))
print(interpretCommand('picture'))
if(PERSON_DETECTED_FORWARD):
  print(interpretCommand('forward', 50))
  print(interpretCommand('wait', 5))
  print(interpretCommand('right', 50))
  print(interpretCommand('picture'))
  
  



  