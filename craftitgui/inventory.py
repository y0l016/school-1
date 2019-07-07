import json

from dataclasses import dataclass

# unsafe_hash shouldn't be a problem since all datatypes are hashable
@dataclass(unsafe_hash=True)
class Item:
    """
    """
    name:   str
    recipe: dict
    count:  int = 0

    def increase_count(self, incby):
        """
        increase count by incby
        """
        self.count += incby
        return True

    def decrease_count(self, decby):
        """
        decrease count by decby
        """
        self.count -= decby
        return True

    def get_recipe(self):
        """
        return recipe dict
        """
        return self.recipe

@dataclass
class Tool:
    durability: int
    recipe:     dict

@dataclass
class Inventory:
    items: [Item]
    tools: [] # TODO

    def is_item_craftable(self, item):
        pass

def make_all_items(item_data_file):
    """
    create a dictionary of all items from item_data_file
    item_data_file is a json file where the key is the item's
    name and the value is a dict with recipe.

    the dictionary's key is the item name and value is Item object
    """
    res = {}
    with open(item_data_file) as f:
        data = json.load(f)

    for item in data:
        res[item] = Item(item, data.get(item))

    return res
