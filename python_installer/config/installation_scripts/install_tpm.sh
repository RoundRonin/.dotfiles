#!/bin/bash
set -e

# If no tmux session exists, start a dummy session.
if ! tmux has-session 2>/dev/null; then
  echo "No tmux session found. Starting a dummy session..."
  tmux new-session -d -s dummy || true
fi

# Proceed with the TPM installation and any other tmux-based setup.
if [ ! -d "$HOME/.tmux/plugins/tpm" ]; then
  echo "Cloning TPM (Tmux Plugin Manager)..."
  git clone https://github.com/tmux-plugins/tpm "$HOME/.tmux/plugins/tpm"
fi

# Optionally, run TPM's installation command.
# "$HOME/.tmux/plugins/tpm/scripts/install_plugins.sh" || true
tmux source ~/.tmux.conf

# Optionally, kill the dummy session if you don't want to leave it running.
tmux kill-session -t dummy 2>/dev/null || true
