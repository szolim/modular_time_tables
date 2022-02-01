import pygame, sys, math
from funcs import *
from pygame.locals import (
    KEYDOWN,
    K_SPACE,
    QUIT,
    K_ESCAPE,
    KEYUP,
    K_d,
    K_s
)
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
d = 2 # the ratio of reflected arc and original arc for a point
circle_res = 200 #how many points = resolution of cardioid and derived shapes
#initalizing pygame and setting up the window
pygame.init()
screen_size = SCREEN_WIDTH, SCREEN_HEIGHT
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

change_rate = 1
R = 350 #radius of a circle
current_color = pygame.color.Color(190, 190, 190, 255) 
color_shift_dir = 1
#Game loop
running = True
while running:
    clock.tick(60) #set fps to 30
    #Event loop /check for input and other activities
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                change_rate = 0
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_d:
                change_rate = 1
            if event.key == K_s:
                change_rate = 0
        if event.type == KEYUP:
            if event.key == K_SPACE:
                change_rate = 1
        if event.type == QUIT:
            running = False
    
    if change_rate == 1:
        d += 0.005

    current_color, color_shift_dir = rainbow_animation(current_color, color_shift_dir)
    #draw a background circle and clear previous frame
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, current_color, (SCREEN_WIDTH/2 - R, SCREEN_HEIGHT/2 - R, 2*R, 2*R), width=1)
    #make a list of evenly spaced points on the circle's circumference
    points = points_on_wheel(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, R, circle_res)
    for point in points: #For every point in the list, draws a line from the point to its reflected point
        reflected_point = get_reflected_point(R, point, d, screen_size)
        pygame.draw.line(screen, current_color, point[0], reflected_point)

    #Flip the screen surface - makes things visible
    pygame.display.flip()



pygame.quit()
sys.exit()