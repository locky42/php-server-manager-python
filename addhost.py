#!/usr/bin/python3

import os
import argparse
import shutil

argParser = argparse.ArgumentParser()
argParser.add_argument("--host", help="google.com")
args = argParser.parse_args()

user = os.getlogin()
userPath = os.path.expanduser('~' + user)
host = args.host
sitesConfigDir = '/etc/apache2/sites-available/''

shutil.copy(sitesConfigDir + 'example.com.conf', '../' + host + '.conf')

print(user)
print(userPath)
print(host)