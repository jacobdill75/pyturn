from model import City, Unit
import view
from controller import GameController

def handle_input(cmd, gc: GameController):
    msg = ""

    if cmd == "end":
        gc.next_turn()
    elif cmd == "assign":
        try:
            city_index = int(input("City index: "))
            project = view.get_project_choice()
            if project:
                gc.assign_production(city_index, project)
        except:
            msg = "Invalid input."
    elif cmd == "buy":
        try:
            city_index = int(input("City index: "))
            project = view.get_project_choice()
            if project:
                success = gc.buy_project(city_index, project)
                if not success:
                    msg = "Not enough gold."
        except:
            msg = "Invalid input."
    elif cmd == "found":
        name = input("New city name: ")
        if not gc.found_city(name):
            msg = "Need settler and 5 gold."
    elif cmd == "quit":
        return msg, False
    else:
        msg = "Unknown command."

    return msg, True

def main():
    gc = GameController()
    gc.player.units.append(Unit("Settler"))

    msg = ""

    while True:
        view.clear_console()
        view.show_status(gc, msg)
        print("Commands: end, assign, buy, found, quit")
        cmd = input("> ").strip().lower()
        
        msg, result = handle_input(cmd, gc)
        if not result:
            break


if __name__ == "__main__":
    main()
