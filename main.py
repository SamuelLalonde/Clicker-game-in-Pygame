import pygame

from button import Button
from upgrade import Upgrade
from ui import UI
from game import Game

pygame.init()
pygame.font.init()

button = Button(125, 600, 100, 50)
upgrade = Upgrade(290, 10, 50, 50)
ui = UI()
game = Game()

screen = pygame.display.set_mode((350, 675))
running = True
clock = pygame.time.Clock()
dt = 0

# game is on
while running:
    
    # look for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if any mouse button is clicked -> call button method
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                game.click()
            if upgrade.is_clicked(event.pos):
                game.buy_upgrade(upgrade)

    screen.fill("white")

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    button.draw(screen)
    upgrade.draw(screen)
    ui.draw_score(screen, game.score)
    ui.draw_cost(screen, upgrade.upgrade_cost)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
pygame.font.quit()