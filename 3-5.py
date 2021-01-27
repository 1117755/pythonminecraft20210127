from mcpi.minecraft import Minecraft
qq=Minecraft.create()

x,y,z=qq.player.getTilePos()
for i in range(0,20):
    qq.setBlock(x+i+1,y-1,z+i,41)
    qq.setBlock(x+i+2,y-1,z+i,41)
    qq.setBlock(x+i+3,y-1,z+i,41)
