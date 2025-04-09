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

        # Traverse up the inheritance tree if a parent is defined:
        while current_distro and "parent" in current_distro:
            parent_distro = current_distro["parent"]
            current_distro = distro_config.get(parent_distro, None)

        # Use the install command from the resolved distro config, or fall back via "_" key.
        if current_distro:
            return current_distro.get("install", distro_config.get("_", {}).get("install", None))
        else:
            return None

    def get_install_command(self, package):
        """
        Determines the installation command for a package.
        If the package's origin is:
          - a string "default": it uses the distro's default installation command template.
          - any other string: the given command is used.
          - a dict: tries to use a distro-specific key, then falls back to the "fallback" key.
        """
        origin = package.get("origin", "default")

        if isinstance(origin, str):
            if origin == "default":
                command_template = self.resolve_distro_command()
                if command_template:
                    return command_template.replace("{package}", package["name"])
            return origin
        elif isinstance(origin, dict):
            distro_command = origin.get(self.distro, None)
            if distro_command and distro_command == "default":
                command_template = self.resolve_distro_command()
                if command_template:
                    return command_template.replace("{package}", package["name"])
            return distro_command or origin.get("fallback", None)
        return None

    def install_packages(self):
        packages = self.packages_config.get("packages", [])

        for package in packages:
            # Determine which installation profiles apply for this package.
            profiles = package.get("profiles", ["default"])
            # If the current profile isn’t listed and "default" is not provided, skip this package.
            if self.profile not in profiles and "default" not in profiles:
                continue

            # Get the installation command (either using distro defaults or a custom command).
            install_command = self.get_install_command(package)
            if install_command:
                print(f"Installing {package['name']} with command: {install_command}")
                try:
                    subprocess.run(install_command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error installing {package['name']}: {e}")
            else:
                print(f"No valid install command found for {package['name']} on distro {self.distro}")

            # Execute an optional post-install command for additional setup (like creating symlinks).
            postinstall = package.get("postinstall", "")
            if postinstall:
                print(f"Running post-install command for {package['name']}: {postinstall}")
                try:
                    subprocess.run(postinstall, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error in post-install command for {package['name']}: {e}")