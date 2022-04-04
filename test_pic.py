#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
import time

import os

time.sleep(2)

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
x,y,z = mc.player.getTilePos()
# print(x,y,z)
mc.camera.setPos(x, y , z)
time.sleep(2)

shot_list = []

max_shot = 120

for i in range(max_shot):
    y += .25
    x += .25  
    mc.camera.setPos(x, y , z)
    file_path = f'/home/pi/Pictures/video_still{i:04}.png'
    os.system(f'scrot -u {file_path}')
    # os.system(f'scrot {file_path}')
    shot_list.append(file_path)

