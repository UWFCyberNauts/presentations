#!/usr/bin/env bash
# Mikes cruddy backup script

## Functions
function backup {
    cd $storageDir
    tar -czf $backupName.tgz $backupDir 2>/dev/null 1>/dev/null || { echo "Failed to backup $backupDir!" ; exit 1 ;}
    cat /tmp/newTimes.txt > timestamp.txt
    tar -cf $backupName.tar timestamp.txt $backupName.tgz
    rm -rf $backupName.tgz timestamp.txt /tmp/newTimes.txt
}

function usage { echo "Usage: $0 -b [BACKUP DIRECTORY] -s [STORAGE DIRECTORY]"; }

### MAIN ###
OPTERR=0 # Be quite getopts
storageDir=NULL
backupDir=NULL
backupName=NULL

while getopts :hb:s: opt ; do
    case $opt in
        b)
            backupDir=$OPTARG
            ;;
        s)
            storageDir=$OPTARG
            ;;
        h)
            usage
            exit 0
            ;;
        :)
            echo "Option -$OPTARG requires an argumet!"
            usage
            exit 1
            ;;
        \?)
            usage
            exit 1
            ;;
    esac
done

case $storageDir in
    NULL)
        usage
        exit 1
        ;;
esac

case $backupDir in
    NULL)
        usage
        exit 1
        ;;
esac

backupName=$(basename $backupDir)

## Get the timestamp of the dir and its subdirs to backup
find $backupDir -type d -printf '%f %c\n' > /tmp/newTimes.txt

## Check for a previous backup
cd $storageDir
if [[ -f $backupName.tar ]]; then ## timestamp.txt exists
    ## Compare timestamps
    tar -xf $backupName.tar 
    if [[ $(cat /tmp/newTimes.txt) != $(cat timestamp.txt) ]]; then
        ## Time stamp on backup does not match last modified time stamp so backup
        backup
    else 
        rm -rf timestamp.txt $backupName.tgz /tmp/newTimes.txt
    fi
else ## timestamp.txt does not exist.. Perform a backup.
    backup
fi

### END MAIN ###

