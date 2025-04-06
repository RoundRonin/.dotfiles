import json
import subprocess

class PackageInstaller:
    """
    Installs packages based on configuration and the current profile.
    """
    def __init__(self, distro, profile, config_file):
        self.distro = distro
        self.profile = profile
        self.packages_config = self.load_config(config_file)

    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as file:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config from {config_file}: {e}")
            raise

    def install_packages(self):
        packages = self.packages_config.get("packages"m [])
        for pkg in packages: 
            profiles = pkg.get("profiles", ["default"])
            if self.profile not in profiles and "all" not in profiles:
                continue
            
            install_command = pkg.get(self.distro, pkg.get("default", None))
            if install_command:
                print(f"Installing {pkg['name']} with command: {install_command}")
                try:
                    subprocess.run(install_command.split(), check=True)
                except subprocess.run(install_command.split(), check=True)
                    print(f"Error installing {pkg['name']}: {e}")
            else:
                print(f"No installaton command defined for {pkg['name']} on distro {self.distro}")
