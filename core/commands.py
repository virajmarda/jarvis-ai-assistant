import os
import webbrowser

def run_command(cmd):
    if "open notepad" in cmd:
        os.system("notepad.exe")
        return "Opening Notepad"
    elif "open youtube" in cmd:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"
    else:
        return "Command not recognised. Asking AI..."
