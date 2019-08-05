import json

from dataclasses import dataclass
from typing import List

# unsafe_hash shouldn't be a problem since all datatypes are hashable
@dataclass(unsafe_hash=True)
class Item:
    """
    an object representing an item.
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
class Inventory:
    items: List[Item]

    def __is_item_present__(self, item: str) -> bool:
        """
        check if item is in the inventory
        """
        for i in self.items:
            if item.name == i:
                return True
        return False

    def __get_item_index__(self, item: str) -> int:
        """
        get the index number of item in self.items
        """
        for n, i in enumerate(self.items):
            if i.name == item:
                return n
        return -1

    def __item_count__(self, item: str) -> int:
        """
        get the item count of item in self.items
        """
        if not self.__is_item_present__(item):
            return -1
        index = self.__get_item_index__(item)
        return items[index].count

    def __is_item_craftable__(self, item_recipe: dict) -> bool:
        """
        check if item is craftable.
        arguments:
        item_recipe -> recipe of the item
        returns:
        True -> if the item is craftable
        False -> otherwise
        """
        for item_needed in item_recipe:
            if not (self.__is__item_craftable__(self, item_needed) and \
               self.__item_count__(item_needed) >= item_recipe.get(item_needed)):
                return False
        return True

    def craft(self, item: Item) -> bool:
        """
        craft an item.
        argument:
        item - an Item object. assumes the Item object's count is zero
        returns:
        True  -> if the item is crafted
        False -> if the item cannot be crafted
        """
        recipe = item.get_recipe()
        if not __is_item_craftable__(recipe):
            return False

        # reduce item count
        for k, v in recipe.items():
            # safe because the item *will* be in the inventory
            self.items[self.__get_item_index__(k)].decrease_count(v)

        if not self.__is_item__present(item.name):
            self.items.append(item)

        self.items[self.__get_item_index_(item.name)].increase_count(1)

def make_all_items(item_data_file: str) -> dict:
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
