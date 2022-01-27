def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    array = []
    genHelper("", n, n, array)
    print(array)


def genHelper(cur, open, close, array):
    if len(cur) == 6:
        array.append(cur)
    if open:
        genHelper(cur+'(', open-1, close, array)

    if close > open:
        genHelper(cur+')', open, close-1, array)
    return array


generateParenthesis(3)
