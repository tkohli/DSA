# Union find and Disjoint set 
"""
  Disjoint set = 
  {
    {u-1,2,3},
    {u-4,5},
    {u-9},
    {u-6,7}
  }

  u is nothing just marking head / root of that set

  The union-find data structure is similar to a traditional set data structure
  in that it contains a collection of unique values. However, these values are
  spread out amongst a variety of distinct disjoint sets, meaning that no set
  can have duplicate values, and no two sets can contain the same value.

  1. createSet(value) - Adds a given value in a new set xontaining only that value
  2. union(valueOne,valueTwo) - Takes 2 values and determine which set they are in
                                If they are in different set then it is combined to
                                single set
  3. find(value) - return the representive of the set of which the value belongs 

  DryRun - with optimization
                            Parent              Rank
  createSet(5) - null       {5:5}               {5:0}  
  createSet(10) - null      {5:5,10:10}         {5:0,10:0}
  find(5) - 5               
  find(10) - 10
  union(5,10) - null        {5:5,10:5}         {5:1,10:0}
  find(5) - 5
  find(10) - 5
  createSet(20) - null      {5:5,10:5,20:20}   {5:1,10:0,20:0}
  find(20) - 20
  union(10,20) - null       {5:5,10:5,20:5}   {5:1,10:0,20:0}
  find(5) - 5
  find(10) - 5
  find(20) - 5

  Note - There is a process of path compression so it actually helps 
  if we have something like this 

            1
          / | \
        2   3   4
                |
                5
    rank of 1 = 2
  it will become 
            1
          / | \ \
        2   3   4  5
  5 will be at same level, rank of 1 = 1, for any ethical input the max rank would be 4
"""
#  Complete proper implementation with path compression
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        
    #O(1) time and space
    def createSet(self, value):
        self.parents[value] = value
        self.rank[value] = 0

    #O(1) Approx time | O(1) space
    def find(self, value):
        if value not in self.parents:
            return None
        if value != self.parents[value]:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]


    # O(1) Approx time | O(1) space
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return 
        valueOneRoot = self.find(valueOne)
        valueTwoRoot = self.find(valueTwo)
        if self.rank[valueOneRoot] > self.rank[valueTwoRoot]:
            self.parents[valueTwoRoot] = self.parents[valueOneRoot]
        elif self.rank[valueOneRoot] > self.rank[valueTwoRoot]:
            self.parents[valueOneRoot] = self.parents[valueTwoRoot]
        else:
            self.parents[valueOneRoot] = self.parents[valueTwoRoot]
            self.rank += 1


#------------------------------------
# Optimization
# class UnionFind:
#     def __init__(self):
#         self.parents = {}
#         self.rank = {}
        
#     #O(1) time and space
#     def createSet(self, value):
#         self.parents[value] = value
#         self.rank[value] = 0

#     #O(log(n)) time | O(1) space
#     def find(self, value):
#         if value not in self.parents:
#             return None
#         curParent = value
#         while curParent != self.parents[curParent]:
#             curParent = self.parents[curParent]
#         return curParent


#     # O(log(n)) time | O(1) space
#     def union(self, valueOne, valueTwo):
#         if valueOne not in self.parents or valueTwo not in self.parents:
#             return 
#         valueOneRoot = self.find(valueOne)
#         valueTwoRoot = self.find(valueTwo)
#         if self.rank[valueOneRoot] > self.rank[valueTwoRoot]:
#             self.parents[valueTwoRoot] = self.parents[valueOneRoot]
#         else:
#             self.parents[valueOneRoot] = self.parents[valueTwoRoot]



#------------------------------------
# Naive 
# class UnionFind:
#     def __init__(self):
#         self.parents = {}
        
#     #O(1) time and space
#     def createSet(self, value):
#         self.parents[value] = value

#     #O(n) time | O(1) space
#     def find(self, value):
#         if value not in self.parents:
#             return None
#         curParent = value
#         while curParent != self.parents[curParent]:
#             curParent = self.parents[curParent]
#         return curParent


#     # O(n) time | O(1) space
#     def union(self, valueOne, valueTwo):
#         if valueOne not in self.parents or valueTwo not in self.parents:
#             return 
#         valueOneRoot = self.find(valueOne)
#         valueTwoRoot = self.find(valueTwo)
#         self.parents[valueTwoRoot] = self.parents[valueOneRoot]
