class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        n = len(arr)
        per = int(n*5/100)
        lst = arr[per:len(arr)-per]
        return sum(lst)/float(len(lst))
