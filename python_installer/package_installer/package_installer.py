import json
import subprocess

# package_installer.py
import json
import subprocess


class PackageInstaller:
    """
    Installs packages based on the current distro and package origin.
    Uses distros.json for distro-specific logic and packages.json for package installation details.
    """
    def __init__(self, distro, profile, packages_file, distros_file):
        self.distro = distro
        self.profile = profile
        self.packages_config = self.load_config(packages_file)
        self.distros_config = self.load_config(distros_file)

    def load_config(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config from {file_path}: {e}")
            raise

    def resolve_distro_command(self):
        """
        Resolves the install command template for the current distro,
        accounting for parent-distro inheritance.
        """
        distro_config = self.distros_config.get("distros", {})
        current_distro = distro_config.get(self.distro, None)

        while current_distro and "parent" in current_distro:
            parent_distro = current_distro["parent"]
            current_distro = distro_config.get(parent_distro, None)

        return current_distro.get("install", distro_config.get("_", {}).get("install", None)) \
            if current_distro else None

    def get_install_command(self, package):
        """
        Determines the installation command for a package.
        """
        origin = package.get("origin", "default")

        if isinstance(origin, str):
            # Handle "default" origin (use the distro default command template)
            if origin == "default":
                command_template = self.resolve_distro_command()
                if command_template:
                    return command_template.replace("{package}", package["name"])
            return origin
        elif isinstance(origin, dict):
            # Handle per-distro and fallback logic
            distro_command = origin.get(self.distro, None)
            if distro_command and distro_command == "default":
                command_template = self.resolve_distro_command()
                if command_template:
                    return command_template.replace("{package}", package["name"])
            # Use distro-specific command if available, or fallback
            return distro_command or origin.get("fallback", None)

        return None  # If no command could be resolved

    def install_packages(self):
        """
        Installs only packages matching the active profile.
        """
        packages = self.packages_config.get("packages", [])
        for package in packages:
            # Check if the package belongs to the active profile
            profiles = package.get("profiles", ["default"])
            if self.profile not in profiles and "default" not in profiles:
                continue  # Skip packages not relevant to this profile

            install_command = self.get_install_command(package)
            if install_command:
                print(f"Installing {package['name']} with command: {install_command}")
                try:
                    subprocess.run(install_command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {package['name']}: {e}")
            else:
                print(f"No valid install command found for {package['name']} on distro {self.distro}")


