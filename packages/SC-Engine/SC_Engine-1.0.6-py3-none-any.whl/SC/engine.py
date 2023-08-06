import math

def rotate(point:[int,int], center:[int,int], angle:int)->[int,int]:
    angle = math.radians(360-angle)
    x = point[0] - center[0]
    y = point[1] - center[1]
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    new_x += center[0]
    new_y += center[1]
    return [round(new_x), round(new_y)]