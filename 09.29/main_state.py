from pico2d import *
import game_framework
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
 
    def draw(self):
        self.image.draw(400,30)
 
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame=0
        self.image = load_image('run.png')
 
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x = self.x+2
 
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100,self.x,self.y)




def enter():
    global team, grass, chr_st,running
    i=0
    team = [Boy() for i in range(11)]
    grass = Grass()
    chr_st=-1
    running = True

def exit():
    global team, grass, chr_st,running
    del(team)
    del(grass)
    del(chr_st)
    del(running)

def handle_events():
    global running
    global chr_st
    global team
    
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running = False
            game_framework.pop_state()
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_0:
            chr_st=0
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_1:
            chr_st=1
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_2:
            chr_st=2
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_3:
            chr_st=3
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_4:
            chr_st=4
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_5:
            chr_st=5
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_6:
            chr_st=6
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_7:
            chr_st=7
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_8:
            chr_st=8
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_9:
            chr_st=9
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_F1:
            chr_st=10
        elif event.type ==SDL_MOUSEMOTION and chr_st>=0:
            team[chr_st].x= event.x
            team[chr_st].y= 600-event.y

def update():
    global team
    
    for boy in team:
        boy.update()

def draw():
    clear_canvas()
    
    for boy in team:
        boy.draw()
        
    grass.draw()
    update_canvas()
