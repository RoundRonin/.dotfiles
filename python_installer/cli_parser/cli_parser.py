# cli_parser.py
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
        "--packages-file",
        type=str,
        default=os.path.abspath("config/packages.json"),
        help="Path to the packages configuration file (default: config/packages.json)"
    )
    parser.add_argument(
        "--distros-file",
        type=str,
        default=os.path.abspath("config/distros.json"),
        help="Path to the distros configuration file (default: config/distros.json)"
    )
    return parser.parse_args()

