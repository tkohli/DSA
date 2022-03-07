from multiprocessing.spawn import import_main_path


import heapq
a = 1
b = 1
c = 7
"""
we use maxHeap but python dosen't has maxHeap so we make all
change all +ve to -ve val :) small Cheat 
"ccaccbcc" is output
"""
res = ""
maxHeap = []
for count,char in [[-a,'a'],[-b,'b'],[-c,'c']]:
    if count != 0:
        heapq.heappush(maxHeap, [count,char])

while maxHeap:
    count,char = heapq.heappop(maxHeap)
    # now check if val is same for the 3rd time
    if len(res)>=2 and res[-1] == res[-2] == char:
        if not maxHeap:
            break
        count2 ,char2 = heapq.heappop(maxHeap)
        res+=char2
        count2-=1
        if count2:
            heapq.heappush(maxHeap, [count2,char2])
    res+=char
    count-=1
    if count:
        heapq.heappush(maxHeap, [count,char])

        
