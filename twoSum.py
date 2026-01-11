class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        return []

    def test(self):
        assert self.twoSum([2,7,11,15], 9) == [0,1]
        assert self.twoSum([3,2,4], 6) == [1,2]
        assert self.twoSum([3,3], 6) == [0,1]
        print("All tests passed.")
    
if __name__ == "__main__":
    Solution().test()