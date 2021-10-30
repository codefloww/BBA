"""module that implements obvious rules of physics"""
import pygame
import math
import time


def gravity(moveable,objects):
    stand = 0
    objects = objects.copy()
    objects.remove(moveable)
    
    while stand == 0:
        support1 = (moveable.x+1,moveable.y+moveable.height)
        support2 = (moveable.x+moveable.width-1,moveable.y + moveable.height)
        print(support1)
        for object in objects:
            if object.get_rigid().collidepoint(support1) or object.get_rigid().collidepoint(support2):
                stand+=1
        if stand == 0:
            moveable.fall()
            pygame.time.delay(20)
            
