import os
from setuptools import setup, find_packages
import gengee

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gengee",
    version = gengee.__version__,
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
