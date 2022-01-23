# This is a LRU Cache Implementation.
# Write an LRU Cache which takes the cache_size as input
# Implement the following methods:
# 1. GET (key), SET (key, value), DELETE (key)
# 2. Assume keys and values are strings
# 3. LRU key should be automatically flushed when a 
#    SET operation happens and max cache size has been reached
# 4. GET and SET operations should update the key to the most recently used
# Data Structures - Hash, Doubly Linked List (DLL), Node Object
# Algorithm - Update DLL for every SET/GET/DELETE Op
# **** SCROLL TO THE BOTTOM FOR Detail Analysis *******

class Node:
    def __init__ (self, key, value)->None:
        self.key = key      # Not needed but using to verifiction and testing purposes
        self.value = value

        self.next = None
        self.prev = None

class LRUCache:
    def __init__ (self, size)->None:
        self.mru    = None  # MRU Node
        self.lru    = None  # LRU Node

        self.cache_max = size
        self.cache_size = 0
        self.keys = {}
        

        print("\n\n\n***************")
        print (f"LRU Cache initialized. Max cache size = {self.cache_max}")
        print("***************\n\n")


    def set (self, key, value):
        if self.keys.get(key): 
            print("Key already exists, treating as update operation")
            # Add logic here to do a key update and move node to MRU
            self.get(key)
            return  #does nothing for now. will add logic later
            
        if self.cache_size >= self.cache_max:
            print(f"Max cache size {self.cache_max} reached, deleting LRU node {self.lru.key}")
            # Delete the LRU
            self.delete(self.lru.key)
        
        if self.mru == None:
            print("Creating FIRST NODE in cache\n")
            new_node = Node(key,value)  
            new_node.key = key
            new_node.value = value

            self.mru = new_node
            self.lru = new_node
            
            new_node.prev = None
            new_node.next = None

        else:
            print(f"Adding {key} TO HEAD of Cache\n")
            cur = self.mru
            new_node = Node(key,value)
            new_node.key = key
            new_node.value = value

            # Add the node to the MRU i.e. head node. LRU does not have to be updated.
            new_node.next = self.mru
            new_node.next.prev = new_node
            self.mru = new_node
            new_node.prev = None
            
        # Add the Key to the Hash map. Value is the address of the new_node
        self.keys[key] = new_node
        self.cache_size += 1
        print (f"Curr cache size ={self.cache_size}")
        return True


    def get (self, key):
        print ("\nGET")
        nodeval = self.keys.get(key)
        if not nodeval: return False

        print(f"key = {nodeval.key} val = {nodeval.value}")

        # Some temp values for use later.
        temp = self.mru
        old_mru = self.mru
        old_lru = self.lru

        # Make nodeval as MRU, in other words move to thea head of the list
        # Multiple Cases here

        # Case 1 - If it os the MRU node itself then dont do anything.
        if nodeval == self.mru:
            print("accessing MRU")
            pass #Do not do anything
            
        # Case 2 - There are only two nodes. Swap the LRU and MRU
        elif nodeval == self.lru and nodeval == self.mru.next:
            print("Only two nodes in the system. Swapping LRU and MRU")
            self.mru = self.lru
            self.lru = temp
            old_mru.next = None
            old_mru.prev = self.mru
            old_lru.prev = None
            old_lru.next = self.lru

        # Case 3 - There are more than two nodes. 
        # The node is LRU. Move it to MRU
        elif nodeval == self.lru:
            print ("Accessing LRU")
            print (f"bringing node key {nodeval.key} and value {nodeval.value} to MRU")
            self.lru = nodeval.prev
            nodeval.prev.next = None
            nodeval.next = self.mru
            old_mru.prev = nodeval
            self.mru = nodeval
            nodeval.prev = None

        # Case 4 - The node is somewhere in the middle of the list. 
        #          Move it to MRU.
        elif nodeval.prev != None and nodeval.next != None:
            print ("Accessing MIDDLE Node")
            print(f"nodeval.prev = {nodeval.prev.key}, nodeval.next = {nodeval.next.key} ")
            nodeval.prev.next = nodeval.next
            nodeval.next.prev = nodeval.prev
            nodeval.next = self.mru
            self.mru = nodeval
            old_mru.prev = nodeval
            nodeval.prev = None

        else:
            print ("ERROR! Catastrophically wrong went here.")
            #print(f"nodeval.prev = {nodeval.prev.key}, nodeval.next = {nodeval.next.key} ")

        # Return the nodeval
        if nodeval.value: 
            return nodeval.value
        else: 
            return None

    def delete (self,key):
        print("\nDELETE")

        # Find the address of the node that holds the value to the key
        nodeval = self.keys.get(key)

        if not nodeval:
            print(f"Key {key} not found")
            return

        print(f"key = {nodeval.key} val = {nodeval.value}")

        # Case 0 - Deleting the only node in cache
        if self.mru == nodeval and self.lru == nodeval:
            print("Deleting ONLY NODE")
            self.mru = None
            self.lru = None

        # Case 1 - Delete the MRU node
        elif self.mru == nodeval:
            print("Deleting MRU")
            self.mru = nodeval.next
            nodeval.next.prev = None
        
        # Case 2 - Delete the LRU node
        elif self.lru == nodeval:
            print("Deleting LRU")
            self.lru = nodeval.prev
            nodeval.prev.next = None

        # Case 3 - Delete a node somewhere in the middle
        else:
            print("Deletig MIDDLE Node\n")
            print(f"prev = {nodeval.prev.value}, next ={nodeval.next.value}")
            nodeval.prev.next = nodeval.next
            nodeval.next.prev = nodeval.prev

        # Just reinitialize the values in the object
        nodeval.next = None
        nodeval.prev = None
        nodeval.key = None
        nodeval.value = None

        #Now lets delete the key from the HASH
        self.keys.pop(key)

        self.cache_size -=1
        print(f"cache_size = {self.cache_size}")


    def traverse (self):
        print("FORWARD", end=" ")

        cur=self.mru
        if cur == None:
            print("cache is empty")
            return True
        keylist = ""
        vallist = ""
        while cur != None:
            keylist += str(cur.key) + "->"
            vallist += str(cur.value) + "->"
            cur = cur.next
        print(keylist)
        #print(vallist)

    def reverse (self):
        print("REVERSE", end=" ")

        cur=self.lru
        if cur == None:
            print("cache is empty")
            return True
        keylist = ""
        vallist = ""
        while cur != None:
            keylist += str(cur.key) + "->"
            vallist += str(cur.value) + "->"
            cur = cur.prev
        print(keylist)
        #print(vallist)

    def print_lru_node(self):
        cur = self.lru
        if cur:
            print (f"LRU ==> key={cur.key} value={cur.value}")
        else:
            print ("Cache is empty")
    

    def check_keymap (self, key):
        # Check if the key is in the key has or not.
        # If all items have been deleted, it MUST not exist
        node = lru_cache.keys.get(key)
        if node: 
            print (f"{node.key} EXISTS in the hashtable")
        else:
            print (f"{key} DOES NOT exist in the hashtable")


        return None



