# -*- coding: utf-8 -*-
# functions to get data out of Portage
from os import listdir, path
import portage
from lxml import etree

def setPackages():
    """ Set valid package names """
    with open(getRepoPath() + "/profiles/categories", "r") as f:
        categories = f.readlines()

    categories = [x.strip() for x in categories]

    with open("packages.txt", "w") as f:
        for category in categories:
            for pgk in listdir(getRepoPath() + "/" + category):
                f.write(category + "/" + pgk + "\n")

def getCategories():
    """ Return current categories as list """
    with open(getRepoPath() + "/profiles/categories", "r") as f:
        categories = f.readlines()

    return [x.strip() for x in categories]


def getCurrentEbuilds(package):
    """ Return current ebuilds for provided package """
    current_ebuilds = []

    try:
        for package_file in listdir(getRepoPath() + "/" + package):
            if package_file[-7:] == ".ebuild" and package_file[-11:] != "9999.ebuild":
                current_ebuilds.append(package_file[0:-7])
    except FileNotFoundError:
        pass

    return current_ebuilds

def getPackageMask():
    """ Return currently masked packages """
    with open(getRepoPath() + "/profiles/package.mask", "r") as f:
        packagemask = f.readlines()

    packagemask = [x.strip() for x in packagemask]

    masked = []
    for line in packagemask:
        if line and not line.startswith("#"):
            masked.append(line)
    return masked

def getMaintainers(package,repopath):
    """ Return a list of listed maintainers for a package """
    if not path.isdir(repopath + "/" + package):
        return []

    if not path.isfile(repopath + "/" + package + "/metadata.xml"):
        return []

    maintainers = []
    mdxml = etree.parse(repopath + "/" + package + "/metadata.xml")
    for maintainer in mdxml.xpath("/pkgmetadata/maintainer/email"):
        maintainers.append(maintainer.text)

    return maintainers

def getRepoPath():
    """ Returns system Gentoo repository 
    source: https://github.com/gentoo/portage/blob/master/bin/portageq """
    return portage.db["/"]["vartree"].settings.repositories.treemap.get("gentoo")
