import pygame

def displayScreen(screen, timer):
   screen.fill(pygame.Color("#000000"))

   font = pygame.font.Font(None, 36)
   heading = font.render("You have won the game!", 1, (255, 255, 255))
   screen.blit(heading, (250, 250))

   time = font.render("Total time: " + str(timer) + " seconds.", 1, (255, 255, 255))
   screen.blit(time, (260, 300)) 

   pygame.display.flip()

   while 1:
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.quit()
