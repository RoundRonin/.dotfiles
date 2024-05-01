#!/bin/bash

install_unzip () {
    sudo apt install unzip
}

install_keychain () {
    sudo apt install keychain
}

install_fd () {
    sudo apt install fd-find
    ln -s $(which fdfind) ~/.local/bin/fd
}

install_zoxide () {
    curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash
    export PATH="$HOME/.local/bin:$PATH"
}

install_fzf () {
    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    ~/.fzf/install
}

install_thefuck () {
    sudo apt update
    sudo apt install python3-dev python3-pip python3-setuptools
    pip3 install thefuck --user
}
