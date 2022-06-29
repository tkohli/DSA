people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
"""
h = height of person 
k = number of person in front of him with greater height 
somehow we need to find a way to insert values such that we have fixed order
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        people.sort(key=lambda x: (-x[0],x[1]))
        for person in people:
            ans.insert(person[1],person) # pos to insert, value
        return ans