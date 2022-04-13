# mc.setBlocks(x, y, z, x, y, z, block..id)
#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

time.sleep(2)
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()


def text(text, toScreen = True, userInput = True):
    if toScreen == True:
       mc.postToChat(text)
    if userInput == True:
        var = input(text)
        return var 
    
name = text("What is your name?")
text(f"hi hello {name}fgdhfgnfhftn",userInput = False)
num_village = int(text(f"How many houses would you like in your village {name}?"))
# if num_village <
text(f"Presenting {name}ville!", userInput = False)
text("building village . . . ",toScreen = False, userInput = False)

village = [0]

for n in range(num_village):
    p = n % 3
    if p == 0:
        village.append(10)
    else:
        village.append(7)
  
randomBase = [block.COBBLESTONE.id, block.STONE.id,block.SANDSTONE.id, block.MOSS_STONE.id, block.BRICK_BLOCK.id, block.STONE_BRICK.id, block.NETHER_BRICK.id]



def build_house(x,y,z,randomBase):
   
    randomBlock = random.choices(randomBase)
    
    #walls
    mc.setBlocks(x, y, z+3, x+4, y+4, z+9, randomBlock)
    mc.setBlocks(x+1, y, z+4, x+4-1, y+4, z+8, block.AIR.id)

    # floor
    mc.setBlocks(x+1, y, z+4, x+3, y, z+8, block.WOOD_PLANKS.id)

    # door
    mc.setBlock(x+2, y+1, z+3, block.DOOR_WOOD.id, 0)
    mc.setBlock(x+2, y+2, z+3, block.DOOR_WOOD.id, 8)

    # windows
    mc.setBlocks(x+2, y+2, z+9, x+2, y+2, z+9, block.GLASS.id)
    mc.setBlocks(x, y+2, z+6, x, y+2, z+6, block.GLASS.id)
    mc.setBlocks(x+4, y+2, z+6, x+4, y+2, z+6, block.GLASS.id)

    # stairs
    mc.setBlocks(x+2, y, z+2,x+2, y, z+2, block.STAIRS_WOOD.id,2)

    #add wood deails
    mc.setBlocks(x, y+4, z+3, x+4, y+4, z+3, block.WOOD.id,)
    mc.setBlocks(x, y+4, z+9, x+4, y+4, z+9, block.WOOD.id,)
    mc.setBlocks(x, y+4, z+3, x, y+4, z+9, block.WOOD.id,)
    mc.setBlocks(x+4, y+4, z+3, x+4, y+4, z+9, block.WOOD.id,)

    # roof
    for i in range(4):
        mc.setBlocks(x-1+i, y+4+i, z+2, x-2+i, y+4+i, z+10, block.STAIRS_WOOD.id, 0)
        mc.setBlocks(x+4-i, y+4+i, z+2, x+4-i, y+4+i, z+10, block.STAIRS_WOOD.id, 1)
        
        if (int(4/2) - i > 0):
            mc.setBlocks(x+1+i, y+4+i, z+3, x+4-i-1, y+4+i, z+3, block.COBBLESTONE.id, 0)
            mc.setBlocks(x+1+i, y+4+i, z+9, x+4-i-1, y+4+i, z+9, block.COBBLESTONE.id, 1)
    return x,y,z 



#village = [0,7, 10,7]
#x_pos = x-(sum(village)/len(village))
#mc.camera.setPos(x_pos, y+20 , z)

for v in village:
     x += v
     build_house(x,y,z,randomBase)

#mc.setBlocks(x-100, y, z-100, x+100, y+30, z+100, block.AIR.id)
#mc.setBlocks(x-100, y, z-100, x+100, y, z+100, block.SAND.id)
