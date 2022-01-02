class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prev = 0
        total = 0
        for laser in bank:
            temp = 0
            for l in laser:
                if l == '1':
                    temp += 1
            if prev == 0:
                prev = temp
                temp = 0
            if temp != 0:
                total += (prev*temp)
                prev = temp
        return total
