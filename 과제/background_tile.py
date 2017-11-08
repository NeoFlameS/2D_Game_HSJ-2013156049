from pico2d import *
import json

class Background :

    SCROLL_SPEED_PPMS = 5
    Map_info = None
    Map_json = None



    def __init__(self):
        if Background.Map_json == None :
            Background.Map_json = open('background.json').read()
            Background.Map_info = json.loads(Background.Map_json)

        self.Map_height = Background.Map_info['height']
        self.Map_width = Background.Map_info['width']

        self.Map_Array = Background.Map_info['layers'][0]["data"]


        """for i in range(0,self.Map_height*self.Map_width):
            self.Map_Arrar.append(self.Map_info["layers"]["data"])"""

        self.tile_width = Background.Map_info['tilewidth']
        self.tile_height = Background.Map_info['tileheight']
        self.tile_image_columns = self.Map_info['tilesets'][0]['columns']


        self.tile_margin = self.Map_info['tilesets'][0]['margin']
        self.tile_spacing = self.Map_info['tilesets'][0]['spacing']

        self.Tile_image = load_image(self.Map_info['tilesets'][0]['image'])
        self.x = 16
        self.y = 600-16

        self.tile_coun = self.Map_info['tilesets'][0]['tilecount']




    def draw(self):

        X_arr,Y_arr = None,None
        tile_set_x, tile_set_y = None,None
        for i in range(0,self.Map_height*self.Map_width):

            tile_set_num = self.Map_Array[i]-1

            tile_set_x = (tile_set_num) % self.tile_image_columns
            tile_set_y = 5-((tile_set_num) // self.tile_image_columns)

            X_arr = i % self.Map_width
            Y_arr = i // self.Map_width
            self.Tile_image.clip_draw(self.tile_margin+tile_set_x*(self.tile_width+self.tile_spacing), self.tile_margin+tile_set_y*(self.tile_height+self.tile_spacing), self.tile_width, self.tile_height, self.x + (X_arr * self.tile_width),
                                      self.y - (Y_arr * self.tile_height))


    def update(self):
        if self.x + (self.Map_width*self.tile_width) < 816 :
            self.x = 800 - (self.Map_width*self.tile_width)+16
        elif self.x >16 :
            self.x = 16
        if self.y <600-16 :
            self.y = 600-16
        elif self.y - (self.Map_height*self.tile_height) > -16 :
            self.y = 600-16+((self.Map_height*self.tile_height)-600)


    def handle_event(self, event):
        if event.key == SDLK_DOWN:
            self.y += Background.SCROLL_SPEED_PPMS
        elif event.key == SDLK_UP:
            self.y -= Background.SCROLL_SPEED_PPMS
        elif event.key == SDLK_LEFT:
            self.x += Background.SCROLL_SPEED_PPMS
        elif event.key == SDLK_RIGHT:
            self.x -= Background.SCROLL_SPEED_PPMS




def handle_event():
    global running
    events = get_events()
    global Bg

    for event in events :
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                running = False
            else :
                Bg.handle_event(event)



if __name__ == '__main__':

    open_canvas()

    running = True

    global Bg
    Bg = Background()
    cur_time = get_time()
    bf_time = None


    while running :
        clear_canvas()

        bf_time = get_time() - cur_time
        cur_time = get_time()

        Bg.draw()
        Bg.update()
        handle_event()
        delay(0.01)

        update_canvas()


    close_canvas()

