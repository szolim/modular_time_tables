import math

def points_on_wheel(pos_x, pos_y, r, amount):
    """This function takes position and size of a circle, together with
    the amount of points we will evenly space on its circumference,
    then return a list of desired points."""
    result_list = []
    for i in range(0, amount):
        angle = 2*math.pi*i/amount
        x = r*math.cos(angle) + pos_x
        y = r*math.sin(angle) + pos_y
        point_i = (int(x), int(y))
        result_list.append([point_i, angle])
    return result_list


def get_reflected_point(r, point, d, screen_size):
    """This function takes the angle specified between starting coordinates
    of a circle's circumference and ending coordinates of an point's arc and
    multiplies the angle, thus the length of an arc by [d] argument. A desired
    point is then placed at the end of this new arc."""
    angle_r = point[1]*d #A new angle describing an arc
    #x, y coordinates of a new point, centered on a window
    x = r*math.cos(angle_r) + screen_size[0]/2
    y = r*math.sin(angle_r) + screen_size[1]/2
    point_r = (int(x), int(y))
    return point_r #Return reflected point


#RGB hue shift; WIP
def rainbow_animation(color, mode):
    vel = 2 #how fast the shift goes
    if color[0] > 200: #some clamps and when to change direction of a shift
        mode = -1
    if color[0] < 50:
        mode = 1
    #Shifts all components of a color equally - shifts through the shades of gray
    color[0] += vel*mode #shift red
    color[1] += vel*mode #shift blue
    color[2] += vel*mode #shift green
    return color, mode
