# setup.py

import sys
from PyInstaller.__main__ import run

# Path to your aim_trainer.py
application_path = "aim_trainer.py"

# List of additional data files (images, sounds, etc.) used by your game
# The format is ('path/to/file', 'relative/directory/in/executable')
datas = [
    ("target.png", "images"),
    # ('path/to/sound.wav', 'sounds'),
    # Add as many as you need
]

# PyInstaller options
opts = [
    "--clean",
    "--windowed",
    "--onefile",
    # "--add-data=" + "".join([f"{data[0]}{data[1]}" for data in datas]),
    "--add-data=target.png:images",
    application_path,
]

if __name__ == "__main__":
    if sys.platform == "win32":
        opts.append("--icon=icon.ico")  # Specify the icon (Windows only)
    run(opts)
