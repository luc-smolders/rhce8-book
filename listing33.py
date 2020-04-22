#!/usr/bin/python
""" Dynamic Inventory Script Example """

from subprocess import Popen, PIPE
import sys

try:
    import json
except ImportError:
    import simplejson as json

RESULT = {}
RESULT['all'] = {}

PIPE = Popen(['getent', 'hosts'], stdout=PIPE, universal_newlines=True)

RESULT['all']['hosts'] = []

for line in PIPE.stdout.readlines():
    s = line.split()
    RESULT['all']['hosts'] = RESULT['all']['hosts']+s

RESULT['all']['vars'] = {}

if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(RESULT))

elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({}))

else:
    print("Requires an argument, please use --list or --host <host>")

