class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        stack = []
        for i in range(min(n, 9), 0, -1):
            stack.append(i)

        res = []
        while stack:
            last = stack.pop()
            if last > n:
                continue
            else:
                res.append(last)

            for i in range(9, -1, -1):
                stack.append(last*10+i)

        return res
