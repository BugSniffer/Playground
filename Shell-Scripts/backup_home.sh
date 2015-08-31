#!/bin/bash
#--------------------------------------------------------
# Author: RM
# Date: 2015-08-30
# Description:
# create archive for all directories
#--------------------------------------------------------
SrcDir="/home"
DstDir="/media/rainer/Datensicherung/home"

echo
echo "***************************************************"
echo "Create archives for all directories in $SrcDir"
echo "and put it into $DstDir"
echo
echo "be sure to be logged in as root !!"
echo "***************************************************"
echo

DstDir=$DstDir/`date "+%Y-%m-%d_%H%M%S"`
mkdir $DstDir

cd $SrcDir
for dirName in *
do
    # replace ' ' with '_' in directory names if necessary:
    tarName=`echo $dirName | tr -s ' ' '_'`".tar"
    dirName=`echo $dirName | tr -s ' ' '\ '`

    echo "["`date "+%Y-%m-%d %H:%M:%S"`"] Create archive '$DstDir/$tarName' from '$SrcDir/$dirName' ..."
    tar -cWf "$DstDir/$tarName" "$dirName"
    echo "["`date "+%Y-%m-%d %H:%M:%S"`"] ... finished"
done
