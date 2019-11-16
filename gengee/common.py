# -*- coding: utf-8 -*-

import json
from os import path
from pathlib import Path

def getConfig():
    """ Return dictionary with config values """
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

def getDBPath():
    """ Return path of DB file """
    # using local db when local config is present
    if path.isfile("config.json"):
        return "pulldb.json"
    else:
        storedir = str(Path.home()) + "/.cache/gengee"
        if not path.isdir(storedir):
            Path(storedir).mkdir(parents=True, exist_ok=True)

        return storedir + "/pulldb.json"

def readDB():
    """ Try to read database file and return pulls dict """
    dbpath = getDBPath()
    try:
        with open(dbpath, "r") as f:
            pulls = json.loads(f.read())
        return pulls
    except Exception as e:
        print("error reading " + dbpath + ": " + str(e))
        exit()

def writeDB(pulls):
    """ Try to write pulls to database file """
    dbpath = getDBPath()
    try:
        with open(dbpath, "w") as f:
            f.write(json.dumps(pulls))
            print("wrote database to " + dbpath)
    except Exception as e:
        print("error writing " + dbpath + ": " + str(e))
        exit()
