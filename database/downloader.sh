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
curl -O "https://www.ocso.com/portals/0/CFS_FEED/activecalls.xml" -o C:\Users\vikkh\Documents\github\OSCO_map\database
curl -O "https://www1.cityoforlando.net/opd/activecalls/activecadpolice.xml" -o C:\Users\vikkh\Documents\github\OSCO_map\database
sleep 7m
echo "downloaded"
done
