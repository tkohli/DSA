# linked list  
"""
A linked list can be described asa ata structure which comprises of 
multiple nodes, which contains the address to next node in node.next 

often represented as 
1 -> 2 -> 3 -> 4
Where 1 is node.val and node.next points to next node which is node.next.val = 2
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
        