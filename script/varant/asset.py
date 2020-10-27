#!/usr/bin/python3

### this script generate a hosts file ###
### an alternative to dhcp in vagrant environment ###

import yaml

path_asset = input('insert the path to the asset yaml file: ')    # refer to asset.yml documentation
path_hosts = input('insert the path to the hosts file: ')         # the output file

asset = open(path_asset)                    # open asset
db=yaml.safe_load(asset)                    # put it in a db
asset.close()                               # and close it

hosts = open(path_hosts,'a')                # hosts file opening
for key, value in db.items():               # for cicle to populate it 
  hosts.write(value['software']['ip'] + " " + key + "     # " + str(value['hardware']['vendor']) + "\n")

hosts.close()                               # file closure


### to be added the site selection          ###
### something like: in for if site == $site ###
