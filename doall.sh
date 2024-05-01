

# TODO establish universal installation process, not only ubuntu-specific

arch=$(dpkg --print-architecture)

sudo -s
apt update
apt install curl

bash languages.sh

install_c
install_rust
install_node

bash tools.sh

install_zsh
install_omz
install_nvim
install_tmux
install_docker

bash utilities.sh

install_unzip
install_keychain
install_fd
install_zoxide
install_fzf
install_thefuck

bash misc.sh

install_htop

bash init.sh

create_links
change_shell
configure_ssh


