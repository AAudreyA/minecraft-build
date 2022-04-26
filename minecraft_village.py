#!/usr/bin/env python3
import random
import time

from mcpi import block
from mcpi.minecraft import Minecraft


mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

randomBase = [
    block.COBBLESTONE.id, 
    block.STONE.id,
    block.SANDSTONE.id, 
    block.MOSS_STONE.id, 
    block.BRICK_BLOCK.id, 
    block.STONE_BRICK.id, 
    block.NETHER_BRICK.id
    ]


def text(text, toScreen = True, userInput = True):
    """ This function takes user input to send a custom message to the Minecraft 
        chat and the command line and then accepts user input to impact how the 
        program moves forward. 

    Args:
        text (str): text is the output of the function which apears in the comand 
            line interface and the minecraft chat 
        toScreen (bool, optional): the toScreen keyword argument posts whatever 
            text it is given to the Minecraft chat and the command line interface. 
            Defaults to True.
        userInput (bool, optional): the userInput keyword argument is responsible 
            for letting a user interact with the program in the command line 
            interface. Defaults to True.

    Returns:
        str: whatever is assigned to the text argument at the time it is posted
    """    
    if toScreen == True:
       mc.postToChat(text)
    if userInput == True:
        var = input(text)
        return var 

def build_village(x,y,z,randomBase):
    """Communicates with the user, and collects their info to build a village.

    Args:
        x (int): player x location
        y (int): player y location
        z (int): player z location
        randomBase (list): list of block for random wall blocks
    """
    time.sleep(2)
    text(
        "Please make sure Minecraft is running. Press any key to continue.")
    # userInput=False)
    # text("Press any key to continue.")

    name = text("What is your name? ")
    text(f"Hello {name}",userInput = False)
    num_village = int(text(f"How many houses would you like in each row of your village {name}? "))
    # if num_village <
    text(f"Presenting {name}ville!", userInput = False)
    text("building village . . . ",toScreen = False, userInput = False)
    village = [0]

    for n in range(num_village-1):
        p = n % 3
        if p == 0:
            village.append(10)
        else:
            village.append(7)
    x_ = x
    for v in village:
        randomBlock = random.choices(randomBase)
        x += v
        build_house(x,y,z,randomBlock)
    x = x_
    for v in village:
        randomBlock = random.choices(randomBase)
        x += v
        build_house(x,y,z-12,randomBlock)
    

    text(f"go explore {name}ville",  userInput = False)


def build_house(x,y,z,randomBlock):
    """this function builds each house in the village, including randomizing the 
        texture of it, using the x, y, and z coordinates.
    
    Args:
        x (int): the x position to start each building. It is the position of the 
            player the first time before x is changed by the code to make the whole 
            village 
        y (int): _description_: the y position to start each building. It is the 
            y position of the player  
        z (int): _description_: the z position to start each building. It is the 
            z position of the player 
        randomBase (list): an argument that randomly changes the material of each 
            house in a village 

    Returns:
        int: the x, y, and z ending positions yo use as inputs to start building a new house
    """    

    """ The code below I modified from a public magazine project in magpi issue 
    68 that I did around four years ago. The idea of building a house is thiers but 
    the dimentions and some of the materials and placements where my code as well 
    as the random blocks
    """

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

    # roof
    for i in range(3):
        mc.setBlocks(x-1+i, y+3+i, z+2, x-1+i, y+3+i, z+10, block.STAIRS_WOOD.id, 0)
        mc.setBlocks(x+5-i, y+3+i, z+2, x+5-i, y+3+i, z+10, block.STAIRS_WOOD.id, 1)
        mc.setBlocks(x+2, y+5, z+2, x+2, y+5, z+10, block.WOOD_PLANKS.id)

        if (int(4/2) - i > 0):
            mc.setBlocks(x+1+i, y+4+i, z+3, x+4-i-1, y+4+i, z+3, randomBlock, 0)
            mc.setBlocks(x+1+i, y+4+i, z+9, x+4-i-1, y+4+i, z+9, randomBlock, 1)
    return x,y,z 


def clearAll (x,y,z):
    """Clears all the blocks so there is a flat surface to build the village.

    Args:
        x (int): player x location
        y (int): player y location
        z (int): player z location
    """    
    mc.setBlocks(x-500,y,z-500,x+500,y+50,z+500, block.AIR)

if __name__ == "__main__":
    clearAll(x=x, y=y, z=z)
    build_village(x=x,y=y,z=z,randomBase=randomBase)