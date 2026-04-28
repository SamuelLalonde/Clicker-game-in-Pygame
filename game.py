import pygame

from upgrade import Upgrade

class Game:
    def __init__(self):
        self.score = 0
        self.default_click_power = 1
        self.owned_upgrades = []
    
    def get_click_power(self):
        click_power = self.default_click_power

        for upgrade in self.owned_upgrades:
            click_power *= upgrade.upgrade_multiplier

        return click_power
    
    def click(self):
        self.score += self.get_click_power()
    
    def buy_upgrade(self, upgrade):
        if self.score >= upgrade.upgrade_cost:
            self.score -= upgrade.upgrade_cost
            self.owned_upgrades.append(upgrade)
            upgrade.upgrade_cost *= 5
            upgrade.upgrade_multiplier *= 2

    def update(self, dt):
        pass