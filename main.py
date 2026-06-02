#Bismillah, i have no idea what i am doing

from pathlib import Path as p
import shutil

folder = p.home() / "Downloads"
wall_folder = folder / "Wallpapers"

wall_folder.mkdir(exist_ok = True)

type = ("*wall.jpg", "*wall.png", "*wall.webp", "*wall.jpeg",)

for t in type:
    for i in folder.glob(t):
        shutil.move(i, wall_folder)

#if the following prints anything, this didnt work
for t in type:
    for i in folder.glob(t):
        print(i)
