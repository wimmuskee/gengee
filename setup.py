import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gengee",
    version = "2.0.0",
    author = "Wim Muskee",
    author_email = "wimmuskee@gmail.com",
    url = "https://github.com/wimmuskee/gengee",
    description = ("A Gentoo Github PR analysis tool."),
    license = "GPL-2",
    packages=find_packages(),
    scripts=["gengee-query", "gengee-update"],
    data_files=[("/usr/share/gengee/examples", ["config.example.json"])],
    install_requires = [
        'lxml',
        'PyGithub',
        'prettytable'
    ]
)
