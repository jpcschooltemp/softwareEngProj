import pygame

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

   entities = pygame.sprite.Group()
   pc = player.Player()

   # Temporary
   level = [
   "                         ",
   "                         ",
   "                         ",
   "                         ",
   "                         ",
   "                         ",
   "                         ",
   "           G             ",
   "           PP            ",
   "                         ",
   "                         ",
   "            PPPP         ",
   "                         ",
   "                         ",
   "      PPPP               ",
   "                         ",
   "              PPPPP      ",
   "                         ",
   "                         ",
   "PPPPPPPPPPPPPPPPPPPPPPPPP",]
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

   entities.add(pc)
   entities.draw(screen)

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
