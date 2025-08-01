import os

from controller import *

def print_cities(controller: GameController):
    if len(controller.player.cities) == 0:
        return
    print("Cities:")
    for i, city in enumerate(controller.player.cities):
        proj = city.current_project.name if city.current_project else "None"
        turns_left = (city.current_project.cost - city.progress) // city.production_per_turn if city.current_project else 0
        total_cost = city.current_project.cost if city.current_project else 0
        print(f"  [{i}] {city.name}: {proj} ({city.progress}/{total_cost}; {turns_left} turns left), Prod: {city.production_per_turn}, Gold: {city.gold_per_turn}")

def print_units(controller: GameController):
    if len(controller.player.units) == 0:
        return
    print("Units: " + ", ".join(u.name for u in controller.player.units))

def show_status(controller: GameController, msg  = ""):
    print(f"\n--- Turn {controller.turn} ---")
    print(f"Gold: {controller.player.gold}")
    print_cities(controller)
    print_units(controller)

    if len(msg) > 0: 
        print(f"\n# {msg} #\n")
    else:
        print("\n\n")

def get_project_choice() -> Optional[Project]:
    print("Choose project:")
    print("  1. Soldier (10 prod)")
    print("  2. Settler (12 prod)")
    print("  3. Factory (20 prod)")
    print("  4. Market (16 prod)")
    choice = input("> ")
    match choice:
        case "1": return Unit("Soldier", 10)
        case "2": return Unit("Settler", 12)
        case "3": return Building("Factory", 20)
        case "4": return Building("Market", 16)
    return None

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
