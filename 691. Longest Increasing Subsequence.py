"""
One of the classic question that you cannot miss OP OG Question 
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing 
subsequence is [2,3,7,101], therefore the length is 4.
"""
# naive solution create all sub set 2^n time
nums = [10, 9, 2, 5, 3, 7, 101, 18]
# DP Optimization
"""
we create a DP seq and the use a for loop to goto nums
then we keep track of all smaller values that come in loop 
then store max(seq[i], seq[j]+1) in our seq[i]
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [1 for _ in nums]
        for i in range(len(nums)):
            maxSeq = seq[i]
            # find prev max seq and then update it
            for j in reversed(range(i)):
                if nums[j] < nums[i]:
                    seq[i] = max(seq[i], seq[j]+1)
        return max(seq)


# super optimization
"""
we keep an array and in that we find where new element can be stored
if it exceeds the size then we append it else we update it's value
in our seq[i]. Note use Bisect_left function
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for num in nums:
            i = bisect.bisect_left(seq, num)
            if i == len(seq):
                seq.append(num)
            else:
                seq[i] = num
        return len(seq)
