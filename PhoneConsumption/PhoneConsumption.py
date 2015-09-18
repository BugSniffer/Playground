#! /usr/bin/python
# -*- coding: utf-8 -*-

#===============================================================================
# PhoneConsumption
#
# Call:
# PhoneConsumption <InputFile>
#
# Description:
# 
#===============================================================================
# History:
# Date       Who  Comment
# ----------+----+--------------------------------------------------------------
# 2015-01-22 RM   - created
#===============================================================================

import sys
import os
import time
import datetime
from ProgressBar import ProgressBar
from time import localtime

class PhoneConsumption:

    #===========================================================================
    # Check and initialize input parameter
    #===========================================================================

    def __init__( self, inputFileName ):

        #---------------------------------------------------------------------
        # set default values if not specified:

        #---------------------------------------------------------------------
        # specify separator character for CSV file:
        self.csvSep = ';'

        # check input file name:
        if inputFileName:
            self.inFileName = inputFileName
        else:
            print( 'No input file given!' )
            sys.exit( 1 )

        if self.openInFile() != 0:
            sys.exit( 1 )

        self.__csvChar = ';'
    
    #===========================================================================
    # File IO
    #===========================================================================

    def openInFile( self ):
        try:
            self.inFile = open( self.inFileName, "r" )
        except Exception as e:
            print( '%s' % e )
            return 1
    
        self.inFileSize = float( os.path.getsize( self.inFileName ) )
        return 0

    def inFileReadline ( self ):
        try:
            data = self.inFile.readline()
        except Exception as e:
            print( 'Error reading input file: %s' % e )
            sys.exit( 1 )
        else:
            return data

    def printAllPhones( self ):

        ii = 0
        pb = [0] * 10
        header = [0] * 2
        while ii < 2:
            header[ii] = self.inFileReadline().rstrip()
            if len( header[ii] ) == 0:
                print( 'File corrupted!' )
                return
            ii += 1

        ii = 0
        while True:
            data = self.inFileReadline().rstrip()
            if len( data ) == 0:
                # end of file reached
                break
            list = data.split( self.__csvChar )

            phoneNo = list[0][:-7] + '-' + list[0][-7:-4] + ' ' + list[0][-4:-2] + ' ' + list[0][-2:]
            if ( float( list[9][:-4].replace( ',', '.' ) ) < float( list[5][:-4].replace( ',', '.' ) ) ):
                colorCode = '\033[1;31m'
            else:
                colorCode = ''
            print( '%s (%s) %s (%s) %s%s: %s\033[0m' % ( phoneNo, list[1], list[2], list[5], colorCode, header[0].split( self.__csvChar )[9], list[9] ) )
            print( header[0].split( self.__csvChar )[6] )

            # 3 and 7 contains remaining data volume
            pb[ii] = ProgressBar( capture = header[1].split( self.__csvChar )[3] + ': ', max = int( list[3] ), unit = ' von ' + list[3] + ' MB ' )
            pb[ii].printOut( int( list[6] ) )
            print

            # 4 and 8 contains remaining number of minutes/SMS
            if len( list[4] ) > 0:
                pb[ii] = ProgressBar( capture = header[1].split( self.__csvChar )[4] + ': ', max = int( list[4] ), unit = ' von ' + list[4] + ' Minuten' )
                pb[ii].printOut( int( list[7] ) )
                print
            else:
                print( header[1].split( self.__csvChar )[4] + ': ' )

            # calculate remaining number of days
            today = localtime()
            todayObj = datetime.datetime( today.tm_year, today.tm_mon, today.tm_mday )
            endDate = list[8].split( '.' )
            endObj = datetime.datetime( int( endDate[2] ), int( endDate[1] ), int( endDate[0] ) )
            numDays = ( endObj - todayObj )
            
            pb[ii] = ProgressBar( capture = header[0].split( self.__csvChar )[8] + ": ", max = 30, unit = ' Tage bis ' + str( endObj ).split( ' ' )[0] )
            pb[ii].printOut( numDays.days )
            print
            print( '-' * 140 )
            ii += 1

    
def main( args ):

    os.system( 'clear' )
    print( '=' * 45 )
    today = localtime()
    print( 'Übersicht Handy-Guthaben' )
    print( 'Zeitpunkt der Auswertung:' ), datetime.datetime( today.tm_year, today.tm_mon, today.tm_mday, today.tm_hour, today.tm_min, today.tm_sec )
    print( '=' * 45 )
    print

    ps = PhoneConsumption( args[1] )
    ps.printAllPhones()

#===============================================================================
# 
#===============================================================================

if __name__ == '__main__':
    main( sys.argv )
