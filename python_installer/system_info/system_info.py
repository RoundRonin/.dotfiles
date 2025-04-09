from logger import info, warning, error, debug

class SystemInfo:
    """
    Detects and provides system-specific information
    """
    def __init__(self):
        self.distro = self._get_distro_info()

    def _get_distro_info(self):
        distro = "default"
        try:
            with open("/etc/os-release") as file:
                for line in file:
                    if line.startswith("ID="):
                        distro = line.strip().split("=")[1].strip('"')
                        break
        except Exception as e:
            error(f"Error detecting ditsro: {e}")
        return distro
