import pygame

class Goal(pygame.sprite.Sprite):
   def __init__(self, x, y):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((32, 32))
      self.image.convert()
      self.image.fill(pygame.Color("#800080"))
      self.rect = pygame.Rect(x, y, 32, 32)

   def update(self):
      pass

