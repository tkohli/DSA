class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = arr[-1]
        arr[-1] = -1
        for idx in reversed(range(len(arr)-1)):
            temp  = arr[idx]
            arr[idx] = rightMax
            rightMax = max(temp,rightMax)
        return arr