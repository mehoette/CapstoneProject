import tkinter as tk #import tkinter API
from PIL import ImageTk, Image #import PIL to render images
from Survivor import *

class SurvivorScreen:

    def showPage(self, survivor):
        window = tk.Tk() #make your window
        window.attributes('-fullscreen', True) #set the window to full screen
        window.configure(bg='#465362')

        statsFrame = tk.Frame( # this the part of the screen on the left. it displays the title, map, status and has a button to bring the drone home
            master = window,
            width= 550,
            height= 1500,
            
            bg = '#82a3a1'
        ) 
        statsFrame.pack(anchor = "e", side=tk.LEFT) #anchor it to the right(east) side of the screen and to the right in the row
        statsFrame.pack_propagate(False)

        title = tk.Label( #This is the title of the project
            master = statsFrame,
            text = "Survivor Found",
            font = ("Franklin Gothic Heavy", 40, "bold"),
            fg = '#011936',
            bg = '#82a3a1'
            ) 
        title.pack(pady=(50, 40), padx=(50, 10), anchor = 'w') #survivorsLabel pack your silly self up

        #here we are prepping and resizing the map image to be put into a label and displayed
        #Open the image
        mapImg = Image.open(survivor.getImg())
        #get the width and height and make a new size thats half that
        width, height = mapImg.size
        newSize = (width//3, height//3)
        #resize it
        mapImg = mapImg.resize(newSize)
        #then make it a tkinter object
        mapImg = ImageTk.PhotoImage(mapImg)

        # This is the map image in the overview frame.
        map = tk.Label(
            master = statsFrame, 
            image = mapImg
            )
        map.pack(padx=(60, 10), anchor = 'w')

        def twoColorText (blue, green):
            blueGreenFrame = tk.Frame( #this frame will hold the full status side by side while allowing different colored text
                master = statsFrame, #stick it inside the overview frame
                height= 150,
            )
            blueGreenFrame.pack(pady = 5, padx = 55, anchor = 'w') #anchor it to the left(west) side of the screen and to the Left in the row

            blueText = tk.Label( #This is just here for 
                master = blueGreenFrame,
                text = blue,
                font = ("franklin gothic demi", 20, "bold"),
                fg = '#011936',
                bg = '#82a3a1'
                ) 
            blueText.pack(side = tk.LEFT)

            greenText = tk.Label( #This is the current status of the drone
                master = blueGreenFrame,
                text = green,
                font = ("franklin gothic demi", 20, "bold"),
                fg = '#82e45b', #make the font green
                bg = '#82a3a1'
                ) 
            greenText.pack(side = tk.RIGHT)

        twoColorText("longitude: ", (survivor.getLong()))
        twoColorText("latitude: ", (survivor.getLat()))
        twoColorText("Time Seen: ", "02/15/2024 17:55")
        
        def falsePositive():
                    #WOW code that says hey get that off our list
                    window.destroy()

        falseBtn = tk.Button(
            master = statsFrame, 
            text = 'Mark As False Positive', 
            font = ("franklin gothic demi", 15, "bold"),
            fg = '#c6dddc', #make the font light blue
            bg = '#011936', #make the background the darkest blue
            command = falsePositive) 
        falseBtn.pack(anchor = 'w',  padx = 60, pady = 10)
        
        backBtn = tk.Button(
            master = statsFrame, 
            text = 'Return to Hub', 
            font = ("franklin gothic demi", 15, "bold"),
            fg = '#c6dddc', #make the font light blue
            bg = '#011936', #make the background the darkest blue
            command = window.destroy) 
        backBtn.pack(anchor = 'w',  padx = 60, pady = 10)

        imgFrame = tk.Frame( # this the part of the screen on the left. it displays the title, map, status and has a button to bring the drone home
            master = window,
            width= 800,
            height= 1500,
            
            bg = '#82a3a1'
        ) 
        imgFrame.pack(anchor = "w", side=tk.RIGHT) #anchor it to the left(west) side of the screen and to the Left in the row
        imgFrame.pack_propagate(False)

        #here we are prepping and resizing the map image to be put into a label and displayed
        #Open the image
        survivorImg = Image.open("./found_photos/found_1.png")
        #get the width and height and make a new size thats half that
        width, height = survivorImg.size
        newSize = (int(width*.75), int(height*.75))
        #resize it
        survivorImg = survivorImg.resize(newSize)
        #then make it a tkinter object
        survivorImg = ImageTk.PhotoImage(survivorImg)

        # This is the survivor image in the img frame.
        survivorImgLabel = tk.Label(
            master = imgFrame, 
            image = survivorImg
            )

        survivorImgLabel.pack(padx=60, pady = 90)

        window.mainloop() #and keep showing the window until something happens

