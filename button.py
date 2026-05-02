import pygame

class Button:
   
    # constructor, button has x, y, width and height
    def __init__(self, x, y, width, height, text="", img=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont('arial', 16)
        self.img = ""
    
    # draw on screen
    def draw(self, screen):
        pygame.draw.rect(screen, ("black"), self.rect)
        text_surface = self.font.render(self.text, True, "white")
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
   
    # check if clicked
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
        #increase score*upgrade_multiplyer