class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        use a stack with length of word and depth
        """
        paths = input.split('\n')
        stack = []
        ans = 0
        for path in paths:
            p = path.split('\t')
            depth = len(p)-1
            name = p[-1]
            l = len(name)
            while stack and stack[-1][1] >= depth:
                stack.pop()
            if not stack:
                stack.append((l, depth))
            else:
                stack.append((l+stack[-1][0], depth))
            if '.' in name:
                ans = max(ans, stack[-1][0] + stack[-1][1])
        return ans
