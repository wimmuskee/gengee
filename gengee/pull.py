# -*- coding: utf-8 -*-

class Pull:
    def __init__(self):
        self.nr = ""
        self.p = {
            "comment_count": 0,
            "commit_count": 0,
            "commits": {},
            "ebuilds": set(),
            "eclasses": set(),
            "files": [],
            "file_count": 0,
            "keywords": [],
            "labels": [],
            "maintainers": [],
            "manifest": False,
            "mergeable": False,
            "number": "",
            "packages": set(),
            "title": "",
            "updated": "",
            "updated_ts": 0,
            "user": ""
        }

    def __str__(self):
        return self.nr


    def loadGH(self,pull):
        """ Load Github PullRequest object """
        self.nr = str(pull.number)
        
        self.p["comment_count"] = pull.comments
        self.p["commit_count"] = pull.commits
        self.p["file_count"] = pull.changed_files
        self.p["mergeable"] = pull.mergeable
        self.p["number"] = self.nr
        self.p["title"] = pull.title
        self.p["updated"] = pull.updated_at.strftime("%Y-%m-%d")
        self.p["updated_ts"] = int(pull.updated_at.timestamp())
        self.p["user"] = pull.user.login

        for l in pull.labels:
            self.p["labels"].append(l.name)


    def setKeywords(self,keywords):
        """ match keywords from selected list """
        for match_kw in keywords:
            if match_kw in self.p["title"].lower():
                self.p["keywords"].append(match_kw)

    def setFileData(self,files):
        """ Use Github file objects to set appropriate attributes """
        for c in files:
            split_fn = c.filename.split("/")
            if split_fn[0] == "eclass":
                self.p["eclasses"].add(split_fn[1])
            elif "-" not in split_fn[0]:
                # don't do anything with license/profile
                pass
            else:
                self.p["packages"].add(split_fn[0] + "/" + split_fn[1])

            self.p["files"].append(c.filename)
            if c.filename[-7:] == ".ebuild":
                self.p["ebuilds"].add(split_fn[2][:-7])
            if c.filename[-9:] == "/Manifest":
                self.p["manifest"] = True


    def setCommitData(self,commits):
        """ Use Github commit objects to set appropriate attributes """
        for c in commits:
            self.p["commits"][c.sha] = { "message": c.commit.message }