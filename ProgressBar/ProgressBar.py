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

    def __init__( self, char = u"\u2588", style = 1 ):
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
#===============================================================================
        self.__char = char
        self.__style = style
        self.__lastVal = 0
        self.__wheelPos = 0

    def printOut( self, percent ):
#===============================================================================
# Print the progress bar:
# percent: integer value between 0 and 100
#===============================================================================
        if percent < 0 or percent > 100:
            return
    
        if percent != self.__lastVal:
            self.__lastVal = percent
            self.__wheelPos = 0
        if self.__style == 1:
            outStr = '[%s%s] %3d%%\r' % ( ( self.__char * percent ), ( " " * ( 100 - percent ) ), percent )
    
        if self.__style == 2:
            if percent < 100:
                outStr = '[%s%s%s] %3d%%\r' % ( ( self.__char * percent ), ProgressBar.wheelChar[self.__wheelPos], ( " " * ( 100 - percent - 1 ) ), percent )
            else:
                outStr = '[%s] %3d%%\r' % ( ( self.__char * percent ), percent )
            self.__wheelPos += 1
            self.__wheelPos %= len( ProgressBar.wheelChar )

        sys.stdout.write( outStr )
        sys.stdout.flush()
        self.lastVal = percent

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
#    print ( time.time() - startTime )
    del pb


#===============================================================================

if __name__ == "__main__":
    main()
