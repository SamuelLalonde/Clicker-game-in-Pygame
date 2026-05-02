import pygame
from button import Button

class HomeScreen:
    def __init__(self):
        self.start_button = Button(125, 600, 100, 50, "Start", "assets/start_button.png")
        self.bg = pygame.image.load("assets/home_bg.png")
        self.bg = pygame.transform.scale(self.bg, (350, 675))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_clicked:
                return "game"
        
        return "home"

    def draw(self, screen):
        screen.blit(self.bg, (0,0))
        self.start_button.draw(screen)