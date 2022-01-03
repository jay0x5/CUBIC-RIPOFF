#the typewriting effect function file
import os
import time
import sys
def write(print):
    for i in print:
        time.sleep(.1)
        sys.stdout.write(i)
        sys.stdout.flush()
