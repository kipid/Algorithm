class RandomizedSet:

    def __init__(self):
        self.set_ = set()

    def insert(self, val: int) -> bool:
        if val in self.set_:
            return False
        else:
            self.set_.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.set_:
            self.set_.remove(val)
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return list(self.set_)[randrange(len(self.set_))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()