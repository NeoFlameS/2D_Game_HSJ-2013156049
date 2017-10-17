from pico2d import *
import game_framework
import Title_state
name = "StartState"
image = None
logo_time = 0.0
running = True

def enter():
    global image
    open_canvas()
    image = load_image('kpu_credit.png')

def exit():
    global image
    del(image)
    close_canvas()

def update():
    global logo_time
    
    if (logo_time > 1.0):
        if __name__ == '__main__':
            global running
            running = False
            
        logo_time = 0
        """game_framework.quit()"""
        game_framework.push_state(Title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    event = get_events()
    
def test_main():
    global running
    enter()
    
    while running:
        draw()
        update()
        clear_canvas()
def pause():
    global running
    running = False

def resume():
    global logo_time
    logo_time = 0

if __name__ == '__main__':
    running = True
    test_main()
    
