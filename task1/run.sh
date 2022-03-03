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

#rm -rf $backfolder
mkdir $backfolder
find 2> /dev/null $input -name "*$extension" -exec cp {} $backfolder/ \;
tar -czf $backarch $backfolder
#rm -rf $backfolder
echo "done"

