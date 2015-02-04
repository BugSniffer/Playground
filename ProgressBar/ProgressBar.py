#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import time


#===============================================================================
# Class ProgressBar:
#===============================================================================
#===============================================================================
# Print a progress bar:
# Input Value:
# aktVal: integer value between 0 and 100
#===============================================================================
class ProgressBar:
    wheelChar = ['|', '/', '-', '\\']

    def __init__( self, barType ):
        self.lastVal = 0
        self.barType = barType
        self.wheelPos = 0
#         print 'Type = %d' % self.barType

    def printOut( self, percent ):
        if percent < 0 or percent > 100:
            return
    
        if percent != self.lastVal:
            self.lastVal = percent
            self.wheelPos = 0
        if self.barType == 1:
            outStr = '[%s%s] %3d%% \r' % ( ( "#" * percent ), ( " " * ( 100 - percent ) ), percent )
    
        if self.barType == 2:
            if percent < 100:
                outStr = '[%s%s%s] %3d%% \r' % ( ( "#" * percent ), ProgressBar.wheelChar[self.wheelPos], ( " " * ( 100 - percent - 1 ) ), percent )
            else:
                outStr = '[%s] %3d%% \r' % ( ( "#" * percent ), percent )
            if self.wheelPos >= 3:
                self.wheelPos = 0
            else:
                self.wheelPos += 1

        sys.stdout.write( outStr )
        sys.stdout.flush()
        self.lastVal = percent


#===============================================================================
# main
#===============================================================================
def main():

    pbType = int( raw_input( 'Typ (1=normal 2=mit Zwischenschritten):' ) ) 
    sleepTime = float( raw_input( 'Wartezeit [sec.]:' ) )
    startVal = int( raw_input( 'Startwert [%]:' ) )

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
