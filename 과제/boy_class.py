from pico2d import *
import random
import numbers
class Boy:
    image = None
    COUNT_NUM = 1
    LEFT_RUN,RIGHT_RUN,LEFT_STAND,RIGHT_STAND = 0,1,2,3

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.state = self.RIGHT_RUN
        self.run_frames, self.stand_frames =0,0
        self.total_frames = 0.0
        self.name = None
        self.cnum = Boy.COUNT_NUM
        Boy.COUNT_NUM += 1
        self.KEY_LEFT,self.KEY_RIGHT = False,False



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

    def handle_event(self,event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.KEY_LEFT = True
            if event.key == SDLK_RIGHT:
                self.KEY_RIGHT = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.state = Boy.LEFT_STAND
                self.KEY_LEFT =False
            elif event.key == SDLK_RIGHT:
                self.state = Boy.RIGHT_STAND
                self.KEY_RIGHT = False



    def update(self,frame_time):
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8

        if self.KEY_RIGHT == True and self.KEY_LEFT == True:
            self.state = self.RIGHT_STAND
        elif self.KEY_LEFT == True:
            self.state = self.LEFT_RUN
        elif self.KEY_RIGHT == True:
            self.state = self.RIGHT_RUN

        if self.state == self.RIGHT_RUN:
            self.x = min(800,self.x+distance)
        elif self.state == self.LEFT_RUN:
            self.x = max(0,self.x-distance)
        """self.handle_state[self.state](self)"""

 
    def draw(self):
        self.image.clip_draw(self.frame*100, self.state*100, 100, 100,self.x,self.y)
        numbers.draw(self.cnum,self.x+20,self.y-20,0.3)
