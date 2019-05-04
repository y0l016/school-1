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
   config_path = os.path.abspath(config_path)

   if not os.path.isfile(config_path):
       print("warning: using default config", file=sys.stderr)
       return DEFAULTS

   data = json.load(config_path)

   return data

def get_color_field(config, field):
    return config.get("colors").get(field)
