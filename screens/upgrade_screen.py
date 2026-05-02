import pygame
from button import Button

class UpgradeScreen:
    def __init__(self, game, ui, upgrade):
        self.game = game
        self.ui = ui
        self.upgrade = upgrade

        # buttons
        self.buy_button = Button(125, 300, 100, 50, "Buy")
        self.exit_button = Button(125, 375, 100, 50, "Back")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.buy_button.is_clicked(event.pos):
                self.game.buy_upgrade(self.upgrade)

            elif self.exit_button.is_clicked(event.pos):
                return "game"

        return "upgrades"

    def draw(self, screen):
        screen.fill("white")

        # draw buttons
        self.buy_button.draw(screen)
        self.exit_button.draw(screen)

        # draw info
        self.ui.draw_score(screen, self.game.score)
        self.ui.draw_cost(screen, self.upgrade.upgrade_cost)