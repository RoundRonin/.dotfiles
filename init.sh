#!/bin/bash

create_links () {
    rm -rf ~/.bashrc
    ln -s ~/.dotfiles/.bashrc ~/.bashrc
    rm -rf ~/.zshrc
    ln -s ~/.dotfiles/.zshrc ~/.zshrc
    ln -s ~/.dotfiles/.tmux.conf ~/.tmux.conf
    ln -s ~/.dotfiles/.config/htop ~/.config/htop
    ln -s ~/.dotfiles/.config/nvim ~/.config/nvim
    ln -s ~/.dotfiles/.config/alacritty ~/.config/alacritty
}

change_shell () {
    chsh -s /usr/bin/zsh
}

configure_ssh () {
    #TODO 
}

create_links
chage_shell
