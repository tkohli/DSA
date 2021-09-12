# Simplify Directory Path
"""
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

Absolute path always begin with ’/’ ( root directory ).

Path will not have whitespace characters.




Input Format

The only argument given is string A.
Output Format

Return a string denoting the simplified absolue path for a file (Unix-style).
For Example

Input 1:
    A = "/home/"
Output 1:
    "/home"

Input 2:
    A = "/a/./b/../../c/"
Output 2:
    "/c"
"""
class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        dirs = A.split('/')
        result = []
        for c in dirs:
            if c == '' or c == '.': continue
            elif c == '..':
                if len(result)>0: result.pop()
            else:
                result.append(c)
        return '/'+'/'.join(result)
# class Solution:
#     # @param A : string
#     # @return a strings
#     def simplifyPath(self, A):
#         dirs = A.split('/')
#         stack = []
#         for dir in dirs:
#             if dir == '.':
#                 continue
#             elif dir == "..":
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(dir)
#         return '/'+'/'.join(stack)