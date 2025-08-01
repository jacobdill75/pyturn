from model import *

class GameController:
    def __init__(self):
        self.player = Player()
        self.turn = 1

    def next_turn(self):
        for city in self.player.cities:
            city.do_turn(self.player)
        self.turn += 1

    def assign_production(self, city_index: int, project: Project):
        city = self.player.cities[city_index]
        city.current_project = project
        city.progress = 0

    def buy_project(self, city_index: int, project: Project):
        if self.player.gold >= project.cost:
            self.player.gold -= project.cost
            project.on_complete(self.player.cities[city_index], self.player)
            return True
        return False

    def found_city(self, name: str):
        if self.player.has_settler() and self.player.gold >= 5:
            self.player.remove_settler()
            self.player.gold -= 5
            self.player.cities.append(City(name))
            return True
        return False
