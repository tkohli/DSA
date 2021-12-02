# O(Depth of lowest descendant) Time | O(1) Space
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    """
    Find the difference between 2 nodes and then find the common parent.
    To find the nodes diff we will find their height so that's it.
    """
    depthOne = getDescendantDepth(descendantOne,topAncestor)
    depthTwo = getDescendantDepth(descendantTwo,topAncestor)
    # find the lower decendant up to same level so backTrack
    if depthOne>depthTwo:
        backTrackAncestralTree(descendantOne,descendantTwo,depthOne-depthTwo)
    else:
        backTrackAncestralTree(descendantTwo,descendantOne,depthTwo-depthOne)


def getDescendantDepth(descendant,topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth+=1
        descendant = descendant.ancestor
    return depth


def backTrackAncestralTree(lowerDecendant,higherDecendant,diff):
    while diff>0:
        lowerDecendant=lowerDecendant.ancestor
        diff-=1
    while lowerDecendant!=higherDecendant:
        lowerDecendant.ancestor
        higherDecendant.ancestor
    return lowerDecendant
    
        