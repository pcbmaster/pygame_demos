#!/usr/bin/python
import pygame, time, math

w = 650
h = 480
tw = 256
th = 256

pygame.init()
scr = pygame.display.set_mode((w,h), 0, 32)
img = pygame.image.load("crate.jpg")
ipa = pygame.PixelArray(img)

distanceTable = [[0]*h]*w
angleTable = [[0]*h]*w
for x in range(w):
    for y in range(h):
        try:
            distanceTable[x][y] = int(32.0 * th / math.sqrt((x - w / 2.0) 
                                                            * (x - w / 2.0)
                                                            + (y - h / 2.0)
                                                            * (y - h / 2.0))) % th
            angleTable[x][y] = int(0.5 * tw * math.atan2(y - h / 2.0, x - w / 2.0)
                                   / 3.1416)
        except:
            pass
while True:
    a = time.clock()
    shiftX = int(tw * 1.0 * a)
    shiftY = int(th * 0.25 * a)
    pa = pygame.PixelArray(scr)
    for x in range(w):
        for y in range(h):
            pa[x][y] = ipa[int(distanceTable[x][y] + shiftX) % tw][int(angleTable[x][y] + shiftY) % th]
    del pa
    pygame.display.update()
