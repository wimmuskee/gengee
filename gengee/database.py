# -*- coding: utf-8 -*-

from os import path
import json

class Database:
    db = {
        "pulls": {}
    }

    def __init__(self,dbpath):
        self.dbpath = dbpath


    def read(self):
        if not path.exists(self.dbpath):
            raise FileNotFoundError("database file does not exist: " + self.dbpath)

        try:
            with open(self.dbpath, "r") as f:
                db = json.loads(f.read())
        except Exception as e:
            raise SyntaxError("error reading " + self.dbpath + ": " + str(e))

        if not "pulls" in db:
            raise ValueError("database has invalid format")

        # if no exceptions, set object
        self.db = db

    def write(self):
        """ Try to write pulls to database file """
        try:
            with open(self.dbpath, "w") as f:
                f.write(json.dumps(self.db))
                print("wrote database to " + self.dbpath)
        except Exception as e:
            print("error writing " + self.dbpath + ": " + str(e))
            exit()


    def addPull(self,PR,pull):
        self.db["pulls"][PR] = pull

    def getPulls(self):
        return list(self.db["pulls"].values())

    def getPullAttribute(self,PR,attribute):
        """ Used when copying values from cache. """
        return self.db["pulls"][PR][attribute]


    def checkCacheStatus(self,PR,updated_ts):
        if PR not in self.db["pulls"]:
            return False

        if updated_ts > self.db["pulls"][PR]["updated_ts"]:
            return False

        return True


