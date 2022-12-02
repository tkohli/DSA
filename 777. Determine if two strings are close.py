class Solution:
  def closeString(self, w1 : str, w2 : str) -> bool:
    """
    We need to check 2 things:
    1. Both strings should have same set of char
    2. Both string should have same frequencies of char
    eg: = "abbccddd" has [1,2,2,3] so does dbbaaccc.
    """
    return sorted(Counter(w1).values()) == sorted(Counter(w2).values()) and set(w1)==set(w2)
