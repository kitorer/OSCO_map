#!/bin/bash
#function pause(){
#   read -p "$*"
#}

# ...
# call it
#  curl -O "https://www.ocso.com/portals/0/CFS_FEED/activecalls.xml" -o C:\Users\vikkh\Documents\github\OSCO_map
#pause 'Press [Enter] key to continue...'

while true
do
curl -O "https://www.ocso.com/portals/0/CFS_FEED/activecalls.xml" -o C:\Users\vikkh\Documents\github\OSCO_map
sleep 7m
echo "downloaded"
done
