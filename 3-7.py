def plantTree(x,y,z):
    qq.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,18)
    qq.setBlocks(x,y,z,x,y+4,z,17)            
from mcpi.minecraft import Minecraft
qq=Minecraft.create()

x,y,z=qq.player.getTilePos()

    
for i in range(10):
    plantTree(x+i*5,y,z)
   