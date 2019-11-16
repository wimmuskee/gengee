# gengee
A Gentoo Github PR analysis tool. Easily getting views on the open Gentoo pull requests that Github does not provide.

## Installation
The setup.py will take care of dependencies except Portage; assuming this is installed.

Dependencies
* Portage
* PyGithub
* prettytable
* lxml

## Config
Before use, a config file needs to be set up. You can use the included example config to create your oqn, and set, for example the "public_repo" Github personal access token.
The file can be stored in 2 locations:
* local/dev: in the cloned gengee directory
* user: <HOMEDIR>/.config/gengee/config.json

If using the local/dev setup, the database file will be saved there as well, otherwise in <HOMEDIR>/.cache/gengee/config.json .

## Usage
There are 2 commands:
* gengee-update: to create a local json database
* gengee-query: to execute different views, add -h to see all views

## todo
* see PR's that are in the package.mask
* provide optional keywords for "small" search
* setup.py
