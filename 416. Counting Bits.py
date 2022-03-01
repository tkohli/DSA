class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        if n == 5
        [0 1 2 3 4 5]
        [0 1 1 2 1 2]  
        we can clearly see tha pattern that all even 
        number will have same number of bit as it's mid val (div by 2)
        and odd is just adding prev + 1 bit
        """
        dp = [0]
        for i in range(1, n+1):
            if i % 2 == 1:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
        return dp
