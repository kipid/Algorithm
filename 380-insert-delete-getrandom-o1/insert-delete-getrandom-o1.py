class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.ls = []
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.ls.append(val)
        self.map[val] = len(self.ls) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        t = self.map[val]
        l = self.ls[-1]
        self.ls[t] = l
        self.ls.pop()
        self.map[l] = t
        del self.map[val]
        return True

    def getRandom(self) -> int:

        # print(self.map)
        # print(self.ls)
        return random.choice(self.ls)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()