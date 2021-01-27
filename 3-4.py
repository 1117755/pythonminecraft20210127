from mcpi.minecraft import Minecraft
qq=Minecraft.create()

while True:
    hits=qq.events.pollProjectileHits()
    if len(hits)>0:
        a=hits[0]


