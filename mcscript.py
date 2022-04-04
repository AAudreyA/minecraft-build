from mcpi import minecraft 
mc = minecraft.Minecraft.create()
mc.postToChat("hello world")
flower = 38 
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, x, flower)
