#!/usr/bin/python
import math, colorsys, gc, pygame, time
from pygame.locals import *

def mapto(x, in_min, in_max, out_min, out_max): 
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min) 

height = 75
width = 75
gc.enable() 
pal = "Rainbow" 
pygame.init()
scr = pygame.display.set_mode((height,width), 0, 32)
pygame.display.set_caption('Plasma')
#let's make a nice palette 
palette = [] 
if pal == "Rainbow": 
    for h in range(256): 
        r,g,b = colorsys.hsv_to_rgb(mapto(h,0.0,255.0,0.0,1.0), 1.0, 1.0)
        palette.append(pygame.Color(int(r*255),int(g*255),int(b*255))) 
if pal == "Rasta": 
    for i in range(256): 
        r = int(128.0 + 128 * math.sin(3.1415 * i / 16.0)) 
        g = int(128.0 + 128 * math.sin(3.1415 * i / 128.0)) 
        palette.append(pygame.Color(r,g,0))
plasma = [[]] 
for x in range(width): 
    plasma.append([]) 
    for y in range(height): 
        color = int(128.0 + (128.0 * math.sin(x / 16.0)) + 128.0 + (128.0 * math.sin(y / 8.0)) + 128.0 + (128.0 * math.sin((x+y)) / 16.0) + 128.0 + (128.0 * math.sin(math.sqrt(x * x + y * y) / 8.0))) / 4 
        plasma[x].append(color) 

while True:
    mod = time.clock() * 100
    pa = pygame.PixelArray(scr)
    for x in range(width): 
        for y in range(height): 
            pa[x][y] = palette[int((plasma[x][y] + mod) % 256)]
    del pa
    pygame.display.update()
