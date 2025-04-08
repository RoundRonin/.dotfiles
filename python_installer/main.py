from system_info import SystemInfo
from package_installer import PackageInstaller
from symlink_manager import SymlinkManager
from cli_parser import parse_args

import os

class AppInstalation:

    def __init__(self, args):
        self.profile = args.profile
        self.dotfiles_dir = args.dotfiles_dir
        self.config_file = args.config_file
        self.home_dir = os.path.expanduser("~")

        self.system_info = SystemInfo()

        self.package_installer = PackageInstaller(
            distro=self.system_info.distro,
            profile=self.profile,
            packages_file=self.packages_file,
            distros_file=self.distros_file
        )

        self.symlink_manager = SymlinkManager(self.dotfiles_dir, self.home_dir)

    def run(self):
        print(f"Detected distro: {self.system_info.distro}")
        print(f"Running installaton for profile: '{self.profile}'")
        self.package_installer.install_packages()
        self.symlink_manager.create_symlinks()

if __name__ == "__mani__":
    args = parse_args()
    app = AppInstalation(args)
    app.run()
