class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        flowers = 0
        i = 1
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                return True
            else:
                return False
        if flowerbed[0]==0 and flowerbed[1]==0 :
                flowers += 1
                flowerbed[0] = 1
        # todo is corner case
        while i < len(flowerbed)-1:
            # neighbours check
            if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                flowers += 1
                flowerbed[i] = 1
                if flowers==n:
                    return True
                i+=2
            else:
                i+=1
        if flowerbed[-1]==0 and flowerbed[-2]==0 :
                flowers += 1
                flowerbed[-1] = 1
        return flowers>=n