from pico2d import *
import game_framework

name = "TitleState"
image = None

def enter():
    global image
    image=load_image('title.png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    i = 1
