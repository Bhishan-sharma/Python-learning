import random
import pyautogui as pg 
import time
import pygame

clock = pygame.time.Clock()
time.sleep(18)
for i in range(500):
    clock.tick(0.2)
    pg.write("Thankyou sir")
    pg.press("enter")