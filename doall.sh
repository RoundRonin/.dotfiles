#!/bin/bash

trap "exit" INT
# TODO establish universal installation process, not only ubuntu-specific

arch=$(dpkg --print-architecture)

sudo -s <<EOF
EOF
apt update
apt install curl

source ./languages.sh

install_c
install_rust
install_node

source ./tools.sh

install_zsh
install_omz
install_nvim
install_tmux
install_docker

source ./utilities.sh

install_unzip
install_keychain
install_fd
install_zoxide
install_fzf
install_thefuck

source ./misc.sh

install_htop

source ./init.sh

create_links
change_shell
configure_ssh


