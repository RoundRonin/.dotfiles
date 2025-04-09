import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Dotfiles Installer")
    parser.add_argument(
        "--profile",
        type=str,
        default="default",
        help="Profile to install (e.g., home, work)"
    )
    parser.add_argument(
        "--dotfiles-dir",
        type=str,
        default=os.path.expanduser("~/.dotfiles"),
        help="Path to the root of your dotfiles repository"
    )
    parser.add_argument(
        "--packages-file",
        type=str,
        default="python_installer/config/packages.json",
        help="Path to the packages configuration JSON file"
    )
    parser.add_argument(
        "--distros-file",
        type=str,
        default="python_installer/config/distros.json",
        help="Path to the distros configuration JSON file"
    )
    parser.add_argument(
        "--symlinks-file",
        type=str,
        default=None,
        help="Path to the symlinks configuration JSON file (optional)"
    )
    return parser.parse_args()