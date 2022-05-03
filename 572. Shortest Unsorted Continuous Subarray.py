class Solution:
    def findUnsortedSubarray(self, array: List[int]) -> int:
        if len(array) == 1:
            return 0

        def isOutOfOrder(i, num, array):
            if i == 0:
                return num > array[i+1]
            if i == len(array)-1:
                return num < array[i-1]
            return num > array[i+1] or num < array[i-1]

        minOutOfOrder = float("inf")
        maxOutOfOrder = float("-inf")
        for i in range(len(array)):
            num = array[i]
            if isOutOfOrder(i, num, array):
                minOutOfOrder = min(minOutOfOrder, num)
                maxOutOfOrder = max(maxOutOfOrder, num)
        if minOutOfOrder == float("inf"):
            return 0
        subarrayLeftIdx = 0
        while minOutOfOrder >= array[subarrayLeftIdx]:
            subarrayLeftIdx += 1
        subarrayRightIdx = len(array)-1
        while maxOutOfOrder <= array[subarrayRightIdx]:
            subarrayRightIdx -= 1
        if subarrayRightIdx == subarrayLeftIdx:
            return 0
        return subarrayRightIdx-subarrayLeftIdx+1
