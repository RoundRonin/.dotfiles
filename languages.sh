

install_c () {
    sudo apt install clang -y
    sudo apt install cmake -y
}

install_rust () {
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -y
}

install_node () {
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

    bash
    nvm install --ltc
    nvm use --ltc
    exit
    # TODO add checks for error (then install 16, use 16)
}
