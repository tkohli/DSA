class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        out = [0]*(amount+1)
        out[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                if coin <= i:
                    out[i] += out[i-coin]
        return out[-1]
