import tkinter as tk #import tkinter API
from PIL import ImageTk, Image #import PIL to render images
from Survivor import *
from Drone import Tello
from Driver import Driver

class HomeScreen:

    def showPage(self, survivors, droneActive): #alright so this method shows the page
        
        self.photoImages = [] #this is a list of photo images that have been put into tkinter (we need to keep this for reference)

        window = tk.Tk() #make your window
        window.attributes('-fullscreen', True) #set the window to full screen
        window.configure(bg='#82a3a1')

        overviewFrame = tk.Frame( # this the part of the screen on the left. it displays the title, map, status and has a button to bring the drone home
            master = window,
            width= 800,
            height= 1500,
            
            bg = '#82a3a1'
        ) 
        overviewFrame.pack(anchor = "w", side=tk.LEFT) #anchor it to the left(west) side of the screen and to the Left in the row
        overviewFrame.pack_propagate(False)

        title = tk.Label( #This is the title of the project
            master = overviewFrame,
            text = "Tellx Disaster Response",
            font = ("Franklin Gothic Heavy", 40, "bold"),
            fg = '#011936',
            bg = '#82a3a1'
            ) 
        title.pack(pady=(50, 40), padx=(50, 10), anchor = 'w') #survivorsLabel pack your silly self up

        


        #here we are prepping and resizing the map image to be put into a label and displayed
        #Open the image
        #mapImg = Image.open("./found_photos/found_1.png")
        #get the width and height and make a new size thats half that
        # width, height = mapImg.size
        # newSize = (width//2, height//2)
        # #resize it
        # mapImg = mapImg.resize(newSize)
        # #then make it a tkinter object
        # mapImgg = ImageTk.PhotoImage("./found_photos/found_1.png")

        # # This is the map image in the overview frame.
        # mapImgg.pack(padx=(60, 10), anchor = 'w')

        #here we are prepping and resizing the map image to be put into a label and displayed
        #Open the image
        mapImg = Image.open("image.png")
        #get the width and height and make a new size thats half that
        width, height = mapImg.size
        newSize = (width//2, height//2)
        #resize it
        mapImg = mapImg.resize(newSize)
        #then make it a tkinter object
        mapImg = ImageTk.PhotoImage(mapImg)

        # This is the map image in the overview frame.
        map = tk.Label(
            master = overviewFrame, 
            image = mapImg
            )
        map.pack(padx=(60, 10), anchor = 'w')


        statusFrame = tk.Frame( #this frame will hold the full status side by side while allowing different colored text
            master = overviewFrame, #stick it inside the overview frame
            height= 150,
        )
        statusFrame.pack(pady = (20,10), padx = 55, anchor = 'w') #anchor it to the left(west) side of the screen and to the Left in the row

        status = tk.Label( #This is just here for 
            master = statusFrame,
            text = "Drone Status: ",
            font = ("franklin gothic demi", 20, "bold"),
            fg = '#011936',
            bg = '#82a3a1'
            ) 
        status.pack(side = tk.LEFT)

        statusMessage = "Active" #in the final version, this will be gotten from the piersons code

        status = tk.Label( #This is the current status of the drone
            master = statusFrame,
            text = statusMessage,
            font = ("franklin gothic demi", 20, "bold"),
            fg = '#82e45b', #make the font green
            bg = '#82a3a1'
            ) 
        status.pack(side = tk.RIGHT)


        def start():
            global nextScreen
            nextScreen = -2
            window.destroy()
        
        def end():
            global nextScreen
            nextScreen = -2
            window.destroy()

        if (not droneActive): #if the drone is not active, display the button to start it
            btnStart = tk.Button(
                master = overviewFrame, 
                text = 'Start Rescue', 
                font = ("franklin gothic demi", 15, "bold"),
                fg = '#c6dddc', #make the font light blue
                bg = '#011936', #make the background the darkest blue
                command = start) #we are going to make a temporary function called lambda which allows you to pass arguments through tkinter button commands) 
            btnStart.pack(anchor = 'w',  padx = 60)
        else: #if the drong is active, display the button to end it
            btnStop = tk.Button(
                master = overviewFrame, 
                text = 'End Rescue', 
                font = ("franklin gothic demi", 15, "bold"),
                fg = '#c6dddc', #make the font light blue
                bg = '#011936', #make the background the darkest blue
                command = end) #we are going to make a temporary function called lambda which allows you to pass arguments through tkinter button commands) 
            btnStop.pack(anchor = 'w',  padx = 60)

        btnClose = tk.Button(
            master = overviewFrame, 
            text = 'Close Window', 
            font = ("franklin gothic demi", 15, "bold"),
            fg = '#c6dddc', #make the font light blue
            bg = '#011936', #make the background the darkest blue
            command = close) #we are going to make a temporary function called lambda which allows you to pass arguments through tkinter button commands) 
        btnClose.pack(anchor = 'w',  padx = 60, pady = 10)

        #this frame will show a list of pictures where the drone thinks there is a person.
        #you should be able to scroll through this seperate from the overview frame
        #you should also be able to click each picture and go to a corresponding page
        self.survivorsFrame = tk.Frame(
            master = window,
            width= 400,
            height= 5000, # it should have room for each photo in the list
            
            bg = '#465362'
        )

        self.survivorsFrame.pack(anchor = "e", side=tk.RIGHT) #anchor it to the right(east) side of the screen and to the right in the row
        self.survivorsFrame.pack_propagate(False)

        scrollbar = tk.Scrollbar(self.survivorsFrame)
        scrollbar.pack(side = tk.RIGHT, fill='y')

        survivorsLabel = tk.Label( #this labels the side bar as possible survivors
            master = self.survivorsFrame,
            text = "Survivors Found:",
            font = ("Franklin Gothic Heavy", 20, "bold"),
            fg = '#82a3a1',
            bg = '#465362'
            ) 
        survivorsLabel.pack(pady = (68, 20), padx=30, anchor = "w") #give it some padding and align it to the right(west) side of the frame
        
        def findNextScreen(Survivor):
            global nextScreen 
            nextScreen = Survivor
            window.destroy()

        def showPicture(survivor):#the showPicture function, makes the images photoimages, then puts them in a frame and packs them
            #Open the image
            survivorImg = Image.open(survivor.getImg())
            #get the width and height and make a new size thats half that
            width, height = survivorImg.size
            newSize = (width//3, height//3)
            #resize it
            survivorImg = survivorImg.resize(newSize)
            #then make it a tkinter object
            survivorImg = ImageTk.PhotoImage(survivorImg)

            self.photoImages.append(survivorImg) #make sure you add it to the photo images array so it isn't eaten by the garbage collector

            # This is the map image in the overview frame.
            survivorButton = tk.Button(
                master = self.survivorsFrame, 
                image = survivorImg,
                command = lambda: findNextScreen(survivor) #we are going to make a temporary function called lambda which allows you to pass arguments through tkinter button commands
                )
            survivorButton.pack(pady = 20, anchor = 'center')

        #the survivor images need to be in a list so we can store info about them and it can change
        for x in survivors: #for each picture in your list
            showPicture(x) #run the show picture function

        window.mainloop() #and keep showing the window until something happens
        
        return nextScreen

