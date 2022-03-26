"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Solution we can use hashmap to map all values to their frequency
We can use doubly linked list for the same  
freq and index and then take 2 pointers to keep track of most and least freq 


"""


# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.curSize = 0
        self.listOnMostRecent = DoublyLinkedList()
        self.maxSize = maxSize or 1

    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.curSize == self.maxSize:
                self.removeLeastRecentKey()
            else:
                self.curSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        if self.listOnMostRecent is None:
            return None
        return self.listOnMostRecent.head.key

    def removeLeastRecentKey(self):
        keyToRemove = self.listOnMostRecent.tail.key
        self.listOnMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOnMostRecent.setHeadTo(node)

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key is not in cache")
        self.cache[key].value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None

    def setHeadTo(self, node):
        if self.head == node:
            return  # since it is pointing to most freq node
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            # only one node in ll
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBinding()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

    def removeBinding(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
