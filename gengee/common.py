# -*- coding: utf-8 -*-

import json
from os import path

def getConfig():
    """ Return dictionary with config values """
    from pathlib import Path
    homedir = str(Path.home())

    dev_config = "config.json"
    user_config = homedir + "/.config/gengee/config.json"

    # local config takes precendence
    if path.isfile(dev_config):
        configpath = dev_config
    elif path.isfile(user_config):
        configpath = user_config
    else:
        print("no config found")
        exit()

    try:
        with open(configpath, "r") as f:
            config = json.loads(f.read())
            return config
    except Exception as e:
        print("error reading " + configpath + ": " + str(e))
        exit()
