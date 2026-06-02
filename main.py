#Bismillah, i have no idea what i am doing

from pathlib import Path as p
import shutil

folder = p.home() / "Downloads"
wall_folder = folder / "Wallpapers"

if wall_folder.is_dir():
    pass
else:
    wall_folder.mkdir()


type = ("*wall.jpg", "*wall.png", "*wall.webp", "*wall.jpeg",)

for t in type:
    for i in folder.glob(t):
        shutil.move(folder/i, wall_folder)
        print(i) #if this prints anything, this didnt work