class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        out = [float("inf")]*(amount+1)
        out[0] = 0
        for coin in coins:
            for i in range(amount+1):
                if coin <= i:
                    out[i] = min(out[i], out[i-coin]+1)
        if out[-1] == float("inf"):
            return -1
        return out[-1]
