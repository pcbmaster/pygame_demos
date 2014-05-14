#!/usr/bin/python
import pygame, colorsys, time, random
from pygame.locals import *

def mapto(x, in_min, in_max, out_min, out_max): 
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

height = 128
width = 75
h, w = height, width

pygame.init()
scr = pygame.display.set_mode((width,height), 0, 32)
#generate our palette
palette = []
for i in range(256):
    i = mapto(i,0.0,255.0,0.0,1.0)
    r,g,b = colorsys.hls_to_rgb(i/3, min(1.0,i * 2), 1.0)
    palette.append(pygame.Color(int(r*255),int(g*255),int(b*255)))

fire = [[0]*height]*width
text = pygame.image.load("brett.png")
while True:
    for r in range(20,640):
        time.sleep(0.01)
        #for x in range(width):
           # r = random.randint(0,255)
           # fire[x][height-1] = r
        ipa = pygame.PixelArray(text)
        line = ""
        for x in range(width):
            if ipa[x][r] > -15000000:
                fire[x][height-1] = 128
                line = line + "1"
            else:
                fire[x][height-1] = 0
                line = line + "0"
        print line
        line = ""
        del ipa
        pa = pygame.PixelArray(scr)
        for y in range(1,height-2):
            for x in range(1,width-2):
                fire[x][y] = ((fire[x-1][y+1]
                              + fire[x][y+1]
                              + fire[x-1][y+1]
                              + fire[x][y+2]) * 32) / 129
                if fire[x][y] < 0:
                    fire[x][y] = 0
        for x in range(width):
            for y in range(height):
                pa[x][y] = palette[fire[x][y]]
        del pa
        pygame.display.update()
