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

    parser.add-argument(
            "--dotfiles-dir",
            type=str,
            default=os.path.abspath(os.path.join(os.getcwd(), "dotfile")),
            help="Path to your dotfiles directory"
            )
    
    parser.add_argument(
            "--config-file",
            type=str,
            default="config/packages.json",
            help="Path to the package configuration JSON file"
            )

    return parser.parse_args()
