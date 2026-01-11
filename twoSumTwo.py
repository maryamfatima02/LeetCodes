class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        prevMap = {} # Value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i

        return []

    def test(self):
        assert self.twoSum([1, 2, 3, 4, 5], 5) == [1, 2]
        assert self.twoSum([7,7], 14) == [0,1]
        print("All tests passed.")

if __name__ == "__main__":
    Solution().test()