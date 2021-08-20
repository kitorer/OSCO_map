#!/bin/bash
#just a compi le button ;-;
function pause(){
   read -p "$*"
}

python Parser.py
pause 'Press [Enter] key to continue...'
