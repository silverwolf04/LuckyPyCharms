#!/usr/bin/python
# SAMPLEPYTHON.PY
# dmc - 11/12/21 - program type that passes prompts to Python scripts
# this is compatible with positional and flag-based arguments
# Note: this script is not compatible as a program type for our instance of Applications Manager as python3 must be used in path /opt/rh/rh-python38/root/usr/bin/python3
# Refer to SAMPLEPYTHON.sh instead as a program type

from os import environ
from os import path
from subprocess import run

aw_home = environ['AW_HOME']
debug_path = aw_home + "/debug/SAMPLEPYTHON"

if path.exists(debug_path):
    for k, v in environ.items():
        if k not in ['db_password', 'password2', 'login', 'login2']:
            print(k + "=" + v)

program = environ['program']
arg = "/opt/rh/rh-python38/root/usr/bin/python3 " + program + " `" + aw_home + "/exec/ONELINE $par`"
print(arg)
result = run(arg)
return_code = result.returncode

file = environ['file']

if path.exists(file):
    cmd = aw_home + "/exec/FILESIZE " + file + " " + return_code

exit(return_code)
