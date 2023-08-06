from cacheall.Algorithms.doublylinkedlist import DoublyLinkedList as dll 
from .verbose import Verbose

# LRU cache class
class LIFOCache:

    def __init__(self, capacity,lock,verbose=0):
        # capacity: capacity of cache
        # Initialize all variable
        self.capacity = capacity
        self.map = {}
        self.hits=0
        self.misses=0
        self.verdata=Verbose(verbose)
        self.verbose=verbose
        self.list=dll()
        self.count = 0
        self.lock=lock


    # This method works in O(1)
    def get(self, key):
        with self.lock:
            result=-1
            if key in self.map:
                node = self.map[key]
                result = node.val
            self.verdata.get_data(key,result,self.list.head)
            if result==-1:
                self.misses+=1
            else:
                self.hits+=1
            return result

    # This method works in O(1)
    def set(self, key, value):
        with self.lock:
            if key in self.map:
                node = self.map[key]
                node.val = value
            else:
                if self.count < self.capacity:
                    self.count += 1
                    self.map[key]=self.list.addToHead(key,value)
                else:
                    del self.map[self.list.head.key]
                    self.list.deleteNode(self.list.head)
                    self.map[key]=self.list.addToHead(key,value)
            self.verdata.set_data(key,value,self.list.head)
        
    def get_info(self):
        print("Cache hits: {} , Cache misses: {}".format(self.hits,self.misses))



