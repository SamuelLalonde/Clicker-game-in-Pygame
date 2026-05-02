import pygame

from game import Game
from ui import UI
from upgrade import Upgrade

from screens.home_screen import HomeScreen
from screens.game_screen import GameScreen
from screens.upgrade_screen import UpgradeScreen

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((350, 675))
clock = pygame.time.Clock()
running = True

# core objects (shared across screens)
game = Game()
ui = UI()
upgrade = Upgrade(290, 10, 50, 50)

# screens
screens = {
    "home": HomeScreen(),
    "game": GameScreen(game, ui),
    "upgrades": UpgradeScreen(game, ui, upgrade)
}

current_screen = "home"

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            # let current screen handle event + possibly switch screen
            next_screen = screens[current_screen].handle_event(event)
            if next_screen:
                current_screen = next_screen

    # draw current screen
    screens[current_screen].draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
pygame.font.quit()