

from random import random


class RandomizedSet:

    def __init__(self):
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        else:
            self.values.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.values:
            self.values.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        random_index = int(random() * len(self.values))
        return self.values[random_index]


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1), "true")
print(randomizedSet.remove(2), "false")
print(randomizedSet.insert(2), "true")
print(randomizedSet.getRandom(), "1 or 2")
print(randomizedSet.remove(1), "true")
print(randomizedSet.insert(2), "true")
print(randomizedSet.getRandom(), "2")


"""
Solution could run faster by implementing
-  an array for the random selection.
-  a dictionary to store the key values for quicker look up
-  dictionary values to be location in array

def __init__(self):
        self.num_map = dict()
        self.data = []
        
    def insert(self, val: int) -> bool:
        if val in self.num_map: return False

        # add the value and list index to map
        self.num_map[val] = len(self.data)
        # add the data to the list
        self.data.append(val)

        return True  

    def remove(self, val: int) -> bool:
        if val not in self.num_map: return False
        # main idea is to swap the val to be removed with the last element of list and pop in O(1)

        # update the position of last element to val's position in map
        val_pos = self.num_map[val]
        self.num_map[self.data[-1]] = val_pos  

        # swap the val with last index element in list
        self.data[val_pos], self.data[-1] =  self.data[-1], self.data[val_pos]

        # remove the element from map and list
        self.num_map.pop(val)
        self.data.pop()

        return True

    def getRandom(self) -> int:
        # The choice() method returns a randomly selected element from the specified sequence
        return random.choice(self.data)

"""

