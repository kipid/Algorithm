class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictNums = dict()
        for i in range(len(numbers)):
            dictNums[numbers[i]] = i
        for i in range(len(numbers)):
            if (target - numbers[i]) < numbers[i]:
                return
            if (target - numbers[i]) in dictNums:
                return [i+1, dictNums[target - numbers[i]]+1]