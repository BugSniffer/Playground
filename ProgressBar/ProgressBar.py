#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import time

lastVal = 0
wheelPos = 0

#===============================================================================
# Print a progress bar:
# Input Value:
# aktVal: integer value between 0 and 100
#===============================================================================
def printProgressBar1( aktVal ):

    global lastVal

    if aktVal < 0 or aktVal > 100:
        return

    if aktVal != lastVal:
        lastVal = aktVal

    outStr = '[%s%s] %3d%% \r' % ( ( "#" * aktVal ), ( " " * ( 100 - aktVal ) ), aktVal )
    sys.stdout.write( outStr )
    sys.stdout.flush()
    lastVal = aktVal

#===============================================================================
# Print a progress bar:
# Input Value:
# aktVal: integer value between 0 and 100
#===============================================================================
def printProgressBar2( aktVal ):

    wheelChar = ['|', '/', '-', '\\']

    global lastVal
    global wheelPos

    if aktVal < 0 or aktVal > 100:
        return

    if aktVal != lastVal:
        lastVal = aktVal
        wheelPos = 0

    if aktVal < 100:
        outStr = '[%s%s%s] %3d%% \r' % ( ( "#" * aktVal ), wheelChar[wheelPos], ( " " * ( 100 - aktVal - 1 ) ), aktVal )
    else:
        outStr = '[%s] %3d%% \r' % ( ( "#" * aktVal ), aktVal )
    sys.stdout.write( outStr )
    sys.stdout.flush()
    lastVal = aktVal
    if wheelPos >= 3:
        wheelPos = 0
    else:
        wheelPos = wheelPos + 1


def main():

    ii = 0
    startTime = time.time()
    while ii <= 1000:
        printProgressBar2( ii / 10 )
        ii = ii + 1
#         time.sleep( 0.2 )
    print
    print ( time.time() - startTime )



if __name__ == "__main__":
    main()
