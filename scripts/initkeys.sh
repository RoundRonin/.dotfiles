#!/bin/bash

# TODO check if agent already exists
eval $(ssh-agent)

sshLocation=$HOME/.ssh
cd $sshLocation
pwd
files=`(ls | grep -Pv "^(authorized_keys|environment-.+|known_hosts.*|.+\.pub|config)$")`
echo $files

for file in $files
do
    ssh-add "$sshLocation/$file"
done
# Check if some keys are already added
