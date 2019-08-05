import os

import ui
import users
import inventory

WIN = ui.Window()
ITEMS = inventory.make_all_items(os.path.join(".", "data", "items.json"))
USER = None

def main():
    WIN.add_text("Enter your username")
    name = WIN.get_input()
    USER = users.User(name)
    if not users.is_user_present(name):
        USER.create_user()
    worlds = USER.return_worlds()

    def world():
        WIN.add_text("Do you want to (s)elect/(c)reate/(d)elete/(r)ename world?")
        chose = WIN.get_input()
        if chose.startswith('c'):
            WIN.add_text("Name your world")
            world = WIN.get_input()
            USER.create_world(world)
        elif chose.startswith('d'):
            for n, i in worlds:
                WIN.add_text(f"{n}\t{i}")
            WIN.add_text("Enter the number before the world name to delete it")
            world = WIN.get_input()
            USER.remove_world(worlds[world])
            world()
        elif chose.startswith('s'):
             for n, i in worlds:
                WIN.add_text(f"{n}\t{i}")
            WIN.add_text("Enter the number before the world name to play it")
            world = WIN.get_input()
            USER._switch_world(worlds[world])
        else:
            world()
