from cacheall.EvictionPolicies.LRUevictionpolicy import LRUCache
from cacheall.EvictionPolicies.LIFOevictionpolicy import LIFOCache
from cacheall.EvictionPolicies.FIFOevictionpolicy import FIFOCache
from dictionary import dict
import threading
import time

lock=threading.Lock()


# import json


# with open('dictionary.txt') as f:
# 	data = f.read()

# print("Data type before reconstruction : ", type(data))
	

# dict = json.loads(data)


# dict={0:FIFOCache,1:LRUCache,2:LIFOCache}
def cache_dec(size,eviction,verbose=0):
    cache=dict[eviction](size,lock,verbose)
    def decorator(func):
    
        def inner1(*args):
            #making the key by concatinating the arguments into a string
            s=''
            for g in args:
                s+=str(g)
                s+='.'
            # print(s)
            
            #checking if the value is found in the cache or not
            k=0
            if cache.get(s)==-1:
                k=func(*args)
                cache.set(s,k)
            else:
                k=cache.get(s)
            
            return k
        
        return inner1
   
    return decorator