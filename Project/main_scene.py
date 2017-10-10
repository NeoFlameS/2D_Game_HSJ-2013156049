from pico2d import *
import game_framework



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
        self.x,self.y = 500,500
        self.DES_X,self.DES_Y = self.x,self.y
        self.state = self.STAND
        self.frame = 0

    def draw(self):
        Monster_flare.image.clip_draw(self.frame*150,self.state*150,150,150,self.x,self.y)

    def update(self):
        self.frame += 1
        if self.x != self.DES_X or self.y != self.DES_Y:
            if self.x > self.DES_X:
                self.state = self.RIGHT_RUN
                self.frame = 0
            else :
                self.state = self.LEFT_RUN
                self.frame = 0



def enter():
    global flare
    flare = Monster_flare()

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

    delay(0.01)


def draw():
    global  flare

    clear_canvas()

    flare.update()

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