import pygame

class Upgrade:
    
    def __init__(self, x, y, height, width):
        self.rect = pygame.Rect(x, y, width, height)
        self.upgrade_multiplier = 1
        self.upgrade_cost = 100
   
    def draw(self, screen):
        pygame.draw.rect(screen, ("grey"), self.rect)
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)