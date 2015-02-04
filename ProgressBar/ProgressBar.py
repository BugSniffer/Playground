#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import time


class ProgressBar:
#===============================================================================
# Class ProgressBar:
# Print a progress bar in the terminal
#===============================================================================
    wheelChar = ['|', '/', '-', '\\']

    def __init__( self, style ):
#===============================================================================
# The following styles can be selected by creating an object:
# 1 - simple progress bar with single percentage step:
#     [#######                    ] 37%
# 2 - same as type 1 containing an additional "wheel char" (rotating dash) at
#     the current position indicating activity between two percentage steps 
#     [#######-                   ] 37%
#===============================================================================
        self.lastVal = 0
        self.style = style
        self.wheelPos = 0

    def printOut( self, percent ):
#===============================================================================
# Print the progress bar:
# percent: integer value between 0 and 100
#===============================================================================
        if percent < 0 or percent > 100:
            return
    
        if percent != self.lastVal:
            self.lastVal = percent
            self.wheelPos = 0
        if self.style == 1:
            outStr = '[%s%s] %3d%% \r' % ( ( "#" * percent ), ( " " * ( 100 - percent ) ), percent )
    
        if self.style == 2:
            if percent < 100:
                outStr = '[%s%s%s] %3d%% \r' % ( ( "#" * percent ), ProgressBar.wheelChar[self.wheelPos], ( " " * ( 100 - percent - 1 ) ), percent )
            else:
                outStr = '[%s] %3d%% \r' % ( ( "#" * percent ), percent )
            self.wheelPos += 1
            self.wheelPos %= len( ProgressBar.wheelChar )

        sys.stdout.write( outStr )
        sys.stdout.flush()
        self.lastVal = percent


#===============================================================================
# main
#===============================================================================
def main():

    os.system( 'clear' )
    print ( 'Test ProgressBar' )
    print ( '=' * 80 )
    pbType = int( raw_input( 'Type (1=simple 2=with "wheel char"):' ) ) 
    sleepTime = float( raw_input( 'Sleep time [sec.]:' ) )
    startVal = int( raw_input( 'Start value [%]:' ) )

    ii = startVal * 10
    pb = ProgressBar( pbType )

    startTime = time.time()
    while ii <= 1000:
        pb.printOut( ii / 10 )
        ii = ii + 1
        time.sleep( sleepTime )
    print
    print ( time.time() - startTime )


#===============================================================================

if __name__ == "__main__":
    main()
