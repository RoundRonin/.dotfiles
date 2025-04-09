import json
import subprocess
from logger import info, warning, error, debug

class PackageInstaller:
    """
    Installs packages based on the current distro and package origin.
    Uses distros.json for distro-specific logic and packages.json for package installation details.
    """
    def __init__(self, distro, profile, packages_file, distros_file, universal_postinstall_script=None):
        self.distro = distro
        self.profile = profile
        self.packages_config = self.load_config(packages_file)
        self.distros_config = self.load_config(distros_file)
        # Allow universal postinstall script location to be passed in; fallback to a default path.
        self.universal_postinstall_script = (
            universal_postinstall_script
            if universal_postinstall_script
            else "./python_installer/config/installation_scripts/universal_postinstall.sh"
        )

    def load_config(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            error(f"Error loading config from {file_path}: {e}")
            raise

    def resolve_distro_command(self):
        """
        Resolves the install command template for the current distro,
        accounting for parent-distro inheritance.
        """
        distro_config = self.distros_config.get("distros", {})
        current_distro = distro_config.get(self.distro, None)

        while current_distro and "parent" in current_distro:
            parent = current_distro["parent"]
            current_distro = distro_config.get(parent, None)

        if current_distro:
            return current_distro.get("install", distro_config.get("_", {}).get("install", None))
        else:
            return None

    def get_install_command(self, package):
        """
        Determines the installation command for a package.
        If the package's origin is:
          - the string "default": use the distro's default command (and replace {package}),
          - any other string: use that command,
          - a dict: try the distro-specific command, falling back to the "fallback" key.
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

    def run_distro_postinstall(self):
        """
        Walks up the inheritance chain from the distros config to determine the effective
        postinstall command for the current distro.
        """
        config = self.distros_config.get("distros", {})
        current = config.get(self.distro)
        postinstall = None
        while current:
            if "postinstall" in current:
                postinstall = current["postinstall"]
            if "parent" in current:
                current = config.get(current["parent"])
            else:
                break
        return postinstall

    def install_packages(self):
        packages = self.packages_config.get("packages", [])

        # Process each package.
        for package in packages:
            profiles = package.get("profiles", ["default"])
            if self.profile not in profiles and "default" not in profiles:
                continue

            install_command = self.get_install_command(package)
            if install_command:
                info(f"Installing {package['name']} with command: {install_command}")
                try:
                    subprocess.run(install_command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    error(f"Error installing {package['name']}: {e}")
            else:
                warning(f"No valid install command found for {package['name']} on distro {self.distro}")

            # Run package-specific post-install commands if defined.
            postinstall = package.get("postinstall", "")
            if postinstall:
                info(f"Running post-install command for {package['name']}: {postinstall}")
                try:
                    subprocess.run(postinstall, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    error(f"Error in post-install command for {package['name']}: {e}")

        # Once all packages are processed, run distro-specific post-install command.
        distro_postinstall = self.run_distro_postinstall()
        if distro_postinstall:
            info(f"Running distro-specific post-install command: {distro_postinstall}")
            try:
                subprocess.run(distro_postinstall, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                error(f"Error running distro-specific post-install command: {e}")

        # Finally, run universal post-install tasks.
        if self.universal_postinstall_script:
            info(f"Running universal post-install tasks from {self.universal_postinstall_script}...")
            try:
                subprocess.run(self.universal_postinstall_script, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                error(f"Error running universal post-install tasks: {e}")
