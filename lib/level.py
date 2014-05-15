import pygame

import platform
import goal

def initializeLevel(levelNumber):
   entities = pygame.sprite.Group()

   level = open('data/level' + str(levelNumber))

   x = 0
   y = 0
   for row in level:
      for col in row:
         if col == "P":
            p = platform.Platform(x, y)
            entities.add(p)
         if col == "G":
            g = goal.Goal(x, y)
            entities.add(g)
         x += 32
      y += 32
      x = 0

   return entities
