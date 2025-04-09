from system_info.system_info import SystemInfo
from package_installer.package_installer import PackageInstaller
from symlink_manager.symlink_manager import SymlinkManager
from cli_parser.cli_parser import parse_args
from logger import info  

import os

class AppInstallation:
    def __init__(self, args):
        self.profile = args.profile
        self.dotfiles_dir = args.dotfiles_dir
        self.home_dir = os.path.expanduser("~")
        
        # Define paths for configuration files.
        self.packages_file = args.packages_file
        self.distros_file = args.distros_file
        
        # Optionally provide a symlinks file; if not given, default to the expected location.
        self.symlinks_file = args.symlinks_file
        if not self.symlinks_file:
            self.symlinks_file = os.path.join(
                self.dotfiles_dir, "python_installer", "config", "symlinks.json"
            )

        # Instantiate system info retrieval.
        self.system_info = SystemInfo()

        # Instantiate the package installer with the distro, profile, and config file paths.
        self.package_installer = PackageInstaller(
            distro=self.system_info.distro,
            profile=self.profile,
            packages_file=self.packages_file,
            distros_file=self.distros_file
        )

        # Instantiate the symlink manager with the symlinks file, dotfiles directory, and home directory.
        self.symlink_manager = SymlinkManager(self.symlinks_file, self.dotfiles_dir, self.home_dir)

    def run(self):
        info(f"Detected distro: {self.system_info.distro}")
        info(f"Running installation for profile: '{self.profile}'")
        self.package_installer.install_packages()
        self.symlink_manager.create_symlinks()


if __name__ == "__main__":
    args = parse_args()
    app = AppInstallation(args)
    app.run()