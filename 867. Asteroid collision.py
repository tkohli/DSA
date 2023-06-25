class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []
        for a in ast:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)

        return stack
