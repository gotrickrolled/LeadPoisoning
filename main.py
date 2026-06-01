#we start by praising Allah, subhanuhu wa taala
#Bismillah, i have no idea what i am doing

from pathlib import Path as p
import os #still unused
import platform #detects platform, still unused

folder = p.home() / "Downloads"

type = ("*wall.jpg", "*wall.png", "*wall.webp", "*wall.jpeg",)

for t in type:
    for i in folder.glob(t):
        print (i)