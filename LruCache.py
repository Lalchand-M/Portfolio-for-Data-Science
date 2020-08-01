########################

from collections import OrderedDict


class LRU_Cache(object):
    
    def __init__(self, capacity):
        
        ############################################
        
        self.cache = OrderedDict()
        
        self.capacity = capacity

    def get(self, key):
        
      ###########################################

        try:  #####################################

            
            
            value = self.cache.pop(key)
            
            self.cache[key] = value
            
            return value

        except KeyError:
            
            return -1

    def set(self, key, value):
        
      #####################################################.

        if self.capacity == 0:
            
            print("Can't perform operations on 0 capacity cache")
            
            return

        if key in self.cache:  
            
     ########################################
    
            self.cache.pop(key)
        
            self.cache[key] = value

        else:  
            
       ############################
        
            if len(self.cache) < self.capacity:  # Still space on cache
                
                self.cache[key] = value

            else:  # No space available on cache
                
                self.cache.popitem(last=False)
                
                self.cache[key] = value


####################################

#########################################
our_cache = LRU_Cache(5)

our_cache.set(1, 1)

our_cache.set(2, 2)

our_cache.set(3, 3)

our_cache.set(4, 4)

print(our_cache.get(1))

###################################

print(our_cache.get(2))

###############################################

print(our_cache.get(9))
##############################################

our_cache.set(5, 5)

our_cache.set(6, 6)

print(our_cache.get(3))

#################################################

our_cache = LRU_Cache(2)

our_cache.set(1, 1)

our_cache.set(2, 2)

our_cache.set(1, 10)

print(our_cache.get(1))

#################################

print(our_cache.get(2))

################################

our_cache = LRU_Cache(0)

our_cache.set(1, 1)

################################################

print(our_cache.get(1))

#################################################

