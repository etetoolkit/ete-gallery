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
               sorted(x for x in os.listdir('.') if is_example(x)))

    print('We will run the following scripts:')
    for script in scripts:
        print('-', script)

    for script in scripts:
        launch(script)


def is_example(fname):
    """Return True if file fname is one of the example programs."""
    return (fname.endswith('.py') and  # looks like "something.py"
            os.stat(fname).st_mode % 2 == 1 and  # and has the executable bit
            not fname == os.path.basename(__file__))  # but not ourselves


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
