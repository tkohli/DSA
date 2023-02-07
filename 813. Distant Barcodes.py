# Distant Barcodes
"""
Ques - Rearrange the barcodes so that no two adjacent barcodes are equal. 
You may return any answer, and it is guaranteed an answer exists.

Sort bar codes depending on its occurrence.
We put the most frequent on every two positions,(first, third, fifth...)
In this we, we make sure that no two adjacent bar codes are equal.

Steps -
0. make an ans arr of size n and i = 0
1. Make a counter 
2. Iterate on counter based on higher frequency [Hint you can use most_common() funtion in dict Google it]
3. put it on every two positions,(0,2,4...)

After this structure, main problem is to find out how to implement 3rd step
    i += 2
    if i >= n: 
        i = 1
something like this 
"""

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        i = 0
        res = [0]*len(barcodes)
        cnt = Counter(barcodes)
        for k,v in cnt.most_common():
            for _ in range(v):
                res[i]=k
                i+=2
                if i>=len(res):
                    i=1  
        return res