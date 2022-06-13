class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [float("inf") for _ in range(amount+1)]
        minCoins[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                minCoins[i] = min(minCoins[i], minCoins[i-coin]+1)
        return minCoins[-1] if minCoins[-1] != float("inf") else -1
