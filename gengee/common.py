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
        dbpath = "pulldb.json"
    elif path.isfile(user_config):
        configpath = user_config
        storedir = str(Path.home()) + "/.cache/gengee"
        dbpath = storedir + "/pulldb.json"
        # make sure we have a valid storedir to return
        if not path.isdir(storedir):
            Path(storedir).mkdir(parents=True, exist_ok=True)
    else:
        print("no config found")
        exit()

    try:
        with open(configpath, "r") as f:
            config = json.loads(f.read())
            config["dbpath"] = dbpath
            return config
    except Exception as e:
        print("error reading " + configpath + ": " + str(e))
        exit()


def getPrValue(pr,format):
    """ Returns PR number as url when format is html """
    if format == "html":
        return "<a href=\"https://github.com/gentoo/gentoo/pull/" + pr + "\" target=\"_blank\">" + pr + "</a>"
    else:
        return pr


def printTable(prettytable,format):
    """ Prints prettytable instance depending on specified format """
    if format == "html":
        # prettytable encodes html chars, therefore replacing them back
        print(prettytable.get_html_string(attributes={"border":"1", "cellpadding":"2", "cellspacing":"0"}).replace("&lt;","<").replace("&gt;",">").replace("&quot;","\""))
    else:
        print(prettytable)        

def checkCompatibleDatabase(app_version,db_version):
    """ Checks if current database version has compatible
    major and minor version."""
    if int(app_version.split(".")[0]) > int(db_version.split(".")[0]):
        return False

    if int(app_version.split(".")[1]) > int(db_version.split(".")[1]):
        return False

    return True

