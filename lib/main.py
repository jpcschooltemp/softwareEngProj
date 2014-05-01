import pygame

import player
import platform

DISPLAY = (800, 640)

def main():
   pygame.init()
   screen = pygame.display.set_mode(DISPLAY)
   clock = pygame.time.Clock()

   bg = pygame.Surface((32, 32))
   bg.convert()
   bg.fill(pygame.Color("#000000"))
   entities = pygame.sprite.Group()
   pc = player.Player()
   platforms = []

   # Temporary
   level = [
   "PPPPPPPPPPPPPPPPPPPPPPPPP",
   "P                       P",
   "P                       P",
   "P                       P",
   "P                       P",
   "P                       P",
   "P  PPPP                 P",
   "P                       P",
   "P           PP          P",
   "P                  P    P",
   "P                       P",
   "P            PPPP       P",
   "P                       P",
   "P                       P",
   "P      PPPP             P",
   "P                       P",
   "P              PPPPP    P",
   "P                       P",
   "P                       P",
   "PPPPPPPPPPPPPPPPPPPPPPPPP",]
   x = 0
   y = 0
   for row in level:
      for col in row:
         if col == "P":
            p = platform.Platform(x, y)
            platforms.append(p)
            entities.add(p)
         x += 32
      y += 32
      x = 0

   entities.add(pc)
   entities.draw(screen)

   while 1:
      if pygame.event.get(pygame.QUIT):
         return

      clock.tick(30)
      key_presses = pygame.event.get(pygame.KEYDOWN)
      key_states = pygame.key.get_pressed()

      screen.fill(pygame.Color("#000000"))

      pc.update(key_presses, key_states, platforms)
      entities.draw(screen)

      pygame.display.flip()
