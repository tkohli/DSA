class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        allNum = [12, 23, 34, 45, 56, 67, 78, 89,
                  123, 234, 345, 456, 567, 678, 789,
                  1234, 2345, 3456, 4567, 5678, 6789,
                  12345, 23456, 34567, 45678, 56789,
                  123456, 234567, 345678, 456789,
                  1234567, 2345678, 3456789,
                  12345678, 23456789,
                  123456789]
        seq = []
        for i in range(len(allNum)):
            if allNum[i] >= low and allNum[i] <= high:
                seq.append(allNum[i])
            elif allNum[i] > high:
                break
        return seq
