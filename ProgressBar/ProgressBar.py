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

    def __init__( self, capture = "Progress", char = u"\u2588", style = 1, min = 0, max = 100, unit = "%" ):
#===============================================================================
# Parameters:
# char  - String containig a character to be used for the progress bar
# style - The following styles can be selected by creating an object:
#         1 - simple progress bar with single percentage step:
#             [#######                    ] 37%
#         2 - same as type 1 containing an additional "wheel char" (rotating
#             dash) at the current position indicating activity between two
#             percentage steps 
#             [#######-                   ] 37%
# min   - minimum value of the possible value range
# max   - maximum value of the possible value range
# unit  - unit of the values
#===============================================================================
        self.__capture = capture
        self.__char = char
        self.__style = style
        self.__lastVal = min
        self.__wheelPos = 0
        self.__minVal = min
        self.__maxVal = max
        self.__unit = unit
        self.__scale = float( self.__maxVal - self.__minVal ) / 100.0

    def printOut( self, actVal ):
#===============================================================================
# Print the progress bar:
# actVal: integer value between 0 and 100
#===============================================================================
        if actVal < self.__minVal or actVal > self.__maxVal:
            return
    
        if actVal != self.__lastVal:
            self.__lastVal = actVal
            self.__wheelPos = 0

        percent = int( float( actVal - self.__minVal ) / self.__scale )
        if self.__style == 1:
            outStr = '%s[%s%s] %3d%s   \r' % ( self.__capture, ( self.__char * percent ), ( " " * ( 100 - percent ) ), actVal, self.__unit )
    
        if self.__style == 2:
            if actVal < self.__maxVal:
                outStr = '%s[%s%s%s] %3d%s   \r' % ( self.__capture, ( self.__char * percent ), ProgressBar.wheelChar[self.__wheelPos], ( " " * ( 100 - percent - 1 ) ), actVal, self.__unit )
            else:
                outStr = '%s[%s] %3d%s   \r' % ( self.__capture, ( self.__char * percent ), actVal, self.__unit )
            self.__wheelPos += 1
            self.__wheelPos %= len( ProgressBar.wheelChar )

        sys.stdout.write( outStr )
        sys.stdout.flush()
        self.lastVal = actVal

    def __del__( self ):
        sys.stdout.write( ' ' * 107 + '\r' )
        sys.stdout.flush()


#===============================================================================
# main
#===============================================================================
def main():

    os.system( 'clear' )
    print ( 'Test ProgressBar' )
    print ( '=' * 80 )

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

    choice = raw_input( 'Start value [%] (0=default):' )
    if len( choice ) < 1:
        choice = '0'
    startVal = int( choice )

    ii = startVal * 10
    pb = ProgressBar( char = pbChar, style = pbStyle )

    startTime = time.time()
    while ii <= 1000:
        pb.printOut( ii / 10 )
        ii = ii + 1
        time.sleep( sleepTime )
    print
    print ( '%.4f sec.' % ( time.time() - startTime ) )
    del pb


#===============================================================================

if __name__ == "__main__":
    main()
