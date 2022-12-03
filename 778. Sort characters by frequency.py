class Solution:
  def frequencySort(self, s: str) -> str: 
    """
    Asked in amazon
    A naive solution would be to add counter then make 2D array and then sort it based on values 
    O(nlogn) time O(n) space
    
    We can also use heap but that won't be most optimized
    
    Optimization -
    lets start with counter again, then make a 2d list with empty array of size n i,e -> [[], [],...[]]
    then goto counter and based on that values append char at index based on values 
    then join it to make a string 
    O(n) time O(n) space 
    """
    n = len(s)
    ans = [[] for _ in range(len(s)+1)]
    cnt = Counter(s)
    for k,v in cnt.items():
      ans[v].append(k)
    res = ""
    for freq in range(len(s),-1,-1):
      for c in ans[freq]:
        res += c*freq
    return res
