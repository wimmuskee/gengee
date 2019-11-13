# gengee
A Gentoo Github PR analysis tool. Easily getting views on the open Gentoo pull requests that Github does not provide.

## Installation
No setup.py or ebuild yet.

Dependencies
* Portage
* PyGithub
* prettytable

## Usage
There are 2 commands.

* gengee-update: to create a local json database; you need to have a "public_repo" Github personal access token configured in config.json
* gengee-query: to execute different views, add -h to see all views

## todo
* see PR's that are in the package.mask
* assignee sort?
* provide optional keywords for "small" search
