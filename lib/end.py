import pygame

def displayScreen(screen):
   screen.fill(pygame.Color("#FFFFFF"))

   font = pygame.font.Font(None, 36)
   text = font.render("You have won the game!", 1, (10, 10, 10))
   screen.blit(text, (250, 250))

   pygame.display.flip()

   while 1:
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.quit()
