class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listOfNumbers = {}
        status = False
        for i, n in enumerate(nums):
            currentNumber = n
            if currentNumber in listOfNumbers:
                status = True 
            listOfNumbers[n] = i
        return status