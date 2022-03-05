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
mkdir $backfolder
counter=0
for i in $(find 2> /dev/null $input -name "*$extension")
do
newName=$(basename $i $extension)
newName="$newName$counter$extension"
cp $i $backfolder/$newName
counter=$((counter + 1))
done
tar -czf $backarch $backfolder

echo "done"

