# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.infList = [[1, math.inf]]

    def popSmallest(self) -> int:
        toBePopped = self.infList[0][0]
        if self.infList[0][0] == self.infList[0][1]:
            self.infList.pop(0)
        else:
            self.infList[0][0] += 1
        return toBePopped

    def addBack(self, num: int) -> None:
        i = len(self.infList) - 1
        while num < self.infList[i][0] and i >= 0:
            if i > 0 and num == self.infList[i][0] - 1:
                if self.infList[i-1][1] + 1 == num:
                    self.infList[i][0] = self.infList[i-1][0]
                    if i > 0:
                        self.infList.pop(i-1)
                    break
                else:
                    self.infList[i][0] = num
                    break
            elif i == 0:
                self.infList[i:i] = [[num, num]]
            elif i > 0:
                if num < self.infList[i-1][0] - 1:
                    i -= 1
                    continue
                elif self.infList[i-1][1] + 1 == num:
                    self.infList[i-1][1] = num
                    break
                elif self.infList[i-1][1] >= num >= self.infList[i-1][0]:
                    break
                elif self.infList[i-1][1] + 1 < num < self.infList[i][0] - 1:
                    self.infList[i:i] = [[num, num]]
                    break
            i -= 1