import pygame

class Button:
   
    # constructor, button has x, y, width and height
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
    # draw on screen
    def draw(self, screen):
        pygame.draw.rect(screen, ("black"), self.rect)
   
    # check if clicked
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
        #increase score*upgrade_multiplyer