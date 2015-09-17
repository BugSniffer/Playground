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

    def __init__( self, capture, char, style = 0, colorF = '\033[7;49m', colorB = '\033[1;30m', min = 0, max = 100, unit = '%' ):
#===============================================================================
# Parameters:
# capture - String printed in front of the progress bar
# char    - String containing a character to be used for the progress bar
#           '#' is the default for style 0 and 1
#           ' ' is the default for style 2 (will be displayed inverse)
# style   - The following styles can be selected by creating an object:
#           0 - simple progress bar with single percentage step:
#               [#######                    ] 37%
#           1 - same as type 0 containing an additional "wheel char" (rotating
#               dash) at the current position indicating activity between two
#               percentage steps 
#               [#######-                   ] 37%
#           2 - solid progress bar without [...] at the beginning and end of the
#               bar
# colorF  - string containing escape sequence to switch to specific foreground 
# colorB    and background color of the progress bar if style 2 is selected.
#           Default values are:
#           colorF = '\033[7;49m' (inverse standard terminal color)
#           colorB = '\033[1;30m' (grey)
# min     - minimum/maximum value of the possible value range
# max       Default values are:
#           min = 0
#           max = 100
# unit    - string containing the unit of the values. Default string is '%'
#===============================================================================
        if capture == None:
            self.__capture = ''
        else:
            self.__capture = capture

        self.__char = char
        if style <= 1 and char == None:
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

        if self.__style == 2:
            self.__colorF = colorF  # set foreground color
            self.__colorB = colorB  # set background color
            self.__colorRst = '\033[0m'  # reset colors to default



    def printOut( self, actVal ):
#===============================================================================
# Print the progress bar:
# actVal: integer value in the given range between min and max
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
            outStr = '%s%s%s%s%s%s%3d%s   \r' % ( self.__capture, self.__colorF, ( self.__char * percent ), self.__colorB, ( " " * ( 100 - percent ) ), self.__colorRst, actVal, self.__unit )
    
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
