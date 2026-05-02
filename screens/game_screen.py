import pygame
from button import Button

class GameScreen:
    def __init__(self, game, ui):
        self.game = game
        self.ui = ui

        # buttons
        self.click_button = Button(125, 600, 100, 50, "Click")
        self.home_button = Button(10, 630, 80, 35, "Home")
        self.upgrade_button = Button(260, 630, 80, 35, "Upgrades")
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.click_button.is_clicked(event.pos):
                self.game.click()
            
            elif self.home_button.is_clicked(event.pos):
                return "home"

            elif self.upgrade_button.is_clicked(event.pos):
                return "upgrades"
            
        return "game"
    
    def draw(self, screen):
        screen.fill("white")

        # draw buttons
        self.click_button.draw(screen)
        self.home_button.draw(screen)
        self.upgrade_button.draw(screen)

        # draw UI
        self.ui.draw_score(screen, self.game.score)