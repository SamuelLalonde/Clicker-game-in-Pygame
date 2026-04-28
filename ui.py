import pygame

from upgrade import Upgrade

class UI:
    def __init__(self):
        self.font = pygame.font.SysFont('arial', 15)

    def draw_score(self, screen, score):
        score_text = self.font.render(f"Bank: ${score:.2f}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
    
    def draw_cost(self, screen, cost):
        cost_text = self.font.render(f"Upgrade: ${cost:.2f}", True, (0, 0, 0))
        screen.blit(cost_text, (10, 40))