#!/bin/bash
set -e

# Title Banner
echo "=========================="
echo "Dotfiles Installer - Init"
echo "=========================="

# Check if Python3 is available
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed on your system."
    echo "Please install Python3 to continue."
    echo "For Debian-based systems: sudo apt-get install python3"
    echo "For Arch-based systems: sudo pacman -S python"
    echo "For Fedora-based systems: sudo dnf install python3"
    exit 1
fi

# Python3 is detected; proceed with the installation.
echo "Python3 detected. Proceeding with installation..."
python3 ./python_installer/main.py "$@"
