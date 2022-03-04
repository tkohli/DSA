strs = ["eat","tea","tan","ate","nat","bat"]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {} 
        for st in strs:
            temp = "".join(sorted(st))
            if temp not in dct:
                dct[temp] = [st]
            else:
                dct[temp].append(st)


        ans = []
        for val in dct.values():
            ans.append(val)

        return  ans