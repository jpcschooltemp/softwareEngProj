import pygame
import platform
import goal

class Player(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.xvel = 0
      self.yvel = 0
      self.on_ground = False
      self.image = pygame.Surface((32, 32))
      self.image.convert()
      self.image.fill(pygame.Color("#FF0000"))
      self.rect = pygame.Rect(32, -32, 32, 32) 

   def update(self, key_presses, key_states, entities):
      if key_states[pygame.K_UP]:
         if self.on_ground:
            self.yvel -= 14
      if key_states[pygame.K_DOWN]:
         pass
      if key_states[pygame.K_LEFT]:
         self.xvel = -10
      if key_states[pygame.K_RIGHT]:
         self.xvel = 10
      if not self.on_ground:
         self.yvel += 1
      if not (key_states[pygame.K_LEFT] or key_states[pygame.K_RIGHT]):
         self.xvel = 0
      if (self.rect.top >= 640):
         self.rect = pygame.Rect(32, -32, 32, 32)
         self.xvel = 0
         self.yvel = 0

      # Increment in x direction
      self.rect.left += self.xvel
      # Do x-axis collisions
      self.collide(self.xvel, 0, entities)
      # Increment in y direction
      self.rect.top += self.yvel
      self.on_ground = False
      # Do y-axis collisions
      self.collide(0, self.yvel, entities)

   def collide(self, xvel, yvel, entities):
      for e in entities:
         if pygame.sprite.collide_rect(self, e):
            if isinstance(e, platform.Platform):
               if xvel > 0: self.rect.right = e.rect.left
               if xvel < 0: self.rect.left = e.rect.right
               if yvel > 0:
                  self.rect.bottom = e.rect.top
                  self.on_ground = True
                  self.yvel = 0
               if yvel < 0:
                  self.rect.top = e.rect.bottom
                  self.yvel = 0
            if isinstance(e, goal.Goal):
               print "YOU WON!"
