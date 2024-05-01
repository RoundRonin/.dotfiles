# Pre

arch=$(dpkg --print-architecture)

sudo -s
apt update
apt install curl

# Compilers and utilities
#
## C

sudo apt install clang -y
sudo apt install cmake -y

## Rust

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -y

## JS

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

source ~/.zshrc

nvm install --ltc

## Docker CLI

sudo apt install docker

## Unzip

sudo apt install unzip

## NVM, NPM

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
bash
nvm install --lts
nvm use --lts
exit

# Main
## Zsh
apt install zsh -y 

## OH MY ZSH
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" -y

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

## NVIM
# TODO replace with case statement
if [ $arch -ne "amd64" ]
then
	# MAC: curl -LO https://github.com/neovim/neovim/releases/download/nightly/nvim-macos-arm64.tar.gz
	git clone https://github.com/neovim/neovim
	git checkout stable
	cd neovim && make CMAKE_BUILD_TYPE=RelWithDebInfo
	sudo make install
else
	# Release for AMD64
	curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
	sudo rm -rf /opt/nvim
	sudo tar -C /opt -xzf nvim-linux64.tar.gz
	rm -rf nvim-linux64.tar.gz
fi
export PATH="$PATH:/opt/nvim-linux64/bin"

## Keychain
sudo apt install keychain

## SSH keys

## TMUX
sudo apt install tmux
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

tmux source ~/.tmux.conf

## fd find
sudo apt install fd-find
ln -s $(which fdfind) ~/.local/bin/fd

## Zoxide
curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash

export PATH="$HOME/.local/bin:$PATH"

## Fzf
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

## Htop
sudo apt install htop

## TheFuck
sudo apt update
sudo apt install python3-dev python3-pip python3-setuptools
pip3 install thefuck --user

