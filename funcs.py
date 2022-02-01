import math

def points_on_wheel(pos_x, pos_y, r, amount):
    result_list = []
    for i in range(0, amount):
        angle = 2*math.pi*i/amount
        x = r*math.cos(angle) + pos_x
        y = r*math.sin(angle) + pos_y
        point_i = (int(x), int(y))
        result_list.append([point_i, angle])
    return result_list


def get_reflected_point(r, point, d, screen_size):
    angle_r = point[1]*d
    x = r*math.cos(angle_r) + screen_size[0]/2
    y = r*math.sin(angle_r) + screen_size[1]/2
    point_r = (int(x), int(y))
    return point_r


#RGB hue shift; WIP
def rainbow_animation(color, mode):
    vel = 2
    if color[0] > 200:
        mode = -1
    if color[0] < 50:
        mode = 1
    #Shifts all components of a color equally - shifts through the shades of gray
    color[0] += vel*mode #shift red
    color[1] += vel*mode #shift blue
    color[2] += vel*mode #shift green
    return color, mode
