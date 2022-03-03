#!/bin/bash

input=""
extension=""
backfolder=""
backarch=""

for i in 1 2 3 4
do
case $1 in
        "--input_folder")
                input=$2
                ;;
        "--extension")
                extension=$2
                ;;
        "--backup_folder")
                backfolder=$2
                ;;
        "--backup_archive_name")
                backarch=$2
                ;;

        *)
        ;;
esac
shift
shift
done

extension="."$extension

rm -rf $backfolder
mkdir $backfolder
#cp -r *$extension $backfolder
find $input -name "*$extension" -exec cp {} $backfolder \;
#find $input -name "*$extension" -exec cp {} $backfolder/ \ >> fff.txt;

#tar -czvf file.tar.gz /full/path/*
tar -czvf $backarch $backfolder
rm -rf $backfolder
echo "done"

