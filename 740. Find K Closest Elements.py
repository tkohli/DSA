"""
The array is sorted.
If we want find the one number closest to x,
we don't have to check one by one.
it's straightforward to use binary research.

Now we want the k closest,
the logic should be similar.


Explanation
Assume we are taking A[i] ~ A[i + k -1].
We can binary research i
We compare the distance between x - A[mid] and A[mid + k] - x

If x - A[mid] > A[mid + k] - x,
it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
and we have mid smaller than the right i.
So assign left = mid + 1.

Important
Note that, you SHOULD NOT compare the absolute value of abs(x - A[mid]) and abs(A[mid + k] - x).
It fails at cases like A = [1,1,2,2,2,2,2,3,3], x = 3, k = 3
"""
# Time O(log(N - K)) to binary research and find result
# Space O(K) to create the returned list.


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
