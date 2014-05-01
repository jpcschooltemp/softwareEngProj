import pygame


class Player(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.xvel = 0
      self.yvel = 0
      self.on_ground = False
      self.image = pygame.Surface((32, 32))
      self.image.convert()
      self.image.fill(pygame.Color("#FF0000"))
      self.rect = pygame.Rect(32, 32, 32, 32) 

   def update(self, key_presses, key_states, platforms):
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
         self.yvel += 1.0
      if not (key_states[pygame.K_LEFT] or key_states[pygame.K_RIGHT]):
         self.xvel = 0

      # Increment in x direction
      self.rect.left += self.xvel
      # Do x-axis collisions
      self.collide(self.xvel, 0, platforms)
      # Increment in y direction
      self.rect.top += self.yvel
      self.on_ground = False
      self.collide(0, self.yvel, platforms)

   def collide(self, xvel, yvel, platforms):
      for p in platforms:
         if pygame.sprite.collide_rect(self, p):
            if xvel > 0: self.rect.right = p.rect.left
            if xvel < 0: self.rect.left = p.rect.right
            if yvel > 0:
               self.rect.bottom = p.rect.top
               self.on_ground = True
               self.yvel = 0
            if yvel < 0:
               self.rect.top = p.rect.bottom
               self.yvel = 0

