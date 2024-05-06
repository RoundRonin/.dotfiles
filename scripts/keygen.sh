if [ ! $1 ]; then
    echo "usage: kg <name>"
    exit
fi

name=$1

sshLocation=$HOME/.ssh

if [ ! -d $sshLocation ]; then
    mkdir $sshLocation
fi

ssh-keygen -t ed25519 -C "$name" -f "$sshLocation/${name}_id_ed25519"
