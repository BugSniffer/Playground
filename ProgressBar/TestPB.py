#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import time
from ProgressBar import ProgressBar


#===============================================================================
# main
#===============================================================================
def main():

    os.system( 'clear' )
    print ( '=' * 80 )
    print ( 'Test ProgressBar' )
    print ( '=' * 80 )
    print

    choice = raw_input( 'Style (1=simple(default) 2=with "wheel char"):' )
    if len( choice ) < 1:
        choice = '1'
    pbStyle = int( choice ) 

    str = 'Character (' + u'\u2588' + '=(default)):'
    print ( str ),
    choice = raw_input()
    if len( choice ) < 1:
        choice = u"\u2588"
    pbChar = choice 

    choice = raw_input( 'Sleep time [sec.] (0=default):' )
    if len( choice ) < 1:
        choice = '0'
    sleepTime = float( choice ) / 10.0

    choice = raw_input( 'Minimum value (0=default):' )
    if len( choice ) < 1:
        choice = '0'
    minVal = int( choice )

    choice = raw_input( 'Maximum value (100=default):' )
    if len( choice ) < 1:
        choice = '100'
    maxVal = int( choice )

    choice = raw_input( 'Unit (%=default):' )
    if len( choice ) < 1:
        choice = '%'
    unitStr = choice

    choice = raw_input( 'Start value [%] (0=default):' )
    if len( choice ) < 1:
        choice = '0'
    startVal = int( choice )

    ii = startVal * 10
    pb = ProgressBar( char = pbChar, style = pbStyle, min = minVal, max = maxVal, unit = unitStr )

    startTime = time.time()
    while ii <= maxVal * 10:
        pb.printOut( ii / 10 )
        ii = ii + 1
        time.sleep( sleepTime )
    print
    print ( '%.4f sec.' % ( time.time() - startTime ) )
    del pb


#===============================================================================

if __name__ == "__main__":
    main()
