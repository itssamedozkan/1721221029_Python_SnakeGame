import Constants
class Segment:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = Constants.KEY["UP"]
        self.color = "white"