import os
import json

class SymlinkManager:
    """
    Manages creation of symbolic links for dotfiles by reading a JSON configuration.
    
    The JSON file (e.g. python_installer/config/symlinks.json) should have the following format:
    
    {
      "symlinks": [
        { "target": ".bashrc", "source": ".bashrc" },
        { "target": ".zshrc",  "source": ".zshrc" },
        { "target": ".tmux.conf", "source": ".tmux.conf" },
        { "target": ".config/htop", "source": ".config/htop" },
        { "target": ".config/nvim", "source": ".config/nvim" },
        { "target": ".config/alacritty", "source": ".config/alacritty" }
      ]
    }
    
    Here, each "target" is a file or directory path in the user's home directory,
    and "source" is a file or folder relative to the dotfiles repository root.
    """
    def __init__(self, symlinks_file, dotfiles_dir, home_dir):
        self.symlinks_file = symlinks_file
        self.dotfiles_dir = dotfiles_dir
        self.home_dir = home_dir
        self.links = self.load_symlinks()

    def load_symlinks(self):
        """
        Loads the symlink mapping from the JSON file.
        Returns a list of mapping dictionaries.
        """
        try:
            with open(self.symlinks_file, 'r') as f:
                config = json.load(f)
                return config.get("symlinks", [])
        except Exception as e:
            print(f"Error loading symlink config from {self.symlinks_file}: {e}")
            return []

    def create_symlinks(self):
        """
        Iterates over each symlink mapping and creates symbolic links accordingly.
        
        For each mapping:
          - Computes the full target path (in the user's home directory)
            and the full source path (relative to the dotfiles repository root).
          - If a target file exists and is not a symlink, it is backed up.
          - If a symlink already exists at the target path, it is removed.
          - Finally, the source is symlinked to the target path.
        """
        for link in self.links:
            target = link.get("target")
            source = link.get("source")
            
            # Compute full file paths.
            target_path = os.path.join(self.home_dir, target)
            source_path = os.path.join(self.dotfiles_dir, source)
            print(f"Processing symlink: {target_path} -> {source_path}")

            # If a non-symlink file exists at the target, back it up.
            if os.path.exists(target_path) and not os.path.islink(target_path):
                backup_path = target_path + ".backup"
                print(f"Backing up existing file {target_path} to {backup_path}")
                os.rename(target_path, backup_path)
                
            # If there's already a symlink, remove it.
            if os.path.islink(target_path):
                print(f"Removing existing symlink at {target_path}")
                os.remove(target_path)
            
            # Ensure the directory for the target exists.
            target_dir = os.path.dirname(target_path)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir, exist_ok=True)
                print(f"Created directory {target_dir}")
                
            # Create the symlink.
            try:
                os.symlink(source_path, target_path)
                print(f"Created symlink: {target_path} -> {source_path}")
            except Exception as e:
                print(f"Error creating symlink for {target}: {e}")