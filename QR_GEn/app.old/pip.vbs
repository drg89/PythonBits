command = "pip install --noindex --find-links=/pkg/ -r requirements.txt"
set shell = CreateObject("WScript.Shell")
shell.Run command
