from HomeScreen import *
from SurvivorScreen import *
from Survivor import *

#Next shows which screen will be shown next:
#<= 0: Show that survivor from the survivor list
#-1: Show HomeScreen
#-2: update button 
#-3: Close window
global next 
next = -1
droneActive = False
test = Survivor(39.955020, -91.389550, "../found_photos/found_1.png")
test2 = Survivor(39.955020, -91.389550, "../found_photos/found_2.png")
test3 = Survivor(39.955020, -91.389550, "../found_photos/found_2.png")
survivors = [test, test2, test3]
test.setId(1)
test2.setId(2)
test2.setId(3)

test3 = Survivor(2.123456, 0.987654, "../found_photos/found_3.png")
test3.setId(survivors.count)
survivors.append(test3)


while True:
    #set up screen to show either the home screen or the survivor screen
    if next == -1:
        homeScreen = HomeScreen()
        next = homeScreen.showPage(survivors, droneActive)
        if next == -2:
            droneActive = not droneActive
            next = -1
        if next == -3: #if homeScreen returns -2 instead of the next survivor, it will not show another screen and end the program
            break
    else:
        survivorScreen = SurvivorScreen()
        survivorScreen.showPage(next)
        next = -1 #after you are done with a survivor screen, it always redirects you to the home screen



