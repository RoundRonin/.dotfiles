#!/bin/bash

arch=$(uname -m)

if [ "$arch" != "x86_64" ]; then
    # macOS or ARM64 build
    git clone https://github.com/neovim/neovim
    cd neovim
    git checkout stable
    make CMAKE_BUILD_TYPE=RelWithDebInfo
    sudo make install
else
    # Prebuilt AMD64 binary
    curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
    sudo rm -rf /opt/nvim
    sudo tar -C /opt -xzf nvim-linux64.tar.gz
    rm -rf nvim-linux64.tar.gz
    export PATH="$PATH:/opt/nvim-linux64/bin"
fi
