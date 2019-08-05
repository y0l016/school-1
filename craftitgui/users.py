"""
a file with a User class.
if you want to know more about it, read the doc string
of the User class
"""

import os
import shutil

from dataclasses import dataclass

import inventory

if os.name == "nt":
    __DATA_DIR__ = os.path.join(os.getenv("AppData"),
                            "craftitgui", "cache")
else:
    __DATA_DIR__ = os.getenv("XDG_CACHE_HOME")
    if __DATA_DIR__ is None:
        __DATA_DIR__ = os.getenv("HOME") + "/.cache/craftit"

__DATA_DIR__ = os.path.join(__DATA_DIR__, "users")
__WORLD_DIR__ = os.path.join(__DATA_DIR__, "worlds")

if not os.path.isdir(__DATA_DIR__):
    if os.path.isfile(__DATA_DIR__):
        shutil.rmtree(__DATA_DIR__)
    os.makedirs(__DATA_DIR__)

if not os.path.isdir(__WORLD_DIR__):
    os.makedirs(__WORLD_DIR__)

@dataclass
class User:
    """
    a user object
    """
    name: str

    def create_user(self):
        """
        create user directory

        returns:
        False -> if dir is already present
        True  -> sucessfully created dir
        """
        result_path = os.path.join(__DATA_DIR__, self.name)

        if os.path.isdir(result_path):
            return False

        try:
            os.makedirs(result_path)
        except FileExistsError:
            return False

        return True

    def _switch_world(self, world_name):
        """
        a private function used to set self.curret_world

        returns:
        True -> if changed successfully
        False -> if world is not present
        """
        path = os.path.join(__WORLD_DIR__, world_name)
        if not os.path.isdir(path):
            return False
        self.current_world = world_name
        return True

    def create_world(self, world_name):
        """
        create a world and switch to it

        returns:
        False -> if the world is already present
        True -> otherwise
        """
        path = os.path.join(__WORLD_DIR__, world_name)

        if os.path.isdir(path):
            return False

        os.makedirs(path)
        self._switch_world(world_name)
        return True

    def remove_world(self, world_name):
        """
        remove a world. doesn't switch world. that is something
        the end user has to do

        returns:
        False -> if world_name is not present
        True -> otherwise
        """
        path = os.path.join(__WORLD_DIR__, world_name)

        if not os.path.isdir(path):
            return False
        shutil.rmtree(path)
        return True

    def rename_world(self, old_name, new_name):
        """
        move old_name world to new_name world. changes self.current_world
        to new_name if old_name is the current world

        returns:
        False -> if new_name already exists
        True -> otherwise
        """
        old_path = os.path.join(__WORLD_DIR__, old_name)
        new_path = os.path.join(__WORLD_DIR__, new_name)

        if os.path.isdir(new_path):
            return False

        shutil.move(old_path, new_path)
        if self.current_world == old_name:
            self._switch_world(new_name)
        return True

def is_user_present(user_name: str) -> bool:
    return os.path.isdir(__DATA_DIR__, user_name)
