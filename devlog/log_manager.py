# devlog/log_manager.py

import os
from datetime import datetime
import subprocess

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
def create_or_open_today_log():
    os.makedirs(LOG_DIR, exist_ok=True)
    filename = datetime.today().strftime("%Y-%m-%d") + ".md"
    filepath = os.path.join(LOG_DIR, filename)

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(f"# Dev Log - {datetime.today().strftime('%B %d, %Y')}\n\n")
            f.write("## What I did today\n\n- \n\n## What I learned\n\n- \n")

    # Open in Neovim if available, else fallback to regular editor
    try:
        subprocess.run(["nvim", filepath])
    except FileNotFoundError:
        os.system(f"${{EDITOR:-nano}} {filepath}")
