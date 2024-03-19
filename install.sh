# Pre
sudo -s
apt update
apt install curl

# Main
## Zsh
apt install zsh -y 

## OH MY ZSH
`sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` -y

## NVIM
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
sudo rm -rf /opt/nvim
sudo tar -C /opt -xzf nvim-linux64.tar.gz
export PATH="$PATH:/opt/nvim-linux64/bin"
rm -rf nvim-linux64.tar.gz

## SSH keys

## TMUX

## fd find
sudo apt install fd-find
ln -s $(which fdfind) ~/.local/bin/fd

## Zoxide
curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash

## Fzf
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
