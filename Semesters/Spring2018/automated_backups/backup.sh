#!/usr/bin/env bash

## Change to a working directory
cd /home/mmitc/
time=$(ls -l | grep Code | awk '{print $8}')

function backup() {
    cd /home/mmitc/Public/
    tar -cvzf backup.tgz /home/mmitc/Code/
    echo $time > /home/mmitc/Public/timestamp.txt
}

## log the current timestamp for the code directory
echo $time > /tmp/timetmp.txt

## Check for a previous backup
if [ -f /home/mmitc/Public/timestamp.txt]; then
    backup()
    exit 0
else 
    # compare timestamps
    if [[ $time == $(cat /home/mmitc/Public/timestamp.txt) ]]; then
        ## Time stamp on backup matches last modified time stamp...
        ## Nothing else to do so exit.
        exit 0
    else 
        backup()
    fi
fi

