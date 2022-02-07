import pygame, sys
from funcs import *
from random import randint
from pygame.locals import (
    KEYDOWN,
    K_SPACE,
    QUIT,
    K_ESCAPE,
    KEYUP,
    K_d,
    K_s,
    K_RIGHT,
    K_LEFT,
    K_f,
    K_l,
    K_k,
    K_RETURN
)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
d = 2 # the ratio of reflected arc and original arc for a point
circle_res = 200 #how many points = resolution of cardioid and derived shapes
#initalizing pygame and setting up the window
pygame.init()
screen_size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock() #clock needed for the framerate
font = pygame.font.SysFont(None, 24) #font used for displaying d value

change_rate = 1 #should d change its value base by inputs
vel_of_change = 1 #how fast d changes its value
R = 350 #radius of a circle


current_color = pygame.Color((128, 128, 128))
color_dir = 1   # color decreasing or increasing
color_index = 0     # index of Color array
stopper = 0     # counts milisecs

#Game loop
running = True
while running:
    clock.tick(60) #set fps to 30
    stopper += clock.get_time()
    #Event loop /check for input and other activities
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE: #Freeze the change_rate of d while you're holding a space key.
                change_rate = 0
            if event.key == K_ESCAPE: #quit the program
                running = False
            if event.key == K_d: #permanently freeze the change_rate of d
                change_rate = 1
            if event.key == K_s: #permanently unfreeze the change_rate of d
                change_rate = 0
            if event.key == K_RIGHT: #increment d by 0.1
                d += 0.1
            if event.key == K_LEFT:
                d -= 0.1             #increment d by -0.1
            if event.key == K_k:
                vel_of_change -= 0.1
            if event.key == K_l:
                vel_of_change += 0.1
            if event.key == K_RETURN:
                try:
                    d = int(input("Insert a desired d value: "))
                except:
                    print("The d value should be an integer or a floating point number")
                change_rate = 0
            if event.key == K_f:
                d = math.floor(d) #Floor the d to the closest integer
        if event.type == KEYUP: 
            if event.key == K_SPACE:
                change_rate = 1
        if event.type == QUIT: #quit the program
            running = False
    
    if change_rate == 1:
        d += 0.005*vel_of_change

        # stopper counts 1 sec then updates values
        if stopper > 1000:
            color_dir = randint(-1, 1)
            color_index = randint(0, 2)
            stopper = 0

        # updates color
        current_color = color_shift(current_color, color_dir, color_index)
   
    #draw a background circle and clear previous frame
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, current_color, (SCREEN_WIDTH/2 - R, SCREEN_HEIGHT/2 - R, 2*R, 2*R), width=1)
   
    #create some text showing current value of d
    d_value = font.render(str(round(d, 2)), True, (255, 255, 255))
    screen.blit(d_value, (20, 20))

    #make a list of evenly spaced points on the circle's circumference
    points = points_on_wheel(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, R, circle_res)
    
    for point in points: #For every point in the list, draws a line from the point to its reflected point
        reflected_point = get_reflected_point(R, point, d, screen_size)
        pygame.draw.line(screen, current_color, point[0], reflected_point)

    #Flip the screen surface - makes things visible
    pygame.display.flip()


pygame.quit()
sys.exit()