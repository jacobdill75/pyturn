from dataclasses import dataclass, field
from typing import List, Optional, Union

@dataclass
class Project:
    name: str
    cost: int = 0
    def on_complete(self, city, player):
        pass

@dataclass
class Unit(Project):
    def on_complete(self, city, player):
        player.units.append(self)

@dataclass
class Building(Project):
    def on_complete(self, city, player):
        city.buildings.append(self)
        if self.name == 'Factory':
            city.production_per_turn += 3
        elif self.name == 'Market':
            city.gold_per_turn += 2

@dataclass
class City:
    name: str
    production_per_turn: int = 2
    gold_per_turn: int = 0
    current_project: Optional[Project] = None
    progress: int = 0
    buildings: List[Building] = field(default_factory=list)

    def do_turn(self, player):
        player.gold += self.gold_per_turn
        self.progress += self.production_per_turn
        if self.current_project:
            if self.progress >= self.current_project.cost:
                self.current_project.on_complete(self, player)
                self.current_project = None
                self.progress = 0

@dataclass
class Player:
    cities: List[City] = field(default_factory=list)
    units: List[Unit] = field(default_factory=list)
    gold: int = 5

    def has_settler(self):
        return any(unit.name == 'Settler' for unit in self.units)

    def remove_settler(self):
        for i, unit in enumerate(self.units):
            if unit.name == 'Settler':
                del self.units[i]
                return
