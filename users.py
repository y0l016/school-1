import os
import shutil

def makedirs():
    """ 
    make necessary dirs needed for writing and reading data 
    arguments: nil
    return: user data dir full path
    """
    if os.name == "nt":
        data_dir = os.path.join(os.getenv("AppData"), "craftitgui"
                                "config")
    else:
        data_dir = os.getenv("XDG_CACHE_HOME")
        if data_dir is None:
            data_dir = os.getenv("HOME") + "/.cache/craftit"
    data_dir = os.path.join(data_dir, "users")

    if not os.path.isdir(data_dir):
        # it might be a file
        if os.path.isfile(data_dir):
           shutil.rmtree(data_dir)
        os.makedirs(data_dir)

    return data_dir

def create_world(data_dir, user, world):
    """
    create a world. this simply creates a dir data_dir/user/world.
    if it is already present, it returns False
    """
    result_path = os.path.join(data_dir, user, world)

    if os.path.isdir(result_path):
        return False

    try:
        os.makedirs(result_path)
    except FileExistsError:
        return False
    return True
