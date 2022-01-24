from multiprocessing.dummy import current_process


def generateDivTags(numberOfTags):
    divTag = []
    helper("", numberOfTags, numberOfTags, divTag)
    # Write your code here.
    print(divTag)


def helper(curr, o, c, divTag):
    if o == 0 and c == 0:
        divTag.append(curr)
    if o:
        helper(curr+'<div>', o-1, c, divTag)
    if o < c:
        helper(curr+'</div>', o, c-1, divTag)


generateDivTags(3)
