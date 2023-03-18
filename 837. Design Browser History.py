# Design Browser History

"""
    Approach 1 -  using 2 Stacks
    Time Complexity = O(n) || Space Complexity = O(n)
    initialise two stack then for visit function push value in stack1 and make stack2 empty then for 
    back function pop value from stack1 and push that value into stack2 for steps times and return stack1 top value
    then for forward function pop value from stack2 and push tha value into stack1 and return stack1 top value.


    Approach 2 - using Doubly Linkedlist
    Time Complexity = O(n) || Space Complexity = O(n)
    for homepage make it linkedlist node called the root and a pointer cur pointing to root node
    for visit function make a new node and append it at cur.next and update cur to that node
    for back function go prev as many as steps times possible from cur and then return cur.val
    for forward function go next as many as steps times possible from cur and then return cur.val.

"""

class Linkedlist:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = Linkedlist(homepage)
        self.cur = self.root

    def visit(self, url: str) -> None:
        node = Linkedlist(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.cur.prev:
                return self.cur.val
            self.cur = self.cur.prev
        return self.cur.val        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.cur.next:
                return self.cur.val
            self.cur = self.cur.next
        return self.cur.val        


obj = BrowserHistory("leetcode.com")
print(obj.visit("google.com"))
print(obj.visit("facebook.com"))
print(obj.visit("youtube.com"))

print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))

print(obj.visit("linkedin.com"))

print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))

