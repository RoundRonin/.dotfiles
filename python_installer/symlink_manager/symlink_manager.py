import os

class SymlinkManager:
    """
    Manages creation of symbolic links for dotfiles.
    """
    def __init__(self, dotfiles_dir, home_dir):
        self.dotfiles_dir = dotfiles_dir
        self.home_dir = home_dir

    def create_symlinks(self):
        mapping = {
            ".bashrc": "bashrc",
            ".vimrc": "vimrc"
            }

        for target, source in mapping.items():
            target_path = os.path.join(self.home_dir, target)
            
            config_path = os.path.join(self.dotfiels_dir, "config")
            source_path = os.path.join(config_path, target)

            if os.path.exists(target_path) and not os.path.islink(target_path):
                backup_path = target_path + ".backup"
                print(f"Backing up existing {target_path} to {backup_path}")
                os.rename(target_path, backup_path)
            if os.path.islink(target_path):
                os.remove(target_path)
            
            try:
                os.symlink(source_path, target_path)
                print(f"Created symlink: {target_path} -> {source_path}")
            except Exception as e:
                print(f"Error creating symlink for {target}: {e}")