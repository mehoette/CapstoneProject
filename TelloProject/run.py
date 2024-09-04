from Drone import Tello
from Driver import Driver
# Main run for the project. When ran, it will connect to the drone
# and start sending commands. 

def main():
  tello = Tello('', 8889)
  driver = Driver(tello)
  


main()
