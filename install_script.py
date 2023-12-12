# Move the server folder to home(~) directory

import os
import shutil

home_directory = os.path.expanduser("~")
username = os.getlogin()

print("[+] Checking path....")

source_folder = ("./server")
destination_folder = os.path.join(home_directory, "server")

print("[+] Moving server file....")

shutil.move(source_folder, destination_folder)

#create the server.desktop file

print("[+] Creating launcher at Desktop....")

context = f"""[Desktop Entry]
version=1.0
Type=Application
Name=Server
Comment=
Exec=/home/{username}/server/server.py
Path=/home/{username}/server
Terminal=true
StartupNotify=false
Icon=/home/{username}/server/server.png"""


desktop_file_path = os.path.join(home_directory, "Desktop", "server.desktop")

with open(desktop_file_path, 'w') as f:
    f.write(context)


os.chmod(desktop_file_path, 0o755)
print("[+] Done !")