lru_cache = LRUCache(4)
lru_cache.set("1", "one")
lru_cache.set("2", "two")
lru_cache.set("3", "three")
lru_cache.set("4", "four")

lru_cache.traverse()
lru_cache.reverse()

lru_cache.set("5", "five")


lru_cache.get("1")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.get("2")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.get("1")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.delete("1")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.delete("4")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.get("3")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.get("2")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.delete("3")
lru_cache.traverse()
lru_cache.reverse()

lru_cache.check_keymap("2")

lru_cache.delete("2")
lru_cache.traverse()
lru_cache.reverse()

print(lru_cache.keys.get("1"))

lru_cache.check_keymap("2")

print("***********")
lru_cache.traverse()
lru_cache.set("5", "five")
lru_cache.set("2", "two")
lru_cache.set("1", "one")
lru_cache.set("9", "nine")
lru_cache.set("10", "ten")
lru_cache.traverse()
print("***********")




# Data Structures Used
#   Hash Table, NodeObject, Doubly Linked List, Global Variables to store MRU/LRU Keys and Values
#     HASH - A Hash is used to store each key so retrieval is a O(1) operation
#       - Key is mapped to a NodeID
#       - MRU Key # Updated for each GET, SET, DELETE as required
#       - LRU Key # Updated for each GET, SET, DELETE as required
#     Node Object - Which is a node for a Doubly Linked List
#       - Node consists of 
#       - Value # The value that needs to be retrieved
#       - Key  # This is optional and used primarily to debug. 
#       - Next # pointer to next node
#       - Prev # pointer to previous node
#     Doubly Linked List
#       - A doubly linked list is used to track the LRU and MRU
#       - GET, SET, DELETE operations will require updating both LRU/MRU as needed
# Algorithm
#     Each Operation (GET, SET, DELETE) has multiple cases
#     CASE A - MRU or Head Node Modification
#     CASE B - LRU or Tail Node Modification
#     CASE C - Middle Node Modification
#     Conditions
#       -  1 - If there are no nodes in the system e.g. SET
#       -  2 - If there is just one node in the system. SET, GET, DELETE
#       -  3 - If there are 2 Nodes in the system. I'm not sure if this is required but
#                  this emerged as a special case. I may have overthought this
#       -  4 - When there are more than 2 nodes
# Analysis 
#     HASH  **Time complexity O(1), Space Complexity O(n)**
#       - Enables retrieval as a O(1) operation. 
#       - All ops requires at least 1 Hash lookup. Probably max of 2 primarily 
#         for inserting a new Key
#     DOUBLY LINKED LIST - ** Time Complexity: O(1), Space Complexity O(n) **
#       - MRU/LRU Tracking enables O(1) operation
#       - In place Adjusting MRU/LRU during SET/GET/DELETE operations
#         since we only need to change the pointer values
#     FINAL ANALYSIS: Time - O(1); Space - O(n)
#       - Time Complexity - HASH + DOUBLE_LL
#           - O(1) ==> O(1) + O(1) = O(2 * 1) : Ignoring constant time of 2 ops we get O(1)
#       - Space Complexity - HASH + DOUBLE_LL
#           - O(n) ==> O(n) + O(n) = O(2n) : Ignoring constant space of 2 we get O(n)

