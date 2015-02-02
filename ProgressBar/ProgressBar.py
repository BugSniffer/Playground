#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import time

#===============================================================================
# Print a progress bar:
# Input Value:
# aktVal: integer value between 0 and 100
#===============================================================================
lastVal = 0
def printProgressBar( aktVal ):

    global lastVal

    if aktVal < 0 or aktVal > 100:
        return

    if aktVal != lastVal:
        outStr = '[%s] %3d%% \r' % ( ( " " * 100 ), aktVal )
        sys.stdout.write( outStr )
        outStr = '[' + '#' * aktVal + '\r'
        sys.stdout.write( outStr )
        sys.stdout.flush()
        lastVal = aktVal



def main():

    ii = 0
    while ii < 100:
        ii = ii + 1
        time.sleep( 0.4 )
        printProgressBar( ii )
    print



if __name__ == "__main__":
    main()
