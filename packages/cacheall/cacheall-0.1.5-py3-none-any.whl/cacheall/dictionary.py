from cacheall.EvictionPolicies.LRUevictionpolicy import LRUCache
from cacheall.EvictionPolicies.LIFOevictionpolicy import LIFOCache
from cacheall.EvictionPolicies.FIFOevictionpolicy import FIFOCache
dict= {0:FIFOCache,
    1:LRUCache,
    2:LIFOCache}