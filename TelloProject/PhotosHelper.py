# This class is the photo helper
# It helps with keeping track and manages photo names
# Might make it so that pictures that aren't of interest are still saved, but I just don't see a reason to keep them for now
class PhotosHelper():
    def __init__(self):
        self.list = []
        self.BASE_NAME = "found_"
        self.count = 1

    def generate_name(self):
    # This just generates a name for each photo. Photos that aren't of interest will get overwritten.
        name = self.BASE_NAME + str(self.count)
        return name
    
    def add_photo(self, name):
        # When a photo of interest is taken, it will adjust count so that the picture doesn't get overwritten
        self.count += 1
        self.list.append(name)
            