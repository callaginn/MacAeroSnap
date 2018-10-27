#!/bin/bash

# Simple Yellow Alert
alert () {echo; tput bold && tput setaf 3 && echo "$1" && tput sgr0;}

# Install MouseTools dependency if needed
if [[ ! $(which MouseTools) ]]; then
    # Download MouseTools and check last-known MD5 hash. If it's the same, then
    # install it automatically. Otherwise, it will need to be added manually.
    m5hash="59fa0abec7f326f29b4fe86344ad3994"
    curl -L http://www.hamsoftengineering.com/assets/MouseTools.zip -o ~/bin/MouseTools.zip --create-dirs
    ziphash=($(md5 -r ~/bin/MouseTools.zip))

    if [[ "${ziphash[0]}" == "${m5hash}" ]]; then
        open ~/bin/MouseTools.zip
    else
        alert "Remote file has changed, exiting installer.";
    fi

    sleep 1;
    rm ~/bin/MouseTools.zip
fi
