import pygame

import level
import player
import platform
import goal
import splash

DISPLAY = (800, 640)

def main():
   pygame.init()
   screen = pygame.display.set_mode(DISPLAY)
   clock = pygame.time.Clock()
   pygame.display.set_caption("Jumpy Jumpy")

   pc = player.Player()

   entities = level.initializeLevel(1)
   entities.add(pc)

   splash.Splash.init(screen)

   bg = pygame.Surface((800, 640)).convert()
   bg.fill(pygame.Color("#00FFFF"))
   sunImage = pygame.image.load("./data/sun.bmp").convert()
   bg.blit(sunImage, (410, -10))
   cloudImage = pygame.image.load("./data/cloud.bmp").convert()
   bg.blit(cloudImage, (100, 75))
   bg.blit(cloudImage, (340, 215))

   while 1:
      if pygame.event.get(pygame.QUIT):
         return

      clock.tick(30)
      key_presses = pygame.event.get(pygame.KEYDOWN)
      key_states = pygame.key.get_pressed()

      screen.blit(bg, (0, 0))

      pc.update(key_presses, key_states, entities)
      entities.draw(screen)

      pygame.display.flip()
