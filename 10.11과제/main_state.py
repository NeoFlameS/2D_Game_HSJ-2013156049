from pico2d import *
import game_framework
import random
import numbers

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
 
    def draw(self):
        self.image.draw(400,30)
 
class Boy:
    image = None

    LEFT_RUN,RIGHT_RUN,LEFT_STAND,RIGHT_STAND = 0,1,2,3

    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.state = self.RIGHT_RUN
        self.run_frames, self.stand_frames =0,0


        if Boy.image == None:
            Boy.image = load_image('animation_sheet.png')

    def handle_left_run(self):
        self.x -=5
        self.run_frames += 1

        if self.x < 0:
            self.state = self.RIGHT_RUN
            self.x = 0
            self.frame = 0
        if self.run_frames == 100:
            self.state = self.LEFT_STAND
            self.stand_frames = 0
            self.frame = 0

    def handle_left_stand(self):
        self.stand_frames +=1
        if self.stand_frames == 50:
            self.state = self.LEFT_RUN
            self.run_frames = 0
            self.frame = 0

    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 800:
            self.state = self.LEFT_RUN
            self.x = 800
            self.frame = 0
        if self.run_frames == 100:
            self.state = self.RIGHT_STAND
            self.stand_frames = 0
            self.frame = 0

    def handle_right_stand(self):
        self.stand_frames += 1
        if self.stand_frames == 50:
            self.state = self.RIGHT_RUN
            self.run_frames = 0
            self.frame = 0

    handle_state = {LEFT_RUN: handle_left_run,RIGHT_RUN : handle_right_run, LEFT_STAND:handle_left_stand,RIGHT_STAND:handle_right_stand}



    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

 
    def draw(self):
        self.image.clip_draw(self.frame*100, self.state*100, 100, 100,self.x,self.y)




def enter():
    global team, grass, chr_st,running
    i=0
    team = [Boy() for i in range(1000)]
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

        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE:
                running = False
                game_framework.pop_state()

            elif event.key == SDLK_UP:
                chr_st+=1
                if chr_st>999:
                    chr_st = 0

            elif event.key == SDLK_DOWN:
                chr_st -=1
                if chr_st<0:
                    chr_st = 999

        elif event.type ==SDL_MOUSEMOTION and chr_st>=0:
            team[chr_st].x= event.x
            team[chr_st].y= 600-event.y

def update():
    global team
    
    for boy in team:
        boy.update()

    delay(0.01)

def draw():
    global chr_st
    clear_canvas()
    font = load_font('C:\Windows\Fonts\Candara.ttf',20)
    chr = "Character : " + str(chr_st + 1)
    for boy in team:
        boy.draw()
        
    grass.draw()

    font.draw(10, 500, chr, [0, 0, 0])
    numbers.draw(chr_st +1,740,540)
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