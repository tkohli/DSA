# Tower of hanoi
"""
n - number of disks 
move top n-1 disk from A to B using c as intermediate 
move the remaining disk from A to C
move n-1 disks from B to C using A as intermediate 
"""
def towers(n,source,destination,support):    # n =  number of disk, a,b,c = towers
    if n==1:
        # if only one disk, then move it from A to C directly
        print("move disk %i from pole %s to pole %s"%(n,source,destination)) 
    else:
        towers(n-1,source,support,destination) # first move n-1 disk to B, i.e. using C as intermediate
        print("move disk %i from pole %s to pole %s"%(n,source,destination)) # move remaining 1 disk to C
        towers(n-1,support,destination,source) # ni1 disk move from B to C

towers(2,"A","C","B") # A = starting, C finishing , B intermediate  
        

