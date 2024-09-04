class Survivor:
    #all survivors should have a location (longitude & latitude) and a picture
    latitude: float
    longitude: float
    time: str
    img = "" #this string will hold the location of the picture
    id: int

    def __init__(self, lat, long, img):
        self.latitude = lat
        self.longitude = long
        self.img = img

    def setId(self,id):
        self.id = id
    
    def getId(self):
        return self.id

    def getImg(self):
        return self.img
    
    def getLong(self):
        return self.longitude
    
    def getLat(self):
        return self.latitude
    
    def getTime(self):
        return self.time
