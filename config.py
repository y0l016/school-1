"""
handle the configuration file.
default config path, CONFIG is defined here.
CONFIG in nt -> AppData/craftitgui
       in posix -> XDG_CACHE_HOME/craftitgui
                   uses ~/.config if the env var is not defined.
"""
import json
import os
import sys

DEFAULTS = {
    "colors" : {
        "input_bg" : "#ffffff",
        "input_fg" : "#000000",
        "window_bg" : "#ffffff",
        "window_fg" : "#000000"
    },
    "prompt" : ">",
    "padding" : 5
}

if os.name == "nt":
    CONFIG = os.getenv("AppData")
else:
    CONFIG = os.getenv("XDG_CONFIG_HOME")
    if not CONFIG:
        CONFIG = os.getenv("HOME") + "/.config"
CONFIG = os.path.join(CONFIG, "craftitgui")

def get_config(config_path):
    """
    parse the config located at config_path and return it.
    """
    config_path = os.path.abspath(config_path)

    if os.path.isfile(config_path):
        with open(config_path, "r") as data:
            data = json.load(data)
        DEFAULTS.update(data)
    else:
        print(f"warning: using default config", file=sys.stderr)

    return DEFAULTS

def get_color_field(config, field):
    """
    return a particular color field>
    arguments:
    config -> configuration dictionary
    field -> the color field to be returned.
    """
    return config.get("colors").get(field)
