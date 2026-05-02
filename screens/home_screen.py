import pygame
from button import Button

class HomeScreen:
    def __init__(self):
        self.start_button = Button(125, 300, 100, 50, "Start")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.is_clicked:
                return "game"
        
        return "home"

    def draw(self, screen):
        screen.fill("white")
        self.start_button.draw(screen)