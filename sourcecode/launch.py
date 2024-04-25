import subprocess
# EDIT THIS FILE IF YOUR FAVOURITE TERMINAL EMULATOR IS NOT PRESENT subprocess.run(["YOUR_TERM", "-e", "./window"])
subprocess.run(["alacritty", "-e", "./window"]) 
subprocess.run(["gnome-terminal", "--", "./window"]) 
subprocess.run(["konsole", "-e", "./window"]) 
subprocess.run(["wezterm", "-e", "./window"]) 
subprocess.run(["kitty", "-e", "./window"]) 
subprocess.run(["xterm", "-e", "./window"]) 
subprocess.run(["st", "-e", "./window"])
