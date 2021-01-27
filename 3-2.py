
while True:
    hits=qq.events.pollBlockHits()
    if len(hits)>0:
        a=hits[0]
        x,y,z=a.pos.x,a.pos.y,a.pos.z
        block=qq.getBlock(x,y,z)
        qq.postToChat("你打到了"+str(block))
        if block==1:
            qq.setBlock(x,y,z,41)