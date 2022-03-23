#!/bin/bash
# SAMPLESHELL2.sh
# dmc - 11/10/21 - program type that sets up the environment to call python for a Python-based program type
# this is compatible with positional and flag-based arguments

# SysAdmin group provided a special installation of Python outside of RedHat traditional installation.
python="/opt/rh/rh-python38/root/usr/bin/python3"

arg="$python $AW_HOME/exec/SAMPLEPYTHON.py"
echo $arg
eval $arg
err=$?

exit $err
