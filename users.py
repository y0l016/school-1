import os
import shutil

# TODO: consider using a custom function instead of shutil

class User:
    """
    a user object
    """
    def __init__(self, name):
        """
        initialize variables and make necessary dirs
        """
        self.name = name
        if os.name == "nt":
            data_dir = os.path.join(os.getenv("AppData"),
                                    "craftitgui", "cache")
        else:
            data_dir = os.getenv("XDG_CACHE_HOME")
            if data_dir is None:
                data_dir = os.getenv("HOME") + "/.cache/craftit"

        data_dir = os.path.join(data_dir, "users")
        world_dir = os.path.join(data_dir, "worlds")

        if not os.path.isdir(data_dir):
            if os.path.isfile(data_dir): shutil.rmtree(data_dir)
            os.makedirs(data_dir)

        if not os.path.isdir(world_dir):
            os.makedirs(world_dir)

        self._data_dir  = data_dir
        self._world_dir = world_dir
        self.current_world = ""

    def create_user(self):
        """
        create user directory

        returns:
        False -> if dir is already present
        True  -> sucessfully created dir
        """
        result_path = os.path.join(self._data_dir, self.name)

        if os.path.isdir(result_path): return False

        try:
            os.makedirs(result_path)
        except FileExistsError:
            return False

        return True

    def rename_user(self, new_name):
        """
        rename user. it moves the user dir to new location
        and changes the self.name variable to the new one

        returns:
        True -> if renaming is successful
        False -> if the new user dir is already existing
        """
        old_path = os.path.join(self._data_dir, self.name)
        new_path = os.path.join(self._data_dir, new_name)

        if os.path.isdir(new_path): return False

        shutil.move(old_path, new_path)
        self.name = new_name
        return True

    def _switch_world(self, world_name):
        """
        a private function used to set self.curret_world

        returns:
        True -> if changed successfully
        False -> if world is not present
        """
        path = os.path.join(self._world_dir, world_name)
        if not os.path.isdir(path): return False
        self.current_world = world_name
        return True

    def create_world(self, world_name):
        """
        create a world and switch to it

        returns:
        False -> if the world is already present
        True -> otherwise
        """
        path = os.path.join(self._world_dir, world_name)

        if os.path.isdir(path): return False

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
        path = os.path.join(self._world_dir, world_name)

        if not os.path.isdir(path): return False
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
        old_path = os.path.join(self._world_dir, old_name)
        new_path = os.path.join(self._world_dir, new_name)

        if os.path.isdir(new_path): return False

        shutil.move(old_path, new_path)
        if self.current_world == old_name:
            self._switch_world(new_name)
        return True
