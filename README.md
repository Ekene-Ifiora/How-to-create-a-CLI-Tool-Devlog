# 🛠️ DevLog CLI — Your Personal Developer Journal

A simple and elegant command-line tool to keep daily development logs right from your terminal. Designed to work with `nvim`, this tool helps you stay consistent, focused, and reflective on your coding journey.

---

## 📸 Preview

![image1](https://github.com/user-attachments/assets/8336c230-22f3-475c-807e-653ba4c37dd8)


---

## ✨ Features

- 📅 Creates or opens a markdown log for the current day  
- 📁 Stores logs in your project directory (or custom location)  
- 📝 Auto-generates log templates  
- ⚡ Powered by [Click](https://click.palletsprojects.com/) and [Neovim](https://neovim.io/)

---

## 🚀 Getting Started

Follow these steps to set up and start using your DevLog CLI.

---

### 1. 📁 Project Structure

Make sure your project folder looks like this:

<img width="198" alt="image" src="https://github.com/user-attachments/assets/a533fc3c-b698-483a-83cf-6f8452d4431f" />

> 🧠 The inner `devlog/` directory is your Python package. Make sure it contains an `__init__.py` file.

---

### 2. 🔧 Setting Up the Virtual Environment

python3 -m venv venv
source venv/bin/activate
pip install –upgrade pip

---

### 3. 📦 Installing in Editable Mode

pip install -e .

This will install your CLI tool locally and allow you to run it as `devlog` from your terminal.

---

### 4. 🧠 How It Works

- CLI command: `devlog new`  
- Creates a file named like `2025-03-31.md`  
- Opens it with Neovim for quick note-taking  

Logs are saved in the same directory as your `log_manager.py` file, or in a `logs/` subfolder if configured.

---

## 🧩 CLI Code Breakdown

```python
**cli.py**

import click
from devlog.log_manager import create_or_open_today_log

@click.group()
def cli():
“”“DevLog CLI - your daily dev journal.”””

@cli.command()
def new():
“”“Create or open today’s log.”””
create_or_open_today_log()

if name == “main”:
cli()

**log_manager.py**

import os
from datetime import datetime
import subprocess

Logs will be saved in the current directory of this file

LOG_DIR = os.path.dirname(os.path.abspath(file))

def create_or_open_today_log():
os.makedirs(LOG_DIR, exist_ok=True)
filename = datetime.today().strftime(”%Y-%m-%d”) + “.md”
filepath = os.path.join(LOG_DIR, filename)

if not os.path.exists(filepath):
    with open(filepath, "w") as f:
        f.write(f"# Dev Log - {datetime.today().strftime('%Y-%m-%d')}\n\n")
        f.write("## What I did today\n\n- \n\n## What I learned\n\n- \n")

subprocess.run(["nvim", filepath])
```

---

## 💻 Usage

Once installed, run:

devlog new

That’s it! Your daily markdown log opens in Neovim, ready for writing.

---

## 📥 Requirements

- Python 3.7+  
- Neovim installed and in your system PATH  
- Dependencies:
  - `click`
  - `pynvim`

Install them manually with:

pip install -r requirements.txt

Or declare them in `setup.py` under `install_requires`.

---

---

## 🧪 Future Ideas

- Add `list` command to show recent logs  
- Add search functionality  
- Allow custom log directory via config or `.env`  
- Push logs to Git automatically  
- Support editor config (VSCode, vim, etc.)

---

## 🤝 Contributing

PRs and feedback are welcome. This is a personal journaling tool, but improvements are always appreciated!

To contribute:

git clone [https://github.com/yourusername/devlog.git](https://github.com/Ekene-Ifiora/How-to-create-a-CLI-Tool-Devlog.git)
cd devlog
pip install -e .

---

_Thanks for checking out DevLog CLI. Happy journaling! ✨_

