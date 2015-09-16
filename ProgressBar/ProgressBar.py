#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import time
from TextColor import bColors


class ProgressBar:
#===============================================================================
# Class ProgressBar:
# Print a progress bar in the terminal
#===============================================================================
    wheelChar = ['|', '/', '-', '\\']

    def __init__( self, capture, char, style = 0, min = 0, max = 100, unit = '%' ):
#===============================================================================
# Parameters:
# capture - String printed in front of the progress bar
# char    - String containing a character to be used for the progress bar
# style   - The following styles can be selected by creating an object:
#           0 - simple progress bar with single percentage step:
#               [#######                    ] 37%
#           1 - same as type 0 containing an additional "wheel char" (rotating
#               dash) at the current position indicating activity between two
#               percentage steps 
#               [#######-                   ] 37%
# min     - minimum value of the possible value range
# max     - maximum value of the possible value range
# unit    - unit of the values
#===============================================================================
        if capture == None:
            self.__capture = ''
        else:
            self.__capture = capture

        self.__char = char
        if style == 0 and char == None:
            self.__char = '#'
        if style == 1 and char == None:
            self.__char = '#'
        if style == 2 and char == None:
            self.__char = ' '
#             self.__char = u'\u2588'
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
        if self.__style == 0:
            outStr = '%s[%s%s] %3d%s   \r' % ( self.__capture, ( self.__char * percent ), ( " " * ( 100 - percent ) ), actVal, self.__unit )
    
        if self.__style == 1:
            if actVal < self.__maxVal:
                outStr = '%s[%s%s%s] %3d%s   \r' % ( self.__capture, ( self.__char * percent ), ProgressBar.wheelChar[self.__wheelPos], ( " " * ( 100 - percent - 1 ) ), actVal, self.__unit )
            else:
                outStr = '%s[%s] %3d%s   \r' % ( self.__capture, ( self.__char * percent ), actVal, self.__unit )
            self.__wheelPos += 1
            self.__wheelPos %= len( ProgressBar.wheelChar )

        if self.__style == 2:
            colBar = '\033[1;42m'
            colNoBar = '\033[1;47m'
            colReset = '\033[0m'

            outStr = '%s%s%s%s%s%s%3d%s   \r' % ( self.__capture, colBar, ( self.__char * percent ), colNoBar, ( " " * ( 100 - percent ) ), colReset, actVal, self.__unit )
    
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

    choice = raw_input( 'Style (0=simple(default) 1=with "wheel char") 2=colored:' )
    if len( choice ) < 1:
        choice = '0'
    pbStyle = int( choice ) 

    str = 'Character (#=default):'
    print ( str ),
    choice = raw_input()
    if len( choice ) < 1:
        choice = '#'
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
