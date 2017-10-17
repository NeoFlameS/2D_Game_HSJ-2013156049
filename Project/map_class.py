from pico2d import *

class Map:
    image =None
    def __init__(self):
        if Map.image == None :
            Map.image = [load_image('tile1.png'), load_image('tile2.png')]
