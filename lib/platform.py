import pygame

class Platform(pygame.sprite.Sprite):
   def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((32, 32))
      self.image.convert()
      self.image.fill(pygame.Color("#DDDDDD"))
      self.rect = pygame.Rect(x, y, 32, 32)

   def update(self):
      pass
