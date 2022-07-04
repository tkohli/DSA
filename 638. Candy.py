"""
We can solve this questions by multiple ways
We can use 2 arrays left to right or we can use 1 array and then do
2 pass one from left to right and other from right to left using 2 different loops

Best solution is to keep track of local maxima and minima and then expand from point
"""


class Solution(object):
    def candy(self, scores):
        """
        :type ratings: List[int]
        :rtype: int
        """
        rewards = [1 for _ in scores]
        for i in range(1, len(scores)):
            if scores[i] > scores[i-1]:
                rewards[i] = rewards[i-1] + 1

        for i in range(len(rewards)-2, -1, -1):
            if scores[i] > scores[i+1] and rewards[i] <= rewards[i+1]:  # May already
                rewards[i] = rewards[i+1] + 1
        return sum(rewards)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        result = 1
        up = 1
        down = peak = 0
        for i in range(1, len(ratings)):
            # if rising, then update up/peak and clear down
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                result += up
            # if equal, then add 1 and clear up/down/peak
            elif ratings[i] == ratings[i - 1]:
                up = 1
                down = 0
                peak = 0
                result += 1
            # if declining, then update down and clear up
            else:
                up = 1
                down += 1
                result += down
                # if peak is not large enough, then we need to make peak larger
                if peak <= down:
                    result += 1
        return result
