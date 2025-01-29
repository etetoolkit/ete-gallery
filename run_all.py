#!/usr/bin/env python3

"""
Quickly test the scripts in this directory.
"""

import sys
import os
import time
from subprocess import Popen, PIPE


def main():
    scripts = (sys.argv[1:] if len(sys.argv) > 1 else
               [x for x in os.listdir('.')
                if x.startswith('ete4_') and x.endswith('.py')])

    print('Will run the following scripts:', ' '.join(scripts))
    for script in scripts:
        launch(script)


def launch(script):
    """Launch the given script, send "return" after 2 secs, and terminate."""
    cmd = './' + script
    print('\n-->', cmd)
    p = Popen(cmd, stdin=PIPE)
    time.sleep(3)
    p.communicate(b'\n')
    p.wait()
    time.sleep(3)



if __name__ == '__main__':
    main()
