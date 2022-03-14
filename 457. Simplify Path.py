class Solution:
    def simplifyPath(self, path: str) -> str:
        startSlash = path[0] == '/'
        stack = []
        path = path.split("/")
        for dir in path:
            if dir == '..':
                if stack:
                    stack.pop()
            elif dir == '.' or dir == '/' or dir == '':
                continue
            else:
                stack.append(dir)

        ans = ""
        if startSlash:
            ans += '/'
        ans += "/".join(stack)
        return ans
