class cMonster:
    damages_on_touch = True
    x = 0
    y = 0
    rot = 0
    image = None
    rect = None
    baseImage = None
    mask = None

    def __init__(self,x=0,y=0,rot=0):
	    self.x = x
	    self.y = y
	    self.rot = rot