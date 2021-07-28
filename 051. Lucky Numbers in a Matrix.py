# Lucky Numbers in a Matrix
"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
"""


def luckyNumbers(matrix):
    """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    row = []
    col = []
    out = []
    for mat in matrix:
        row.append(min(mat))
    for j in range(len(matrix[0])):
        colmn = [num[j] for num in matrix]
        col.append(max(colmn))
    for r in row:
        if r in col:
            out.append(r)
    return out

    # common_elements = set(row).intersection(col)
    # return (list(common_elements))


#         row = []
#         col = []
# #         for mat in matrix:
# #             row.append(min(mat))

# #         print(row)
#         x = len(matrix)
#         if len(matrix[0]) == 1:
#             # print()
#             return max(matrix)
#         for i in range(len(matrix[0])):
#             if i < x:
#                 row.append(min(matrix[i]))
#             j = 0
#             m = 0
#             lst = []
#             while j <= x-1:
#                 print(matrix[j][i])
#                 lst.append(matrix[j][i])
#                 j += 1
#             col.append(max(lst))
#             # print(matrix)

#         print(col)
#         common_elements = set(row).intersection(col)
#         return (list(common_elements))
