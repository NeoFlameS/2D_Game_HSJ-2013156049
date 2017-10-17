from pico2d import *
import game_framework

class Map:
    image =None
    def __init__(self):
        self.matrix = [[1,0,1,0],[1,1,1,1],[1,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,0,1],[1,1,1,0]]
        if Map.image == None :
            Map.image = [load_image('tile1.png'), load_image('tile2.png')]



    def draw(self):
        i=1
        j=1
        row = 0
        col = 0
        for j in range(1,8):
            for i in range(1,5-(j%2)):
                self.image[self.matrix[j-1][i-1]].clip_draw(0,0,150,100,(150*i)+(75*(j%2))+25,450-(35*j))

class Monster_flare:
    image = None

    LEFT_DIR, RIGHT_DIR = 0,1
    LEFT_RUN, RIGHT_RUN, STAND = 6, 5, 8

    def __init__(self):
        if Monster_flare.image == None:
            Monster_flare.image = load_image('monster.png')

        self.dir = self.LEFT_DIR
        self.MAX_HP, self.MAX_MP= 300 , 5
        self.CUR_HP, self.CUR_MP=self.MAX_HP, self.MAX_MP
        self.x,self.y = 1,1
        self.DES_X,self.DES_Y = self.x,self.y
        self.state = self.STAND
        self.frame = 0

    def draw(self):
        Monster_flare.image.clip_draw(self.frame*150, self.state*150, 150, 150, (150*self.x)+(75*(self.y%2))+25,450-(35*self.x)+70)

    def update(self):
        self.frame =(self.frame+1)%4
        if self.x != self.DES_X or self.y != self.DES_Y:
            if self.x > self.DES_X:
                self.state = self.RIGHT_RUN
                self.frame = 0
            else :
                self.state = self.LEFT_RUN
                self.frame = 0



def enter():
    global flare,running,MapTile, BackGroundImage,Bar
    running = True
    flare = Monster_flare()
    MapTile=Map()
    BackGroundImage = load_image('background.png')
    Bar = load_image('bar.png')

def exit():
    global flare
    del(flare)


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
                game_framework.pop_state()


def update():
    global flare

    flare.update()

    delay(0.1)


def draw():
    global  flare,MapTile,BackGroundImage,Bar

    clear_canvas()
    BackGroundImage.draw(400,300)
    Bar.draw(400,75)
    MapTile.draw()
    flare.draw()


    update_canvas()

def main():
    open_canvas()
    enter()

    global running

    while running:
        handle_events()
        draw()
        update()

    close_canvas()


if __name__ == '__main__':
    main()