from mcpi.minecraft import Minecraft
qq=Minecraft.create()
import random,time

while True:
    x,y,z=qq.player.getPos()
    a=random.uniform(-20,20)
    b=random.uniform(-20,20)
    y=y+30
    qq.spawnEntity(x+a,y,z+b,93)
    time.sleep(0.1)
    